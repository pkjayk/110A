from flask import Flask
import os
import socket
import gmail_api

app = Flask(__name__)

# Home page
@app.route("/")
def hello():

    return "Ball In Court"

# Authentication page
@app.route("/authenticate")
def render():

	return gmail_api.main()

# 404 - No page exists
@app.errorhandler(404)
def render(error):

	return "Oh no... I found nothing"

if __name__ == "__main__":
	# NOTE: debug mode necessary if you want to see live reloads
    app.run(debug = True, host='0.0.0.0', port=80)

