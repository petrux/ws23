ws23
====

[ws23](https://github.com/petrux/ws23/) is a web app that can turn a web search result into a set of RDF triples: its name stands for *Web Search to Triples*, indeed. It has been developed for didactit purposes, just in order to try a minimal mimic of [Sig.ma](http://blog.sindice.com/2009/07/22/sigma-live-views-on-the-web-of-data/).

Just point the browser to the [search page](http://ws23.herokuapp.com/) and type your query: ws23 will gather all the markup triples from the first 30 pages resulting from a [Google](http://www.google.com) search.

The first draft has been developed in something less than 3 hours and this was possible thanks to third-party libraries and services such as:
* [rdflib](https://github.com/RDFLib/rdflib): a Python library for working with RDF
* [google.py](https://github.com/MarioVilas/google): a simple Python google search interface
* [Amy23](https://any23.apache.org/) (Anything to Truples): an Apache project available both as a library and as a web service.
* [RQ](http://python-rq.org/) a simple Python library for queueing jobs and processing them in background (requires [Redis](http://redis.io/) >= 2.6.0.)
