import sqlite3
import sys

class User:

	# define conn variable

	def checkCredentials(email, password):

		authenticated = False

		conn = sqlite3.connect('LeVinEmployee.db')

		with conn:
        
			cur = conn.cursor()
			try:


				# select username and password match
				cur.execute("SELECT count(*) FROM Employee WHERE Email = '" + email + "' AND Password = '" + password + "'")
	            
				results = cur.fetchall()
	              
				# check the count and make sure = 1, if so, authenticated                      
				if(results[0][0] == 1):
					authenticated = True
				else:
					print("Incorrect email and password combination. Please try again.")
	            
			except:
				print("Unexpected error:" + str(sys.exc_info()[0]))

		if authenticated == True:
			return "Logged in!"
		else:
			return "login failed."