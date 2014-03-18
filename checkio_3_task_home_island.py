import string

def checkio(data):
    su=string.uppercase
    sl=string.lowercase
    di=string.digits
    pull=[]
    
    if len(data)>=10:
        for item in data:
            if item in su or sl or di:
                if len(pull)<4:
                    if data.count(item)==
                    pull.append(item)
                    continue
                else:
                    return 'this is good password, %s'%(pull)
            else:
                return 'sign is NOT upper or lower or digit'
    else:
        return 'initial length is less 10'

print checkio('bAse730onE')
print len('bAse730onE')

a='A1213pokl'
a.count('A')

def checkio(data):
    su=string.uppercase
    sl=string.lowercase
    di=string.digits
    pull=[]
    sul=[]
	sll=[]
	dil=[]
	cntr=0
    if len(data)>=10:
        for item in data:
            if item in su or sl or di:
                if item in su and len(sul)<2:
					sul.append(item)
					cntr+=1
					continue
				elif :
				else:
					if item in sl and len(sll)<2:
						sll.append(item)
						cntr+=1
						continue
					else:
						if item in dil and len(dil)<2:
							dil.append(item)
							cntr+=1
							continue
						else:
            else:
                return 'sign is NOT upper or lower or digit'
    else:
        return 'initial length is less 10'

		
