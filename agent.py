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
        self.cheat_load = None

    @staticmethod
    def cpu():
        if cheat_load:
            return cheat_load
            
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

from flask import Request

@app.route('/cheating/load', methods=['POST'])
def add_load():
    agent.cheat_load = float(Request.get_data(as_text=True))

@app.route('/cheating/load', methods=['DELETE'])
def remove_load():
    agent.cheat_load = None

if __name__ == '__main__':
    agent.run(True)
