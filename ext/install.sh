#!/bin/bash -ex

# install dependencies
apt-get update
apt-get -y install build-essential python python-dev python-virtualenv nginx supervisor git

# create a user to run the agent 
adduser --disabled-password --gecos "" loadagent
cd /home/loadagent

# fetch the agent source
git clone https://github.com/stevelle/loadagent.git 
cp loadagent/agent.py .

# create a virtualenv and install dependencies
virtualenv venv
venv/bin/pip install -r loadagent/requirements.txt
chown -R loadagent:loadagent . 

# configure supervisor to run a private gunicorn web server as a service
cp loadagent/ext/supervisor/loadagent.conf /etc/supervisor/conf.d/
mkdir -p /var/log/loadagent
supervisorctl reread
supervisorctl update

# enable reverse-proxy from nginx to the agent
cp loadagent/ext/nginx/loadagent /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/loadagent /etc/nginx/sites-enabled/
service nginx restart

