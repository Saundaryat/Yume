import os
import json
from google.oauth2 import service_account

def initialize_google():
    # Load JSON with placeholder
    with open("config/keys.json", "r") as json_file:
        service_account_info = json.load(json_file)

    # Substitute the placeholder with the environment variable
    service_account_info["private_key"] = os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n")

    # Initialize credentials with substituted private key
    credentials = service_account.Credentials.from_service_account_info(service_account_info)
    
    print("Google credentials initialized successfully.")
    #os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "config/keys.json"
    return credentials
