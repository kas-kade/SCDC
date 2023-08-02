# Created by Andres V.

answer = input("Welcome to the trails you will face many challenges up ahead do you wish to continue :")
if(answer=="yes"):
    print("You will have to make a choice in going Left or Right  One is easier than the other ;) :")
    answer=input("The path splits into 2 pick left or right:")
    if(answer=="right"):
        answer = input("you must answer the question correct to proceed.  Is aquaman from atlantis T/F : ")
        if(answer=="true"):
            print("Correct")
            answer=input(" Going down the path you see that theres a person. Would you like to speak to them? : ")
            if(answer=="yes"):
                answer=input("He wants you to answer the question <wasing your time> 2+3+1+9 :")
                if(answer=="15"):
                    print("Correct. YOU WIN Fastest way to win")
                else:
                    print("Wrong he kicked you off a clif. YOU LOSE")
            elif(answer=="no"):
                answer=input("You Made a good choice Possibly. A small branch is falling do you save it.")
                if(answer=="yes"):
                    answer=input("you get to continue since you saved the birds. What is 4 x 1 x 9 x 3")
                    if(answer=="108"):
                        answer=input("Nice one you may continue wanted to get your brain working. What is right left or right :")
                        if(answer=="left"):
                            print("Nah left isnt right. You lose")
                        elif(answer=="right"):
                            print("Nice you understood. YOU WIN the boring way chose to speek to the wizard to have fun ;D")
                    else:
                        print("Wrong the numbers became 3D and fell on you. YOU lOSE")
                elif("no"):
                    print("You let the branch fall and the birds there decided to attack you. YOU LOSE")
        elif(answer=="false"):
             print("Wrong you got struck by lightning in daylight and died")
    elif(answer=="left"):
        answer=input("You decided to take the harder way would u like to get electrocuted :")
        if(answer=="yes"):
            print("You killed yourself YOU LOSE")
        elif(answer=="no"):
            print("the questions will get harder as you go Lets start simple whats 2+2 :")
            if(answer=="4"):
                print("Correct, What is 2 x 2 :")
                if(answer=="4"):
                    print("Correct Your smart. What is 2^3")
                    if(answer=="8"):
                        print("Nice job the wizard is very impressed. What is 2 + 3 x 4")
                        if(answer=="14"):
                            print("Correct. What is Cos(0)")
                            if(answer=="1"):
                                print("WOW impressive you will be asked a couple more questions answer the right and the wisard will take you to the end. What is 6/2(1+2)")
                                if(answer=="9"):
                                    print("Correct. What is 7^2")
                                    answer=input("Congratulations you completed the wizards challenges This path was eaier right :")
                                    if(answer=="yes"):
                                        print("Glad you agree have a nice trip young one. YOU WIN")
                                    elif(answer=="no"):
                                        print("Oh well guess you should work on your math dummy. YOU WIN")
                                else:
                                    print("Wrong the wizard banished you to the underworld. YOU LOSE")
                    else:
                        print("Wrong the wizard tossed dust on you and died. YOU LOSE")
            else:
                print("Wisard was disapointed he Zaped you. YOU LOSE")
elif (answer=="no"):
    print("You lose go away traveler")