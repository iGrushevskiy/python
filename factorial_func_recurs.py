def factorial(n):
    if(n == 0):
    """Recursion function that returns the factorial of the number"""
		return 1#What was our base case? 
	else:
		return n*factorial(n-1)
