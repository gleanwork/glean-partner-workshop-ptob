import requests

# Configuration variables
SEARCH_API_URL = "support-lab-be.glean.com/rest/api/v1/search"  # The domain for the API endpoint.
SEARCH_API_TOKEN = "<INSERT_GLEAN_SEARCH_API_TOKEN>"  # Replace with your Glean Search API token.
DATASOURCE = "<INSERT_YOUR_DATASOURCE_NAME>" # Replace with your Glean Datasource name (i.e. ptobpartnerwsXX)
SEARCH_QUERY = "Propensity to Buy"  # The search term to query.
NUMBER_OF_RESULTS = 2  # Number of search results to retrieve (allowed values: 1-50).

def print_results(results):
    """
    Prints the search results in a readable format.
    
    Parameters:
    - results (list): List of document results retrieved from the API.
    """
    if not results:
        print("No results found.")
        return
    
    print("\nSearch Results:")
    for idx, result in enumerate(results):
        doc = result.get("document", result)
        doc_id = doc.get("id", "N/A")
        title = doc.get("title", "N/A")
        # Prefer 'url' but fallback to 'viewURL' if present.
        url = doc.get("url") or doc.get("viewURL", "N/A")
        ds = doc.get("datasource", "N/A")
        metadata = doc.get("metadata", {})
        create_time = metadata.get("createTime", "N/A")
        update_time = metadata.get("updateTime", "N/A")
        
        # Print the details for each document.
        print("-" * 40)
        print(f"Result #{idx+1}")
        print(f"Document ID: {doc_id}")
        print(f"Title      : {title}")
        print(f"URL        : {url}")
        print(f"Datasource : {ds}")
        print(f"Created    : {create_time}")
        print(f"Updated    : {update_time}")
        print("-" * 40)
        print("\nFull Metadata:")
        print(f"Metadata   : {metadata}")

def search_documents(api_url, api_token, search_query, num_results):
    headers = {
        'Authorization': f'Bearer {api_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "datasource": DATASOURCE,
        "query": search_query,
        "limit": num_results
    }
    response = requests.post(api_url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        print(f"Error {response.status_code}: {response.text}")
        return []

def main():
    """
    Main function to construct the API URL, send the search query, 
    and print out the results.
    """
    print("\nSearching for documents...")
    # Fetch results from the API based on the search query.
    results = search_documents(SEARCH_API_URL, SEARCH_API_TOKEN, SEARCH_QUERY, NUMBER_OF_RESULTS)
    # Print the search results in a readable format.
    print_results(results)

if __name__ == "__main__":
    main()
