from flask import Flask, session, redirect
from flask_session import Session
import sqlite3
import sys
import re
import os

class User:

	def __init__(self):
		self = self
		self.userDatabasePath = os.path.dirname(os.path.abspath(__file__)) + '/LeVinEmployee.db'
		self.userDatabase = sqlite3.connect(self.userDatabasePath)

	# checks if any fields of the given argument are empty
	def isEmpty(*arg):
		emptyValue = False
		for var in arg:
			clean = str(var).strip()
			if clean == "":
				emptyValue = True
				
		return emptyValue

	def isValidEmail(self, email):
		if len(email) > 4:
			if(re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None):
				return True
			else:
				return False

	def userExists(self, email):

		with self.userDatabase:

			cur = self.userDatabase.cursor()

			try:

				# select username and password match, use placeholders in query to prevent SQL injection
				cur.execute("SELECT count(*) FROM Employee WHERE Email = ?", (email))
	            
				results = cur.fetchall()
	            
			except Exception as e:
				print(e)


	def checkCredentials(self, email=None, password=None):

		if(self.isEmpty(email, password)):
			return False, 'Please enter a username and password.'

		with self.userDatabase:

			cur = self.userDatabase.cursor()

			try:

				# select username and password match, use placeholders in query to prevent SQL injection
				cur.execute("SELECT count(*), FirstName FROM Employee WHERE Email = ? AND Password = ?", (email, password))
	            
				results = cur.fetchall()

				print("results" + str(results))
	              
				# check the count and make sure = 1, if so, authenticated                      
				if(results[0][0] > 0):
					session['loggedIn'] = True
					session['FirstName'] = str(results[0][1])
				else:
					print("Incorrect email and password combination. Please try again.")
	            
			except Exception as e:
				print(e)

		if session.get('loggedIn') == True:
			return True, redirect("/", code=302)
		else:
			return False, 'Invalid credentials, please try again.'

	# registers a user in the database
	def registerUser(self, firstName, lastName, address, city, state, zip, email, password):
		
		if(self.isEmpty(firstName, lastName, address, city, state, zip, email, password)):
			return 'Please enter all fields.'

		if not self.isValidEmail(email):
			return 'Invalid email address!'

		with self.userDatabase:

			cur = self.userDatabase.cursor()

			try:

				# select username and password match, use placeholders in query to prevent SQL injection
				cur.execute("SELECT EmployeeID FROM Employee")

				employeeIdList = list(cur.fetchall())

				highestId = max(employeeIdList)

				print(highestId)

				newId = int(highestId[0]) + 1

				# insert new user information into db
				cur.execute("INSERT INTO Employee (EmployeeID, FirstName, LastName, StreetAddress, City, State, ZipCode, Email, Password) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (newId, firstName, lastName, address, city, state, zip, email, password))

				self.userDatabase.commit()

			except Exception as e:
				print(e)

		return 'User with email ' + email + ' registered!'

	def getUsers(self):

		with self.userDatabase:

			cur = self.userDatabase.cursor()

			try:

				# select username and password match, use placeholders in query to prevent SQL injection
				cur.execute("SELECT EmployeeID, FirstName, LastName, StreetAddress, City, State, ZipCode, Email FROM Employee")

				employeeList = list(cur.fetchall())
				

			except Exception as e:
				print(e)

		return employeeList


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