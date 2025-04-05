import requests
import json

# Configuration: set these variables as needed
DELETION_API_URL = "https://support-lab-be.glean.com/api/index/v1/deletedocument"
INDEX_API_TOKEN = "<INSERT_GLEAN_INDEXING_API_TOKEN>"  # Replace with your Glean Indexing API token
DATASOURCE = "<INSERT_GLEAN_INDEXING_API_TOKEN>" # Replace with your Glean Datasource name (i.e. ptobpartnerwsXX)
DOCUMENT_ID = "<INSERT_DOCUMENT_ID>" # Insert DocumentID. This can be found by running 3_searchDocument.py. The format will be something like: Document_ptobpartnerwsXX


def delete_document(api_url, token, doc_id, datasource):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    payload = {
        "datasource": datasource,
        "id": doc_id
    }
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    print("Status Code:", response.status_code)
    if response.text.strip():
        try:
            parsed = response.json()
            print("Response JSON:")
            print(json.dumps(parsed, indent=2))
        except json.decoder.JSONDecodeError:
            print("Response is not valid JSON:")
            print(response.text)
    else:
        print("No response body returned.")

def main():
    print("Deleting document via the Glean API")
    print(f"Deleting document with ID '{DOCUMENT_ID}' from datasource '{DATASOURCE}'...")
    delete_document(DELETION_API_URL, INDEX_API_TOKEN, DOCUMENT_ID, DATASOURCE)

if __name__ == "__main__":
    main()
