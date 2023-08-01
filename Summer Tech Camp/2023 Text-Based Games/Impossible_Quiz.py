# Created by Michael R.

print('Welcome to the impossible quiz?')
answer=input('Are you ready to play? (yes/no) :')
score=0
total_questions=6
 
if answer.lower()=='yes':
    answer=input('Question 1: How many holes are in a polo?   (options) 1.One  2.Two  3.Three  4.Four')
    if answer.lower()=='4':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Can a match box?   (options) 1.Yes  2.No  3.No but a tin can  4.Yes one beat mike tyson ')
    if answer =='3' or answer.lower()=="no but a tin can":
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: sdrawkcab noitseuq siht rewsna?    (options) 1.K.O  2.What? 3.I dont understand 4.Tennis elbow')
    if answer.lower()=='1':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 4: The answer is really big?    (options) 1. An Elephant 2. Infinity 3. Really big 4. answer')
    if answer.lower()=='1':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 5: What sound does a bell make?     (options)  1. Whoop 2. ftaang 3. froon 4. flip-bang-blop-blip-woof-ooo-wop-scap-bloop')
    if answer.lower()=='2':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 6: What was the answer to answer 2?     (options)   1.That one  2.This One  3. That one  4.That one ')
    if answer.lower()=='3':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')


print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
