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


from subprocess import call

@app.route('/cheating/load', methods=['POST'])
def add_load():
    call('stress -c 1 &', shell=True) # FOR DEMO

@app.route('/cheating/load', methods=['DELETE'])
def remove_load():
    call('killall stress', shell=True)

if __name__ == '__main__':
    agent.run(True)
