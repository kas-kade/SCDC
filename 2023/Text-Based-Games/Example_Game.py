import time

health = 3
inventory = []
name = "Bruh"
sword_encounter = 0

def startMenu():
    print("On your path, you encounter a fork in the road with signs.")
    while True:
        time.sleep(2.25)
        currentPath = input("What do you do? ").lower()
        print("")
        time.sleep(1)
        if (currentPath.__contains__("look")):
            time.sleep(1)
            if (currentPath.__contains__("left")):
                print("You can see a forest covered in mist.")
                time.sleep(0.5)
                print("Cheerful voices are calling to you...")
            elif (currentPath.__contains__("right")):
                print("You can see a storm running in")
                time.sleep(0.5)
                print("There is a cave down this path...")
            elif (currentPath.__contains__("around")):
                print("You can see a storm running in from the right.")
                time.sleep(0.5)
                print("Towards the left, you see a misty forest.")
                time.sleep(0.5)
                print("Towards the right, you see a cave opening into the mountains.")
            elif (currentPath.__contains__("down")):
                swordEvent()
            else:
                print("You can't do that..")
        elif (currentPath.__contains__("sign")):
            print("As you take a closer look at the sign, you see faint words.")
            time.sleep(1)
            print("The left sign says The Enchanted Forest.")
            time.sleep(1)
            print("Try not distrupt the peace...")
            time.sleep(1.75)
            print("\nThe right sign says pathway to the Cave of Fjornil.")
            time.sleep(1)
            print("Highly dangerous. Be cautious...\n")
        elif (currentPath.__contains__("left")):
            print("Seeing flora convinces you go to the left path.")
            forestBeginning()
        elif (currentPath.__contains__("right")):
            print("De")
        elif (currentPath.__contains__("back")):
            print("As you start walking backwards")
            time.sleep(1.25)
            print("A shadowy figure jumps up at you.")
            gameOver()
        else:
            print("You can't do that")
        print("")

def forestBeginning():
    time.sleep(1)
    print("You've ")

def swordEvent():
    print("In the corner of your eye, ")

def gameOver():
    time.sleep(3)
    print("——————————————————————————————————\n" +
          "|            GAME OVER            |\n" +
          "——————————————————————————————————")
    exit(0)

if __name__ == '__main__':
    while True:
        print("")
        name = input("What is the name of this brave adventurer: ")
        print("Let's begin, " + name + "...\n")
        time.sleep(2)
        startMenu()
