import json
import logging
import time
from langchain_google_vertexai import ChatVertexAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_google_vertexai import VertexAI
from google.oauth2 import service_account
from pdfminer.high_level import extract_text
import yaml
import os
import pandas as pd
from cachetools import TTLCache
from langsmith import traceable
from vertexai.preview.generative_models import GenerativeModel

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class DocumentIngestion:
    def __init__(self, config_file="config/config.yaml"):
        start_time = time.time()
        config = self._load_config(config_file)

        self.project_id = config["project"]["id"]
        self.region = config["project"]["region"]
        self.credentials = self._initialize_credentials(config["google"]["service_account_file"])
        self.llm_model = config["llm"]["model"]
        self.cache = TTLCache(maxsize=config["cache"]["maxsize"], ttl=config["cache"]["ttl"])
        self.model = GenerativeModel(f"{self.llm_model}-001")

        # Initialize an empty DataFrame to store summaries chunk by chunk
        self.summary_df = pd.DataFrame(columns=["chapter_title", "chunk_number", "summary_text"])
        
        logger.info(f"DocumentIngestion initialized in {time.time() - start_time:.2f} seconds")

    @staticmethod
    def _load_config(config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config

    def _initialize_credentials(self, service_account_file):
        credentials = service_account.Credentials.from_service_account_file(service_account_file)
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_file
        logger.info(f"Authenticated with service account: {credentials.service_account_email}")
        return credentials

    @staticmethod
    def _log_execution_time(method):
        """Decorator to log execution time of a method."""
        def timed_method(*args, **kwargs):
            start_time = time.time()
            result = method(*args, **kwargs)
            logger.info(f"{method.__name__} completed in {time.time() - start_time:.2f} seconds")
            return result
        return timed_method

    @traceable(name="generate_summary_for_chapter_pdf")
    @_log_execution_time
    def generate_summary_for_chapter_pdf(self, pdf_path, chapter_title):
        chapter_text = self._extract_text(pdf_path)
        chunks = self._split_text_into_chunks(chapter_text, chunk_size=2000)
        chapter_summary = self._process_and_store_chunks(chunks, chapter_title)
        return " ".join(chapter_summary)

    @_log_execution_time
    def _extract_text(self, pdf_path):
        """Extracts text from a PDF file."""
        return extract_text(pdf_path)

    def _split_text_into_chunks(self, text, chunk_size=2000):
        """Splits text into manageable chunks."""
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        logger.info(f"Split text into {len(chunks)} chunks")
        return chunks

    def _process_chunks(self, chunks, chapter_title):
        """Processes each chunk with the model and returns the combined summary."""
        chapter_summary = []
        for idx, chunk in enumerate(chunks, start=1):
            logger.info(f"Processing chunk {idx}/{len(chunks)}")
            response = self._generate_summary_for_chunk(chunk, chapter_title)
            chapter_summary.append(response)
        return chapter_summary
    
    def _process_first_chunk(self, chunks, chapter_title):
        """Processes only the first chunk with the model and returns the summary."""
        if not chunks:
            logger.warning("No chunks to process.")
            return []
        
        # Process only the first chunk
        logger.info(f"Processing the first chunk out of {len(chunks)} total chunks")
        response = self._generate_summary_for_chunk(chunks[0], chapter_title)
        return [response]

    def _process_and_store_chunks(self, chunks, chapter_title):
        """Processes each chunk with the model, adds each summary to the DataFrame."""
        for idx, chunk in enumerate(chunks[:5], start=1):
            logger.info(f"Processing chunk {idx}/{len(chunks)}")
            response = self._generate_summary_for_chunk(chunk, chapter_title)
            # Print the generated summary for each chunk
            print(f"Summary for {chapter_title}, Chunk {idx}:\n{response}\n")
            self._add_summary_to_dataframe(chapter_title, idx, response)
    
    def _add_summary_to_dataframe(self, chapter_title, chunk_number, summary_text):
        """Adds the generated summary for each chunk to the DataFrame."""
        new_row = {"chapter_title": chapter_title, "chunk_number": chunk_number, "summary_text": summary_text}
        self.summary_df = pd.concat([self.summary_df, pd.DataFrame([new_row])], ignore_index=True)
        logger.info(f"Summary for '{chapter_title}', chunk {chunk_number} added to DataFrame.")


    @_log_execution_time
    def _generate_summary_for_chunk(self, chunk, chapter_title):
        """Generates a summary for a single chunk of text."""
        prompt = self._create_prompt(chunk, chapter_title)
        response = self.model.generate_content(prompt)
        return response.text

    def _create_prompt(self, chunk, chapter_title):
        """Creates the prompt for the language model."""
        return f"""
        Analyze the following text to identify chemicals and compounds relevant to the food industry in the context of "{chapter_title}".
        Focus on documenting the names of compounds and their effects on human health.

        Chapter Title: {chapter_title}
        Chapter Text:
        {chunk}

        Format the output using the following structure:
        {{
            "compound_1": "effect description",
            "compound_2": "effect description",
            ...
        }}
        """

if __name__ == "__main__":
    pdf_path = "data/books/PreservativesChapter1.pdf"
    chapter_title = "Antioxidants and Radical Scavengers"

    document_ingestion = DocumentIngestion(config_file="config/config.yaml")

    try:
        result = document_ingestion.generate_summary_for_chapter_pdf(pdf_path, chapter_title)
        print("Generated Summary for Chapter:")
        print(result)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
