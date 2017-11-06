from user import User
import unittest

class TestUserFunctions(unittest.TestCase):

	def setUp(self):
		self.user = User()

	def testInvalidEmail(self):
		self.assertFalse(self.user.isValidEmail('invalidemail@email'))
		
	def testValidEmail(self):
		self.assertTrue(self.user.isValidEmail('bob.moore@gmail.com'))

	def testNotIsEmpty(self):
		self.assertFalse(self.user.isEmpty('  j. ', 'j.'))

	def testIsEmpty(self):
		self.assertTrue(self.user.isEmpty('      ', ' '))
