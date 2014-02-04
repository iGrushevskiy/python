def hotel_cost(nights):
    return nights*140
    
def plane_ride_cost(city):
    if city=='Charlotte':
        return 183
    elif city=='Tampa':
        return 220
    elif city=='Pittsburgh':
        return 222
    elif city=='Los Angeles':
        return 475
    else:
        return 'Wrong city name'

def rental_car_cost(days):
    if days==0:
        return days*40
    elif days>=1 and days<=2:
        return days*40
    elif days>=3 and days<=6:
        return (days*40)-20
    elif days>=7:
        return (days*40)-50
    else:
        return 'you inserted or negative or string value.Please, think by your head!'
        
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money

print trip_cost('Los Angeles',5,600)
