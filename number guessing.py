import random
n = random.randint(1, 50)
guess = int(input("Enter an integer from 1 to 50: "))
while n!= ("guess"):
    print
    if guess < n:
        print ("guess is low")
        guess = int(input("Enter an integer from 1 to 50: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 50: "))
    else:
        print("you guessed it!")
        break
    print
