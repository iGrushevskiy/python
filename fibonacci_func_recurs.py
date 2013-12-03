def fibonacci(n):
	if(n == 1):
		return 0#Base case 1
	elif(n == 2):
		return 1#Base case 2 
	else:
		return fibonacci(n-1)+fibonacci(n-2)
