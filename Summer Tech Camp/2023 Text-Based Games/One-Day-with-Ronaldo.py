# Created by Nathan C.

def theend():
      print("-------------------------------------------------------------------")
      print("                              THE END                              ")
      print("-------------------------------------------------------------------")
      exit(0)

answer = input("Visit Ronaldo's house?")
    
if (answer == "yes"):
  print("He is happy")

elif (answer == "no"):
   print("You went home")

else:
   print("You went anyway")

reply = input ("Do you train with him? ")

if (reply == "yes"):
   print("He broke your leg")

elif (reply == "no") :
   print(" You stayed with Georgina")

else: 
   print("Ronaldo thinks you are indecisive and kicks you out")
   print ("")

reply = input ("It is nightime, where do you sleep?       1. On the floor    2. In Ronaldo's bed    3. In the Guest room" )
if (reply == "2"):
   print("A robber broke in but you were safe")
else:
   print ("A robber broke in and you died!")
   theend()

answer = input ("The robber tries to enter the room, what do you do?     1. Call 911  2. Fight the robber  3. Hide")
if (answer == "2"):
   print("You and Ronaldo fought off the intruder and survived!")
elif (answer == "1"):
   print("Ronaldo died but the police came to save you")
   theend()
else:
   print("Ronaldo bled out and the robber found you.")
   theend()
reply = input("A football team offers you a contract do you accept?")
if (reply == "yes"):
   print ("Barcelona writes your contract on a napkin and Ronaldo is proud")
else:
   print ("Ronaldo gets really upset by your laziness  ╬ ಠิ益ಠิ)")

   print ("")

print ("Congratulations! You survived part one of the Ronaldo game; I hope you enjoyed this at least a little.")
theend()
print ("")