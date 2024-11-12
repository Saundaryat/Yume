import os
import json
import firebase_admin
from firebase_admin import credentials
from google.oauth2 import service_account

def initialize_firebase():
    # Construct the service account information from environment variables
    service_account_info = {
        "type": "service_account",
        "project_id": "yume-f1311",
        "private_key_id": "ea9e2a03f99c9ee4eabaffaa3d0a0b8dc41cf809",
        "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": "firebase-adminsdk-y3n6v@yume-f1311.iam.gserviceaccount.com",
        "client_id": "100477777189804071941",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-y3n6v%40yume-f1311.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com"
    }

    # Save to a JSON file (e.g., "firebase_key.json")
    with open("firebase_key.json", "w") as json_file:
        json.dump(service_account_info, json_file)

    # Load from the JSON file and initialize Firebase
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)
