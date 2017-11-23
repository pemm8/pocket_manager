import requests, json, os, json
import os
import datetime as dt
from flask_script import Manager
from flask import Flask

app = Flask(__name__)

req_tok_url = 'https://getpocket.com/v3/oauth/request'
cons_key = '72615-19476ccd3c099ffd425ba614'
auth_url = 'https://getpocket.com/v3/oauth/authorize'
get_url = 'https://getpocket.com/v3/get'
access_tok = '9e731d11-b5b5-25b3-5487-8053de'

app.config.from_object(__name__)

manager = Manager(app)

@manager.command
def test_command():
	print "Test Success"

@manager.command
def authenticate():
	# request token
	settings = {
	    "Content-Type": "application/json; charset=UTF-8",
	    "X-Accept": "application/json",
	    "consumer_key": cons_key,
	    "redirect_uri": "http://www.google.com/"
	}
	r = requests.post(req_tok_url, settings)

	code = str(re.split('=',r.text)[1])
	print("%s: %s") % (r, code)
	url = "https://getpocket.com/auth/authorize?request_token=%s&redirect_uri=%s" % (code, "http://www.google.com/")
	return url

@manager.command
def authorise():
	settings = {
	    "Content-Type": "application/json; charset=UTF-8",
	    "X-Accept": "application/json",
	    "consumer_key": cons_key,
	    "code": code
	}
	r = requests.post(auth_url, settings)
	print("%s") % (r)

@manager.command
def get_all():
	settings = {
	    'Content-Type': 'application/json',
	    'consumer_key': cons_key,
	    'access_token': access_tok,
	    'detailType': 'simple'
	}
	r = requests.post(get_url, settings)
	print(r.status_code)
	with open('pocket.json', 'w') as jsonfile:
	    json.dump(r.json(), jsonfile)


if __name__ == "__main__":
	manager.run()