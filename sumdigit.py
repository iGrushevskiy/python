#x=123


def digit_sum(n):
'''function counts sum of the digits in one big number'''
    sum=0
    y=str(n)
    for i in range(len(y)):
        sum=sum+int(y[i])
    return sum
    
print digit_sum(x)

def digit_sum_upd(n):
'''function counts sum of the digits in one big number'''
    sum=0
    y=str(n)
    for i in y:
        sum=sum+i
    return sum
    
print digit_sum_upd(x)
