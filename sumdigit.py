#x=123


def digit_sum(n):
'''function counts sum of the digits in one big number'''
    sum=0
    y=str(n)
    for i in range(len(y)):
        sum=sum+int(y[i])
    return sum
    
print digit_sum(x)
