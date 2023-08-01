def partTwo():
    print("As you head into the kitchen you see Mrs. Rabbit preparing a dish that makes you gag.")

def partThree():
     print("Once the cake is finished she redirects you to the living room to eat.")

def partFour():
     print("She directs you to your room which is directly across from hers. Your room is dark and cold. She suggests you get sleep before it gets to late. She goes to her room.")

def partFive():
     answer = input("Do you stay up, sneak out, or go to sleep. ")
     if (answer.lower() == "sleep" or answer.lower() == "go to sleep"):
         print("You wake up in the morning to hear the sound of dishes downstairs.")
         answer = input("Do you, stay or go downstairs. ")
         if (answer.lower() == "stay"):
             print("Mrs. Rabbit calls you down for breakfast. It's your favorite food. She says she got the recipe from your parents. She also says your parents are on their way.")
             answer=input("As you finish break fast your parents arrive. Do you run to them. Politely say bye. Say nothing. ")
             if (answer.lower() == "say nothing" or answer.lower() == "nothing"):
                 print("She is felt disappointed that you said nothing to her as you are leaving/ your parents thank Mrs. Rabbit and leave.")
             elif (answer.lower() == "politely" or answer.lower() == "politely say bye" or answer.lower() == "say bye"):
                 print("She says you've grown so much and is very thankful that she was able to watch you. Your parents say bye and you leave.")
             elif (answer.lower() == "run to them" or answer.lower() == "run" or answer.lower() == "to them" or answer.lower() == "them"):
                print("She is surprised and offended by this but let's you and your parents go. Your parents thank Mrs. Rabbit and leave. As you are driving away. You tell your parents to call the police on Mrs. Rabbit. They call you crazy and ground you.")
         elif (answer.lower() == "go downstairs" or answer.lower() == "go" or answer.lower() == "down" or answer.lower() == "stairs"):
             print("You see Mrs. Rabbit making breakfast. She says good morning. You respond the same. She says breakfast is almost ready and your parents are almost here.")
             answer = input("Do you help her or wait. ")
             if (answer.lower() == "wait"):
                 print("She continues to make breakfast trying to sneakily take out and put away ingredients, you do not know what she is making.")
             elif(answer.lower() == "help her" or "help" or answer.lower() == "her"):
                 print("She says she does not need the help because it is another surprise. She directs you to the table.")
             print("She finishes breakfast and it is your favorite. She says your parents gave her the recipe. You thank her for the food and your parents arrive.")
             answer = input("As your parents arrive. Do you, run towards them, politely say bye, or say nothing. ")
             if (answer.lower() == "say nothing" or answer.lower() == "nothing"):
                 print("She is offended that you said nothing. Your parents thank Mrs. Rabbit and you leave.")
             elif (answer.lower() == "politely say bye" or answer.lower() == "say bye" or answer.lower() == "politely"):
                 print("She is glad that you've grown so much and wishes to see you again. Your parents thank Mrs. Rabbit and you leave.")
             elif (answer.lower() == "run" or answer.lower() == "towards" or answer.lower() == "them" or answer.lower() == "run towards" or answer.lower() == "run towards them" or answer.lower() == "towards them"):
              print("Mrs. Rabbit is confused as to why you decided to run. Your parents thank Mrs. Rabbit for everything and leave. You try to explain to them that Mrs. Rabbit is crazy and they should call the cops. They don't want to deal with you so they just ground you.")

     elif (answer.lower() == "sneak" or answer.lower() == "sneak out" or answer.lower() == "out"):
        print("You sneak out of your room when Mrs. rabbit is asleep. You are now downstairs.")
        answer = input("Where will you go? Kitchen. Backyard. Living Room. Front Door.  ")
        if (answer.lower() == "kitchen" or answer.lower() == "kit"):
            print("You see a window above a sink that is filled with dishes. The door you came from is behind you. ")
        answer = input("What will you do? Wash dishes. Climb out window into backyard. Go back. ")
        if (answer.lower() == "go" or answer.lower() == "back" or answer.lower() == "go back" or answer.lower() == "back go"):
           partFive()
        elif (answer.lower() == "climb" or answer.lower() == "out" or answer.lower() == "window" or answer.lower() == "into" or answer.lower() == "backyard" or answer.lower() == "climb out window" or answer.lower() == "into backyard" or answer.lower() == "climb out window into backyard"):
            print("You trip on a wire. You hear hydraulic pistons pump. The whole yard opens. You fall to your death.")
            exit(0)
        elif (answer.lower() == "wash" or answer.lower() == "dishes"):
            print("You can't seem to find the soap or sponge anywhere. You decide to go back to regroup.")
            partFive()
     elif (answer.lower() == "stay up" or answer.lower() == "stay" or answer.lower() == "up"):
      print("You hear the door downstairs open. You hear something glide smoothly through the air. It sounds like the winds from the ocean. It comes up the stairs. It opens Mrs. Rabbit's door. It watches. It hears. It exits the door and closes the door. It's in your room now. You are hiding beneath the sheets. It listens. It hears your loud heartbeat. It hears your slow deep breathes. It's dark presence is choking you. You throw the sheets off you. Your eyes straining to see something, anything, you know it's there. It feels as if it's towering above you, as if the whole room has gone dark, as if you and it are the only things in existence. It brings you back to reality. You see it with a unidentified object. You feel it happen. A sharp but delightful pain coursing through your body. You die with no regrets.")
      exit(0)
     elif (answer.lower() == "backyard" or answer.lower() == "yard"):
         print("You open the door to the backyard. You hear hydraulic pistons pump. The whole yard opens. You fall to your death.")
         exit(0)
     elif (answer.lower() == "front door" or answer.lower() == "door" or answer.lower() == "front"):
         print("You are now outside.")
         answer = input("You are standing on the porch. There is a road in front of you. Do you go right, left or forward. ")
         if (answer.lower() == "left"):
             print("A dog like creature starts following you across the long road. It's features seem to be changing without warning and randomly. It starts chasing you.")
             answer = input("What do you do? Run. Stay.  ")
             if (answer.lower() == "stay"):
                 print("It jumps at you. You fall face first onto the concrete. You pass out before it starts to eat you. You died with the regret of sneaking out.")
             elif (answer.lower() == "run"):
              print("It is faster than you it was foolish to sneak out. It starts eating you. You pass out after 5 seconds. You died and somewhat painful death.")
         elif (answer.lower() == "right"):
             print("You are walking on a sidewalk. A man wearing all white comes out a alley. You wonder why anyone would wear such clothing.")
             answer.lower("The mans starts chasing you what do you do? Run. Stay.")
             if (answer.lower() == "run"):
                 print("He catches you. You try to see his face. There is none. It beats you to death. You died slowly and painfully. You regret sneaking out.")
             elif (answer.lower() == "stay"):
                 print("He catching you and beats you to death. You ask him why he does it. It dooesn't have a face. Your surroundings go white. It's only you and it until it goes dark. You die a painful slow death.")
                 exit(0)
         elif (answer.lower() == "forward"):
             print("A speeding car slams into you. You go flying. You land on a intersection. Cars seem to appear out of nowhere. You die a painful death.")
             exit(0)
     elif (answer.lower() == "living" or answer.lower() == "room" or answer.lower() == "living room"):
         print("You see the basement door and the door you came from behind you.")
         answer = input("Where will you go. Go back. Basement. ")
         if (answer.lower() == "basement" or answer.lower() == "base" or answer.lower() == "ment"):
             print("You walk down the basement stairs. You tripped a motion sensor. Mrs. Rabbit knows, you don't. Mrs. Rabbit is watching now. You do not think of anything more. Mrs. Rabbit is behind you now. Lurking. She jumps at you. Rips your spine out. Fatality.")
             exit(0)
         elif (answer.lower() == "go" or answer.lower() == "back" or answer.lower() == "go back"):
             partFive()

