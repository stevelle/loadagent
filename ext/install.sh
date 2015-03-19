#!/bin/bash -ex

# install dependencies
apt-get update
apt-get -y install build-essential python python-dev python-virtualenv nginx supervisor git

# create a user to run the agent 
adduser --disabled-password --gecos "" loadagent
cd /home/loadagent
git clone https://github.com/stevelle/loadagent.git .

# create a virtualenv and install dependencies
virtualenv venv
venv/bin/pip install -r requirements.txt
chown -R loadagent:loadagent .

# configure supervisor to run a private gunicorn web server as a service
cp ext/supervisor/loadagent.conf /etc/supervisor/conf.d/
supervisorctl reread
supervisorctl update

# enable reverse-proxy from nginx to the agent
cp ext/nginx/loadagent /etc/nginx/sites-available/
ln -s /etc/nginx/sites-available/loadagent /etc/nginx/sites-enabled/
service nginx restart

