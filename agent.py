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
        self.cheat_load = None
        self.cpu() # initial call required to prepare the system

    def cpu(self):
        if self.cheat_load:
            return self.cheat_load
            
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

from flask import request

@app.route('/cheating/load', methods=['POST'])
def add_load():
    agent.cheat_load = float(request.get_data(as_text=True))
    return ""

@app.route('/cheating/load', methods=['DELETE'])
def remove_load():
    agent.cheat_load = None
    return ""

if __name__ == '__main__':
    agent.run(True)
