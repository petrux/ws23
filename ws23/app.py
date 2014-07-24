from flask import Flask, render_template, request
from ws23 import web_search_to_triples
from worker import conn
import sys
import os
from rq import Queue
from rq.job import Job
from rq import get_current_job

APP = Flask(__name__)
q = Queue(connection=conn)

@APP.route("/")
def home():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    query = request.args.get("q", default="")
    job_key = request.args.get("job_key", default="")
    triples = []
    
    if job_key:
        job = Job.fetch(job_key, connection=conn)
        if job.is_finished:
            triples = job.result
            job_key = ""
    elif query:
        triples = []
        job = q.enqueue(web_search_to_triples, query)
        job_key = job.key.replace("rq:job:", "")
        print "new job: " + str(job_key)
    else:
        pass
    return render_template("search.html", \
                           actual_query=query,\
                           job_key=job_key,
                           triples=triples)

if __name__ == '__main__':
    APP.run(debug=True,
            host="0.0.0.0",
            port=int(os.environ.get("PORT", "5000")))
