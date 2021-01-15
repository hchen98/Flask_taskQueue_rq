# Flask_taskQueue_rq
A simple Flask task queue through Redis Queue (RQ).

---


### Get start

* Start the Redis 

    ```
    redis-server
    ```
    * The output should look like
    ```
                        _._                                                  
            _.-``__ ''-._                                             
        _.-``    `.  `_.  ''-._           Redis 6.0.10 (00000000/0) 64 bit
    .-`` .-```.  ```\/    _.,_ ''-._                                   
    (    '      ,       .-`  | `,    )     Running in standalone mode
    |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
    |    `-._   `._    /     _.-'    |     PID: 275838
    `-._    `-._  `-./  _.-'    _.-'                                   
    |`-._`-._    `-.__.-'    _.-'_.-'|                                  
    |    `-._`-._        _.-'_.-'    |           http://redis.io        
    `-._    `-._`-.__.-'_.-'    _.-'                                   
    |`-._`-._    `-.__.-'    _.-'_.-'|                                  
    |    `-._`-._        _.-'_.-'    |                                  
    `-._    `-._`-.__.-'_.-'    _.-'                                   
        `-._    `-.__.-'    _.-'                                       
            `-._        _.-'                                           
                `-.__.-'                                               

    275838:M 14 Jan 2021 17:23:05.548 # Server initialized
    275838:M 14 Jan 2021 17:23:05.548 # WARNING overcommit_memory is set to 0! Background save may fail under low memory condition. To fix this issue add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the command 'sysctl vm.overcommit_memory=1' for this to take effect.
    275838:M 14 Jan 2021 17:23:05.549 * Loading RDB produced by version 6.0.9
    275838:M 14 Jan 2021 17:23:05.549 * RDB age 153330 seconds
    275838:M 14 Jan 2021 17:23:05.549 * RDB memory usage when created 0.79 Mb
    275838:M 14 Jan 2021 17:23:05.549 * DB loaded from disk: 0.000 seconds
    275838:M 14 Jan 2021 17:23:05.549 * Ready to accept connections
    ```

* Run the Redis Queue

    ```
    cd <directory where run.py is located>
    rq worker
    ```

    * The output should look like
    ```
    17:23:23 Worker rq:worker:10eae75d732146d887b3b286275cc302: started, version 1.7.0
    17:23:23 Subscribing to channel rq:pubsub:10eae75d732146d887b3b286275cc302
    17:23:23 *** Listening on default...
    ```

* Setup the project

    ```
    # activate the environment
    source taskqueue_rq/bin/activate

    # install the libraries
    pip install -r requirements.txt
    ```


* Run the Flask
    ```
    export FLASK_APP=run.py
    export FLASK_ENV=development
    flask run
    ```

* Pass the para to the URL http://127.0.0.1:5000/task?n=2

<br>

### Result

```
17:29:58 default: app.views.background_task('2') (29754d5e-69f4-4f91-a1b9-e85ba659d431)
ENV is set to: production
Task running
Simulating a 2 second delay
1
Task complete
17:30:01 default: Job OK (29754d5e-69f4-4f91-a1b9-e85ba659d431)
17:30:01 Result is kept for 500 seconds
```

<br>

### Reference
1. <a href="https://python-rq.org/">Redis Queue offical site</a>
2. <a href="https://pythonise.com/series/learning-flask/flask-rq-task-queue">Code Reference</a>


