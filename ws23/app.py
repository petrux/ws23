from flask import Flask, render_template, request
from rdflib import Graph
from google import search
import requests
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
    triples = []

    if query:
        g = Graph()
        urls = [str(u) for u in search(query, stop=10)]
        for u in urls:
            params = { "format": ANY23_FORMAT, "url": u }
            r = requests.get(ANY23URL, params=params)
            serialized_triples = r.text
            if TRIPLES_TOKEN in serialized_triples:
                ts = serialized_triples.split(TRIPLES_SEP)
                print str(len(ts)) + " triples for " + u
                for t in ts:
                    g.parse(data=t, format=RDFLIB_FORMAT)
        print "serializing all the " + str(len(g))+  " triples..."
        triples = g.serialize(format=RDFLIB_FORMAT).split("\n")
        print "serializing all the " + str(len(triples))+  " triples..."
        print "...done!"
    
    return render_template("search.html",
                           actual_query=query,
                           triples=triples)

if __name__ == '__main__':
    APP.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", "5000")))
