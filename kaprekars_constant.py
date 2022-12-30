# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Anderson Wayne Loan 
# Section: 574
# Assignment: 7-4
# Date: 5 10 22
#


digit = input("Enter a four-digit integer:\n")#gets user input
if len(digit) == 3:#if digit is a 3 digit number itll add an apropriate 0 
    digit = int(digit)
    digit = digit * 10
    digit = str(digit)
elif len(digit) == 2:
    digit = int(digit)
    digit = digit * 100
    digit = str(digit)  
elif len(digit) == 1:
    digit = int(digit)
    digit = digit * 1000
    digit = str(digit)
organizer = [] 
organizerM = []
mini = ""
maxi = ""
x = 0
placeHolder = digit
for i in range(4):#puts the digit into a list
    organizer.append(digit[i])
organizer = sorted(organizer)
for i in range(4):#makes the reversed form of the same list
    organizerM.append(organizer[3-i])

if organizer == organizerM:
    mini = int("".join(organizer))#turns the list into int
    maxi = int("".join(organizerM))#turns the list into int
    placeHolder = maxi - mini
    print(maxi,end = " > ")
    print(placeHolder)
    print(f"{digit} reaches 0 via Kaprekar's routine in 1 iterations")
else:
    print(digit,end = " > ")
    while placeHolder != '6174':
        x += 1#count
        placeHolder = int(placeHolder)
        organizer = sorted(organizer)#calcualtes new min number
        for i in range(len(organizer)):#calcualtes new max number
            organizerM[i] = organizer[3-i]
        mini = int("".join(organizer))#turns the list into int
        maxi = int("".join(organizerM))#turns the list into int
        placeHolder = maxi - mini#calcuakltes the new number
        if len(str(placeHolder)) == 3:
            placeHolder *= 10
        placeHolder = str(placeHolder)
        for i in range(4):#moves the number back into the organizer list
            organizer[i] = placeHolder[i]
        if placeHolder[3] == 0:
            placeHolder = str(int(placeHolder / 10))
        if placeHolder != '6174':
            print(placeHolder, end = " > ")
        else:
            print(placeHolder)
    print(f"{digit} reaches 6174 via Kaprekar's routine in {x} iterations")
