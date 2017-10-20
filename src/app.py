from flask import Flask, render_template, request, make_response, jsonify, session
from flask_session import Session
import memcache
import os
import socket
from user import User
import redis

app = Flask(__name__)

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

# Home page - Will display either login screen or dashboard
@app.route("/")
def displayHomepage():

	if not User.isLoggedIn():
		response = render_template('login.html')
	else:
		response = render_template('dashboard.html')

	return response

# Authentication page
@app.route("/login", methods=['POST'])
def checkCredentials():

	return User.checkCredentials(email = request.form['email'], password = request.form['password'])

# Authentication page
@app.route("/register", methods=['GET', 'POST'])
def renderRegisterPage():

	if request.method == "GET":
		return render_template('register.html')
	if request.method == "POST":
		return User.registerUser(request.form['firstName'], request.form['lastName'], request.form['address'], request.form['city'], request.form['state'], request.form['zip'], request.form['email'], request.form['password'])

@app.route("/logout")
def logoutUser():
	return User.logout()

# 404 - No page exists
@app.errorhandler(404)
def render(error):

	return "Oh no... I found nothing"

if __name__ == "__main__":
	# NOTE: debug mode necessary if you want to see live reloads
    #port = int(os.environ.get('PORT', 4000))
    #app.run(host='0.0.0.0', port=port)
    app.run(debug = True, host='0.0.0.0', port=80)
