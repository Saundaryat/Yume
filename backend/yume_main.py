import os
import pandas as pd
from config import load_config
from chain import Chain
from health_analyzer import HealthAnalyzer
from search import KeywordSearch
from app import APP

def main():
    load_config()
    
    df = pd.read_csv('data/user_data.csv')

    llm_chain = Chain(df)
    health_analyzer = HealthAnalyzer(llm_chain, df)
    search = KeywordSearch()
    app = APP(health_analyzer, search)
    
    app.run()

if __name__ == '__main__':
    main()