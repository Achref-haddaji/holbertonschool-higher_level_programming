#!/usr/bin/python3
"""
Mylist module
"""


class MyList(list):
	"""
	Mylist class that inherits from list
	"""
	def print_sorted(self):
		"""
		prints a sorted list
		"""
		print(sorted(self))
