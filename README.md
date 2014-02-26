pypass
======
Password force analyser written in python
-----------------------------------------

How to use it :

	pypass = PassAnalyze(password='password', login='login')
	pypass.is_valid() 			# Will return True if the password is correct
	pypass.errors() 			# Will return the list of errors
