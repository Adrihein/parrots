#!/usr/bin/env python
# -*- coding: utf-8 -*-

number = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
spl_char = set('`~!@#$%^&*()-_=+{[}]|\;:"\'<,>.?/')


class PassAnalysis(object):

	def __init__(self, password, login='', length=6, number_count=1, uppercase_count=1, spl_char=1, repetition=1):
		""" """
		self.password = password
		self.login = login
		self.length = length
		self.number_count = number_count
		self.uppercase_count = uppercase_count
		self.spl_char = spl_char
		self.repetition = repetition
		self.analyze_error = []


	def has_char(self):
		"""Checks if the password has at least 6 characters."""

		return True if len(self.password) >= self.length else self.analyze_error.append('bad length')


	def _counter(self, char, number):
		"""Default counter function."""

		if number:
			counter = 0
			for i in self.password:
				if i in char:
					counter += 1
			return True if counter and counter >= number else False
		else:
			return True


	def has_number(self):
		"""Checks if the given password has a number."""

		return True if self._counter(char=number, number=self.number_count) else self.analyze_error.append('number')


	def has_uppercase(self):
		"""Checks if the given password has a upper case character."""

		return True if self._counter(char=uppercase, number=self.uppercase_count) else self.analyze_error.append('uppercase')


	def has_spl_char(self):
		"""Checks if the given password has a spl character."""

		return True if self._counter(char=spl_char, number=self.spl_char) else self.analyze_error.append('spl_char')


	def multi_char(self):
		""""Check if tere are the same character."""

		for i in self.password:
			j = self.password.count(i)
			if j-1 > self.repetition:
				return self.analyze_error.append('multi_char')

		return True


	def has_log_in_pass(self):
		"""Check if 60% of the login is in the password"""

		if self.login:
			log = self.login.lower()
			password = self.password.lower()

			length = len(log)
			spliting = (60*length)/100

			if log in password or log[:spliting] in password or log[length-spliting:] in password:
				self.analyze_error.append('has_log_in_pass')
		else:
			return True


	def errors(self):
		"""Show error list."""

		return self.analyze_error


	def is_valid(self):
		"""Checks if the given password is weak or strong."""

		process = [self.has_char, self.has_number, self.has_uppercase,\
					 self.has_spl_char, self.multi_char, self.has_log_in_pass]
		for p in process:
			p()

		return True if not self.analyze_error else False



if __name__ == '__main__':
	login = 'MyLogin'
	password = 'MyPass,_09'

	password = PassAnalyze(password=password, login=login)
	print(password.is_valid())
	print(password.errors())
