import pandas as pd

search_results = pd.DataFrame(columns=['query', 'title', 'link', 'snippet', 'relevance'])

def store_results(query, results):
    global search_results
    for result in results:
        search_results = search_results.append({
            'query': query,
            'title': result['title'],
            'link': result['link'],
            'snippet': result['snippet'],
            'relevance': 1  # Initial relevance score
        }, ignore_index=True)

def get_ranked_results(query, results):
    global search_results
    ranked_results = []
    for result in results:
        matching_result = search_results[(search_results['query'] == query) & (search_results['link'] == result['link'])]
        if not matching_result.empty:
            # Update relevance score based on user interaction or other factors
            relevance_score = matching_result['relevance'].values[0] + 1
            search_results.loc[(search_results['query'] == query) & (search_results['link'] == result['link']), 'relevance'] = relevance_score
            result['relevance'] = relevance_score
            ranked_results.append(result)
    return sorted(ranked_results, key=lambda x: x['relevance'], reverse=True)