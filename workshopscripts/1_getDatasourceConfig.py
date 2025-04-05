import json
import requests

INDEX_API_URL = "https://support-lab-be.glean.com/api/index/v1/getdatasourceconfig"
INDEX_API_TOKEN = "<INSERT_GLEAN_INDEXING_API_TOKEN>"  # Replace with your Glean Indexing API token
DATASOURCE = "<INSERT_YOUR_DATASOURCE_NAME>" # Replace with your Glean Datasource name (i.e. ptobpartnerwsXX)

url = INDEX_API_URL
headers = {
    "Authorization": "Bearer " + INDEX_API_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "datasource": DATASOURCE
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)

try:
    # Try to parse the response as JSON and pretty-print it
    response_data = response.json()
    print("Response Body:")
    print(json.dumps(response_data, indent=4))
except ValueError:
    # If the response isn't JSON, print the raw text
    print("Response is not in JSON format:")
    print(response.text)
