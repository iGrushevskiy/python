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


for item in prices and stock:
    print item #Prints the name
    print "price: " + str(prices[item]) #Prints the price
    print "stock: " + str(stock[item]) #Prints the stock
