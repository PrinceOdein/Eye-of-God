from flask import Flask, request, render_template
from search import perform_search

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    results = perform_search(query)
    return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)