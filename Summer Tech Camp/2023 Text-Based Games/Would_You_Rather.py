# Created by Isaiah G.

answer=input("Lets play would you rather!" )
if (answer.lower() == "ok" or answer.lower() == "yes"):
    question1 = input("would you rather eat hamburgers or pizza? ")
    if (question1 == "pizza"):
        question2= input("would you rather be in DC or Marvel? ")
        if (question2 == "DC"):
            print("------------------------------")
            print("|        You're done          |")
            print("------------------------------")
        if (question2 == "Marvel"):
            print("------------------------------")
            print("|  You passed the vibe test   |")
            print("------------------------------")

    elif (question1 == "hamburger"):
        question3=input("would you rather have super strength or be indestructible? ")
        if   (question3=="super strength"):
            question4 = input ("would you rather choose messi or ronaldo? ")
            if (question4 == "ronaldo"):
                print("------------------------------")  
                print("|        Game Over           |")
                print("------------------------------")
            if    (question4 == "messi"):
                print("-------------------------------")
                print("|     congratulations         |")
                print("-------------------------------")
