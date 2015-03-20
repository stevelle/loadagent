from flask import Flask

import json
import os
import psutil
import socket

app = Flask(__name__)


class Agent():
    def __init__(self, *args, **kwargs):
        app = Flask(__name__)
        self.hostname = socket.gethostname()
        self.cpu() # initial call required to prepare the system

    @staticmethod
    def cpu():
        return psutil.cpu_percent(0)

    def run(self, debug=False):
        app.run(debug=debug)

agent = Agent()

@app.route('/')
def index():
    return json.dumps({'hostname': agent.hostname})

@app.route('/cpu')
def cpu():
    return str(agent.cpu())

if __name__ == '__main__':
    agent.run(True)
