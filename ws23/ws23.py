"""
ws23 turns your web search into triples
"""
import requests
from rdflib import Graph
from google import search

ANY23URL = "http://any23.org/any23/"
ANY23_FORMAT = "ntriples"
TRIPLES_TOKEN = "> .\n"
TRIPLES_SEP = "\n"
RDFLIB_FORMAT = "n3"

def web_search_to_triples(query, num=30):
    """
    Returns: a list of n3-serialized RDF triples.
    """
    
    # return object
    triples = []

    # if query is defined... go!
    if query:
        g = Graph()
        urls = [str(u) for u in search(query, stop=num)]
        for u in urls:
            params = { "format": ANY23_FORMAT, "url": u }
            r = requests.get(ANY23URL, params=params)
            serialized_triples = r.text
            if TRIPLES_TOKEN in serialized_triples:
                ts = serialized_triples.split(TRIPLES_SEP)
                for t in ts:
                    g.parse(data=t, format=RDFLIB_FORMAT)
        triples = g.serialize(format=RDFLIB_FORMAT).split("\n")

    # return
    return triples

if __name__ == '__main__':
    import sys
    query = sys.argv[1]
    num = 10
    if len(sys.argv) > 2:
        num = int(sys.argv[2])
    triples = web_search_to_triples(query, num=num)
    
    for t in triples:
        print t