answer = input("Play Mrs. Rabbit? Yes? No? ")

if (answer == "no"):
    print("Leave")
    exit(0)
elif  (answer == "yes"):
    print("Continue.")

    print("Rules: Obey Mrs. Rabbit's requests, never talk about her husband, do not go in the basement, do not stay awake past 3:00am, be polite and eat all her food." )

    print("Your parents drop you off at Mrs. Rabbit's house. You beg your parents to take you with them to the casino they are going to, they refuse. Your parents say Mrs. Rabbit was your nanny  up until you were 3, you have fond memories of her. The house is very cold, rundown and old.")

    answer = input("You walk inside. How will you greet Mrs. Rabbit? A simple 'Hi, Politely greet her, Say nothing, Run. ")
    if (answer.lower() == "hi"):
        print("She expected a better response; Continue. ")
    elif (answer.lower() == "politely greet her"):
        print("She is warmed by the response; Continue. ")
    elif (answer.lower() == "say nothing"):
      print("She is disappointed that you did not greet her; Continue. ")
    elif (answer.lower() == "run"):
      print("She slowly suffocates you and makes you watch your grave being dug")
      exit(0)

print("As you walk in you see, the basement door, kitchen, the backyard and upstairs hall. ")

answer = input("Where will you go? ")
if (answer.lower() == "basement" or answer.lower() == "door" or answer.lower() == "basement door"):
        
        print("She locks you in the basement and the water leaking begins to flood until you drown, she watches you disppointedly through a hidden window.")
        exit(0)
