from flask import Flask, render_template, request
from ws23 import web_search_to_triples
import sys
import os


ANY23URL = "http://any23.org/any23/"
ANY23_FORMAT = "ntriples"
TRIPLES_TOKEN = "> .\n"
TRIPLES_SEP = "\n"
RDFLIB_FORMAT = "n3"
APP = Flask(__name__)

@APP.route("/")
def home():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    query = request.args.get("q")
    triples = web_search_to_triples(query)
    return render_template("search.html",
                           actual_query=query,
                           triples=triples)

if __name__ == '__main__':
    APP.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", "5000")))
