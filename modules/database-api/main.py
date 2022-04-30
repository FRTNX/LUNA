from wikipedia.wikipedia import summary
import db_handler as persistence
import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/dbquote')
def fetch_quote():
    return persistence.fetch_quote()

@app.route('/dbwiki')
def fetch_wikipage():
    page_title = request.args['title']
    return persistence.fetch_document('intelligence', page_title, summary=False)

@app.route('/wikisearch')
def search_wikipedia_db():
    search_term = request.args['searchTerm']
    return json.dumps(persistence.search_wikipedia_db(search_term))

@app.route('/wikirandomlist')
def fetch_random_wiki_list():
    return persistence.list_titles_by_tag('random')

@app.route('/')
def status():
    return 'OK'

if __name__ == '__main__':
    app.run()


