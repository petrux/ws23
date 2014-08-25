ws23
====

[ws23](https://github.com/petrux/ws23/) can turn a web search result into a set of RDF triples: its name stands for *Web Search to Triples*, indeed. It has been developed for didactic purposes, just in order to try a minimal mimic of [Sig.ma](http://blog.sindice.com/2009/07/22/sigma-live-views-on-the-web-of-data/). Just type what you want and `ws23` will gather all the markup triples from the first pages resulting from a [Google](http://www.google.com) search.

The first draft has been developed in something less than 3 hours and this was possible thanks to third-party libraries and services such as:
* [rdflib](https://github.com/RDFLib/rdflib): a Python library for working with RDF
* [google.py](https://github.com/MarioVilas/google): a simple Python google search interface
* [Amy23](https://any23.apache.org/) (Anything to Truples): an Apache project available both as a library and as a web service.
* [RQ](http://python-rq.org/) a simple Python library for queueing jobs and processing them in background (requires [Redis](http://redis.io/) >= 2.6.0.)

Usage
-----

### From the command line (best way) ###
The easies and safes way to use `ws23` is to download the source code and then run the `ws23/ws23.py` script from the command line:

`~$ python ws23/ws23.py "QUERY" [NUMBER OF RESULTS]`

The first argument is the query you want to perform (e.g. "web search to triples", "Ascoli Calcio", ecc) and the second argument is the number of pages you want to consider, so if you specify the value of `10` only the first 10 Google Search results will be parsed and triplified using [Any23](https://any23.apache.org/).

### Self-hosted web application (work in progress) ###

### Publicly available service (coming soon) ###






