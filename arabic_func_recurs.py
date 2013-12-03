def rval(letr):
    """Function translates one digit roman number to one digit arabic"""
    if(letr == "I"):
    	return 1
    elif(letr == "V"):
    	return 5
    elif(letr == "X"):
    	return 10
    elif(letr == "L"):
    	return 50
    elif(letr == "C"):
    	return 100
    elif(letr == "D"):
    	return 500
    elif(letr == "M"):
	return 1000
    else:
    	return "error"
		
		
def arabic(n):
    """Recursive function that translates roman number to arabic"""
    if len(n)==1: #First Base Case 
        return rval(n)
    elif len(n)==2:#Second Base Case
        if rval(n[0])>=rval(n[1]):
	        return (rval(n[0])+rval(n[1]))
        else:
            return (rval(n[0])-rval(n[1]))
    else:
        if rval(n[len(n)-3]) > rval(n[len(n)-2]):
            return arabic(n[len(n)-2:]) + arabic(n[:len(n)-2])
        else:
            return arabic(n[len(n)-1]) + arabic(n[:len(n)-1])
