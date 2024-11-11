import os
import json
from google.oauth2 import service_account

def initialize_google():
    # Construct the service account information from environment variables
    service_account_info = {
        "type": "service_account",
        "project_id": "wf-gcp-us-estetica2-sbx",
        "private_key_id": "b50699314bad458ee4351b30c4b5e0263d2bf05e",
        "private_key":  os.getenv("GOOGLE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": "949772750044-compute@developer.gserviceaccount.com",
        "client_id": "117500036807747510026",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/949772750044-compute%40developer.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }

    
    credentials = service_account.Credentials.from_service_account_info(service_account_info)

    return credentials
