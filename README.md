pypass
======
Password force analyser written in python
-----------------------------------------

How to use it :

	from pypass import PassAnalysis

	pypass = PassAnalysis(password='password', login='login')
	pypass.is_valid() 			# Will return True if the password is correct
	pypass.errors() 			# Will return the list of errors
