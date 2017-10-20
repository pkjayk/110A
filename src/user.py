from flask import Flask, session, redirect
from flask_session import Session
import sqlite3
import sys


class User:

	# define conn variable

	def checkCredentials(email=None, password=None):

		conn = sqlite3.connect('/app/src/LeVinEmployee.db')

		with conn:

			cur = conn.cursor()

			try:

				# select username and password match, use placeholders in query to prevent SQL injection
				cur.execute("SELECT count(*) FROM Employee WHERE Email = ? AND Password = ?", (email, password))
	            
				results = cur.fetchall()

				print("results" + str(results))
	              
				# check the count and make sure = 1, if so, authenticated                      
				if(results[0][0] == 1):
					session['loggedIn'] = True
				else:
					print("Incorrect email and password combination. Please try again.")
	            
			except Exception as e:
				print(e)

		if session['loggedIn'] == True:
			return redirect("/", code=302)
		else:
			return "Invalid credentials, please try again."

	# registers a user in the database
	def registerUser(firstName, lastName, address, city, state, zip, email, password):
		
		conn = sqlite3.connect('/app/src/LeVinEmployee.db')

		with conn:

			cur = conn.cursor()

			try:

				# select username and password match, use placeholders in query to prevent SQL injection
				cur.execute("SELECT EmployeeID FROM Employee")

				employeeIdList = list(cur.fetchall())

				highestId = max(employeeIdList)

				print(highestId)

				newId = int(highestId[0]) + 1

				# insert new user information into db
				cur.execute("INSERT INTO Employee (EmployeeID, FirstName, LastName, StreetAddress, City, State, ZipCode, Email, Password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (newId, firstName, lastName, address, city, state, zip, email, password))

				conn.commit()

			except Exception as e:
				print(e)

	            
		return "Good"

	def isLoggedIn():
		if session.get('loggedIn') == True:
			return True
		else:
			return False

	def logout():
		session['loggedIn'] = False
		return redirect("/", code=302)