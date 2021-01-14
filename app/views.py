from app import app
from flask import request
from app import r
from app import q
import time


@app.route("/")
def index():
    return "Hello World!"


# task queue
@app.route("/task")
def task():

    if request.args.get("n"):

        job = q.enqueue(background_task, request.args.get("n"))

        return f"Task ({job.id}) added to queue at {job.enqueued_at}"

    return "No value for count provided"


def background_task(n):
    """ Function that returns len(n) and simulates a delay """

    delay = 2

    print("Task running")
    print(f"Simulating a {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)


if __name__ == "__main__":
    app.run()