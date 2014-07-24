"""
Redis worker
"""

import os
import redis

from rq import Worker, Queue, Connection

listen = ["default"]

url = os.getenv('REDISTOGO_URL', "http://localhost:6379")
conn = redis.from_url(url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
