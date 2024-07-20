from flask import Flask, request, render_template
import requests
import pandas as pd

app = Flask(__name__)

API_KEY = 'AIzaSyAwwYyJht9kA086LZSuArBUo6muJyjmUgw'
SEARCH_ENGINE_ID = 'd5d88d720d58b488b'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"
    
    response = requests.get(url)
    data = response.json()

    if 'items' in data:
        results = []
        for item in data['items']:
            results.append({
                'title': item['title'],
                'link': item['link'],
                'snippet': item['snippet']
            })
        return render_template('results.html', results=results)
    else:
        return "No results found."

if __name__ == '__main__':
    app.run(debug=True)