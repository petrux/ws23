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

def google_search(query, num):
    """
    Return the first ``num`` results from the Google search for the given ``query``.

    Arguments:
        query: a query string
    	num: the max number of results to be returned

    Returns:
    	an iterable of strings representing the resulting URLs
    """
    
    results = [str(u) for u in search(query, stop=num)]
    if len(results) > num:
        return results[:num]
    return results


def any23(url, format=ANY23_FORMAT):
    """
    Return the triples extracted by Any23 from the given ``url`` in the specified ``format``.

    Arguments:
    	url: the url to be scanned
    	format: the preferred format for the triples

    Returns:
    	the Any23 result in the form of plain text to be parsed into triples if any triple has returned, otherwise an empty string.
    """
    
    params = { "format": format, "url": url }
    r = requests.get(ANY23URL, params=params)
    if TRIPLES_TOKEN in r.text:
        return r.text
    return ""


def build_graph(data, format=RDFLIB_FORMAT):
    """
    Return a rdflib.Graph for the triples contained in ``data`` and parsed according to the given ``format``
    """
    
    g = Graph()
    if data:
        g.parse(data=data, format=format)
    return g


def web_search_to_triples(query, num=30):
    """
    Returns: a list of n3-serialized RDF triples.
    """
    
    # return object
    triples = []

    # if query is defined... go!
    if query:
        g = Graph()
        for u in google_search(query, num):
            print "##: " + str(u)
            any23_result = any23(u)
            if any23_result:
                g.parse(data=any23_result, format=RDFLIB_FORMAT)
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
