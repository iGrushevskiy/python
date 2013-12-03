def timesTwo(n):
	"""Recursion function that returns a number multiplied by 2"""
	if(n == 0):
		return 0#base case 
	else: 
		return timeTwo(n-1)+2