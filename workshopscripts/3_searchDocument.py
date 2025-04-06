import requests
from datetime import datetime

# Default configuration values (modify these directly in the script)
DOMAIN = "https://support-lab-be.glean.com/rest/api/v1/search"
SEARCH_API_TOKEN = "<INSERT_GLEAN_SEARCH_API_TOKEN>"  # Replace with your Glean Search API token.
DATASOURCE = "<INSERT_YOUR_DATASOURCE_NAME>" # Replace with your Glean Datasource name (i.e. ptobpartnerwsXX)
QUERY = "Propensity to Buy"  # Replace with your search term
NUM_RESULTS = 2  # Number of search results to retrieve (allowed values: 1-50)

def search_documents(api_url, token, query, page_size, datasource):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    # Use the documented requestOptions for filtering by datasource.
    payload = {
        "query": query,
        "pageSize": page_size,
        "includeFields": ["datasource", "metadata", "title", "url", "document"],
        "requestOptions": {
            "datasourceFilter": datasource
        }
    }
    print("Sending search payload:")
    print(payload)
    
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(response.text)
        return None
    
    data = response.json()
    # Detailed document results are expected to be in the "results" key.
    return data.get("results", [])

def print_results(results):
    if not results:
        print("No results found.")
        return
    
    print("\nSearch Results:")
    for idx, result in enumerate(results):
        doc = result.get("document", result)
        doc_id = doc.get("id", "N/A")
        title = doc.get("title", "N/A")
        url = doc.get("url") or doc.get("viewURL", "N/A")
        ds = doc.get("datasource", "N/A")
        metadata = doc.get("metadata", {})
        create_time = metadata.get("createTime", "N/A")
        update_time = metadata.get("updateTime", "N/A")
        try:
            if create_time != "N/A":
                create_time = datetime.fromisoformat(create_time).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pass
        try:
            if update_time != "N/A":
                update_time = datetime.fromisoformat(update_time).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pass
        
        print("-" * 40)
        print(f"Result #{idx+1}")
        print(f"Document ID: {doc_id}")
        print(f"Title      : {title}")
        print(f"URL        : {url}")
        print(f"Datasource : {ds}")
        if create_time != "N/A":
            print(f"Created    : {create_time}")
        if update_time != "N/A":
            print(f"Updated    : {update_time}")

def main():
    api_url = DOMAIN
    print("Using the following configuration:")
    print(f"Domain          : {DOMAIN}")
    print(f"Datasource      : {DATASOURCE}")
    print(f"Search Term     : {QUERY}")
    print(f"Number of Results: {NUM_RESULTS}")
    print("\nSearching for documents...")
    results = search_documents(api_url, SEARCH_API_TOKEN, QUERY, NUM_RESULTS, DATASOURCE)
    print_results(results)

if __name__ == "__main__":
    main()
