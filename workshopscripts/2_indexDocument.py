import os
import json
import requests

# API configuration
INDEX_API_URL = "https://support-lab-be.glean.com/api/index/v1/indexdocument" # This doesn't need to be changed
PTOB_FILE_PATH = "./propensityToBuyData.json" # This doesn't need to be changed, unless you want to index a different document later

INDEX_API_TOKEN = "<INSERT_GLEAN_INDEXING_API_TOKEN>"  # Replace with your Glean Indexing API token
DATASOURCE = "<INSERT_YOUR_DATASOURCE_NAME>" # Replace with your Glean Datasource name (i.e. ptobpartnerwsXX)
ATTENDEE_NAME = "<INSERT YOUR WORKSHOP ATTENDEE NAME>" # Replace with your Glean Partner Workshop name (i.e. Partner WorkshopXX). This is used for the author and owner fields in the payload.
ATTENDEE_NUMBER = "<INSERT YOUR WORKSHOP ATTENDEE NUMBER>" # Replace with your Glean Partner Workshop number (i.e. ptobpartnerwsXX). This is used for the author and owner fields in the payload.


def index_document(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Define document ID and view URL.
    doc_id = DATASOURCE
    view_url = "https://docs.google.com/document/d/1Nvb3YUzEuUOK0EBfz2MMnyNx4m2XmAz1W54h9ZeJBxA/"

    payload = {
        "version": 1,
        "document": {
            "id": doc_id,
            "datasource": DATASOURCE,
            "objectType": "Document",
            "viewURL": view_url,
            "title": "Propensity to Buy Data - " + DATASOURCE,
            "filename": "Propensity to Buy Data - " + DATASOURCE,
            "summary": {
                "mimeType": "text/plain",
                "textContent": "Propensity to Buy data showing which customers are most likely to close a deal."
            },
            "body": {
                "mimeType": "text/plain",
                "textContent": content
            },
            "author": {
                "email": ATTENDEE_NUMBER + "@glean-sandbox.com",
                "name": ATTENDEE_NAME
            },
            "owner": {
                "email": ATTENDEE_NUMBER + "@glean-sandbox.com",
                "name": ATTENDEE_NAME
            },
            "permissions": {
                "allowAnonymousAccess": True
            },
            "createdAt": 1711824000, # Hardcoded timestamp (in Unix epoch seconds)
            "updatedAt": 1712428800, # Hardcoded timestamp (in Unix epoch seconds)
            "updatedBy": {
                "email": ATTENDEE_NUMBER + "@glean-sandbox.com",
                "name": ATTENDEE_NAME
            },
            "tags": ["Propensity to Buy Data", "PartnerWorkshop"],
            "interactions": {
                "numViews": 10,
                "numLikes": 10,
                "numComments": 0
            },
            "status": "active",
            "additionalUrls": [],
            "comments": []
        }
    }

    # Print the payload being sent.
    print("Payload being sent:")
    print(json.dumps(payload, indent=2))

    headers = {
        "Authorization": f"Bearer {INDEX_API_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(INDEX_API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            print(f"Document indexed successfully. Response status: {response.status_code}")
        else:
            print(f"Failed to index document. Response status: {response.status_code}")
            print("Response:", response.text)
    except Exception as e:
        print(f"Error during API request: {e}")

def main():
    file_path = os.path.expanduser(PTOB_FILE_PATH)
    index_document(file_path)

if __name__ == "__main__":
    main()
