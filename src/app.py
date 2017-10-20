from flask import Flask
from flask import render_template
import os
import socket
from user import User

app = Flask(__name__)

# Home page
@app.route("/")
def display():

    return render_template('home.html')

# Authentication page
@app.route("/login", methods=['GET','POST'])
def test():
	return User.checkCredentials("bob.moore@gmail.com", "bob")

# 404 - No page exists
@app.errorhandler(404)
def render(error):

	return "Oh no... I found nothing"

if __name__ == "__main__":
	# NOTE: debug mode necessary if you want to see live reloads
    #port = int(os.environ.get('PORT', 4000))
    #app.run(host='0.0.0.0', port=port)
    app.run(debug = True, host='0.0.0.0', port=80)
