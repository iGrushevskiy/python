prices={
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock={
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}


#calculates total price for all items in the stock
for item in prices and stock:
    print item #Prints the name
    print "price: " + str(prices[item]) #Prints the price
    print "stock: " + str(stock[item]) #Prints the stock

#here is the way to calculate your exect shopping list

#your personal shopping list
shopping_list = ["banana", "orange", "apple"]

#function which calculates total price for the items in your list
def compute_bill(food):
    total=0
    for item in food:
        total=total+prices[item]
    return total

print compute_bill(shopping_list)
