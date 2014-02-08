from random import randrange

#generating random number
random_number = randrange(1, 10)
print random_number
count = 0
# Start your game!
while count <3:
    guess=int(raw_input("Enter a guess:"))    
    if guess==random_number:
        print "You win!"
        break
    else:
        if count<2:
            print "Try again..."
        count+=1
else:
    print "You Lose."
