from flask import Flask, session, redirect
from flask_session import Session
import sqlite3
import sys


class User:

	def __init__(self):
		self = self
		self.userDatabasePath = '/app/src/LeVinEmployee.db'
		self.userDatabase = sqlite3.connect(self.userDatabasePath)

	def isEmpty(*arg):
		emptyValue = False
		for var in arg:
			if var == "":
				emptyValue = True
				
		if(emptyValue):
			return True
			#raise ValueError('All fields must be entered.')

	def checkCredentials(self, email=None, password=None):

		if(self.isEmpty(email, password)):
			return 'Please enter a username and password.'

		with self.userDatabase:

			cur = self.userDatabase.cursor()

			try:

				# select username and password match, use placeholders in query to prevent SQL injection
				cur.execute("SELECT count(*), FirstName FROM Employee WHERE Email = ? AND Password = ?", (email, password))
	            
				results = cur.fetchall()

				print("results" + str(results))
	              
				# check the count and make sure = 1, if so, authenticated                      
				if(results[0][0] == 1):
					session['loggedIn'] = True
					session['FirstName'] = str(results[0][1])
				else:
					print("Incorrect email and password combination. Please try again.")
	            
			except Exception as e:
				print(e)

		if session['loggedIn'] == True:
			return redirect("/", code=302)
		else:
			return "Invalid credentials, please try again."

	# registers a user in the database
	def registerUser(self, firstName, lastName, address, city, state, zip, email, password):
		
		if(self.isEmpty(firstName, lastName, address, city, state, zip, email, password)):
			return 'Please enter all fields.'
			
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

	            
		return "User Registered!"

	def isLoggedIn():
		if session.get('loggedIn') == True:
			return True
		else:
			return False

	def getFirstName():
		return session.get('FirstName')

	def logout():
		session['loggedIn'] = False
		return redirect("/", code=302)