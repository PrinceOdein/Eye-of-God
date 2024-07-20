import requests
from settings import API_KEY, SEARCH_ENGINE_ID, COUNTRY, MAX_RESULTS
from storage import store_results, get_ranked_results

def perform_search(query):
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&gl={COUNTRY}"
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        results = []
        for item in data['items'][:MAX_RESULTS]:
            result = {
                'title': item['title'],
                'link': item['link'],
                'snippet': item['snippet']
            }
            results.append(result)
        store_results(query, results)
        return get_ranked_results(query, results)
    else:
        return []