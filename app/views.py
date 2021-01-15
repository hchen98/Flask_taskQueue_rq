from app import app
from flask import render_template, request
from app import r
from app import q

from app.tasks import cound_wrds
from time import strftime


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


@app.route("/add-task", methods=["GET", "POST"])
def add_task():

    # Get a list of jobs in the queue
    jobs = q.jobs
    message = None

    # Only run if a query string is sent in the request
    if request.args:

        # Gets the URL coming in as a query string
        url = request.args.get("url")

        # Send a job to the task queue
        task = q.enqueue(cound_wrds, url)

        # Get a list of jobs in the queue
        jobs = q.jobs

        # Get the queue length
        q_len = len(q)

        message = f"Task queued at {task.enqueued_at.strftime('%a, %d %b %Y %H:%M:%S')}. {q_len} jobs queued"

    return render_template("public/add_task.html", message=message, jobs=jobs)


if __name__ == "__main__":
    app.run()