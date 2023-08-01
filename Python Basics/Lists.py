def startMenu():
    print("Welcome player")


# Start Game Here
answer = input("Do you want to go North, east , or west? ")
answer2 = input("Are you sure you want to go " + answer)

if (answer2 == "yes"):
        print("You have gone east")

elif (answer == "yes"):
    startMenu()
