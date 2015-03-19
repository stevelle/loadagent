# loadagent
restfuly report server load 

Intended as a means of checking server load in cloud environments (possibly to use in autoscaling or node health checks).  Assumed to work under python 2.7.

to install required python libs:
``pip install -r requirments.txt``

to run: 
``python agent.py``

* query the ``/`` endpoint as a health check endpoint to ensure the agent is running
* query the ``/cpu`` endpoint to get % CPU used since last query
