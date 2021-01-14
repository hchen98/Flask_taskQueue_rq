from flask import Flask, request
import redis
from rq import Queue
import time

app = Flask(__name__)

r = redis.Redis()
q = Queue(connection=r)


def background_task(n):
    """ Function that returns len(n) and simulates a delay """

    delay = 2

    print("Task running")
    print(f"Simulating a {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)