elif (answer.lower() =="backyard" or answer.lower() == "yard" or answer.lower() == "back"):
        print("She assumed you were trying to run so chased after you and strangled you. ")
        exit(0)
elif (answer.lower() == "upstairs hall" or answer.lower() == "hall" or answer.lower() == "upstairs"):
        print("As you walk up the stairs Mrs. Rabbit redirects you to the kitchen saying supper is almost ready. As you walk back down you see a red liquid dripping from the attic. It's too runny to be blood.")
        partTwo()
elif(answer.lower() == "kitchen"):
        partTwo()

answer = input("Will you help Mrs. Rabbit, criticize her, wait, or watch her? ")
if (answer.lower() == "help" or answer.lower() == "help Mrs. Rabbit"):
    print("She is glad that you are helping.")
elif (answer.lower() == "criticize" or answer.lower() == "critize her" or answer.lower() == "crit"):
    print("She adds a unknown substance to the food and makes you eat it and watches you painfully die.")
    exit(0)
elif (answer.lower() == "wait"):
    print("She finishes making supper no thanks to you.")
elif (answer.lower() == "watch" or answer.lower() == "watch her"):
    print("She felt uncomfortable but finishes supper no thanks to you.")

print("As you are finishing supper, she starts baking a cake, the ingredients are questionable.")
answer = input("Will you help bake, wait in the living room, watch her bake, or criticize her. ")
if (answer.lower() == "help" or answer.lower() == "help bake"):
    print("She appreciates your help but tells you it's a surprise and redirects you to the living room.")
elif (answer.lower() == "wait" or answer.lower() == "living" or answer.lower() == "room" or answer.lower() == "living room"):
    print("She brings the cake to you.")
elif (answer.lower() == "criticize her" or answer.lower() == "criticize" or answer.lower() == "crit"):
    print("She amputates you and bakes them into the cake, she then forces you to eat the cake, you die from food poisioning an hour later.")
    exit(0)
elif (answer.lower() == "watch" or answer.lower() == "watch her bake" or answer.lower() == "bake"):
     print("She felt very uncomfortable but still bakes the cake.") 
     partThree()

answer = input("Now in the living room she shows you the cake, just looking at the cake makes your stomach turn. Do you, eat the cake, say you are not hungry, criticize her baking, or say that you feel unwell. ")
if (answer.lower() == "say that you feel unwell" or answer.lower() == "feel unwell" or answer.lower() == "unwell" or answer.lower() == "feel"):
     print("She understands.")
     partFour()
elif (answer.lower() == "eat" or answer.lower() == "eat the cake" or answer.lower() == "the cake" or answer.lower == "cake"):
     print("She is glad that you ate the cake.")
     answer = input("She now wants to know if you liked the cake or not what will you say? The cake was delicous. The cake was disgusting. ")
     if (answer.lower() == "disgusting" or answer.lower() == "disgusting cake" or answer.lower() == "the cake was digusting" or answer.lower() == "cake disgusting"):
          print("She throws the plate you ate off of at you, you suffer from a concussion and blood loss. You died in your coma.")
          exit(0)
     elif (answer.lower() == "the cake was delicous" or answer.lower() == "delicous" or answer.lower() == "cake delicous" or answer.lower() == "delicous cake"):
          print("She appreciates your enojoyment.")
          partFour()
elif (answer.lower() == "not hungry" or answer.lower() == "say i am not hungry" or answer.lower() == "say you are not hungry"):
     print("She is disappointed but understands.")
     partFour()
elif (answer.lower() == "criticize her baking" or answer.lower() == "crit baking" or answer.lower() == "baking" or answer.lower() == "crit"):
     print("She throws the cake at your face, stunned, she chains your limbs to the floor and starts filling your nose and mouth with cake, she watches as you desperately try to get rid of the cake.")
     exit(0)

partFive()