# Created by Rosy C.

# Start Game Here 
answer = input("would you like to do a puzzle")

if(answer == "yes"):
    answer2 = input("what puzzle would you like to do? 1. puzzle one or 2. puzzle two?")
    if answer2 == ("2"):
        print("in this puzzle you have to figure out which words go together")
        answer = input("the letter options you get are SBAKHCOLOLTO")
        if (answer.lower() == "table"):
            print("This answer is wrong you will be logged out")
        if (answer.lower() == "school"):
            print("Yes you have got these right, now you have ended puzzle two")
        if (answer.lower() == "back"):
            print("Yes you have got these right, now you have ended puzzle two")
        if (answer.lower() == "too"):
            print("Yes you have got these right, now you have ended puzzle two")
    if answer2 == ("1"):
        print("in this puzzle you have to figure out which words go together")
        answer = input("the letter options you get are PUFCRSSOORDWAEZZLN")
        if (answer.lower() == "puzzle"):
            print("Yes you have got these right, now you have ended puzzle one")
        if (answer.lower() == "are"):
            print("Yes you have got these right, now you have ended puzzle one")
        if (answer.lower() == "crossword"):
            print("Yes you have got these right, now you have ended puzzle one")
        if (answer.lower() == "perfect"):
            print("This answer is wrong you will be logged out")

elif(answer == "no"):
    answer2 = input("would you like to end the game")
    if(answer2 == "yes"):
        print("ok ending game now...")
    
