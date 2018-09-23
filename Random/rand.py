import random

randomNumbers = []
userNumbers = []

#Computer filling randomNumbers list with three random different integers
# 0 < number < 10 .
while len(randomNumbers) < 3:
    number = random.randint(1,9)

    #If number is already in randomNumbers it dont put it again.
    #So that there is no duplicates.
    if number in randomNumbers:
        continue
    randomNumbers.append(number)

#Asking the user to enter his guess of the numbers
print("Enter three different positive integers less than 10:")
print()

#Continue prompting the user until he gives valid numbers.
while 1 :
    try:
        number = int(input("Enter first number: "))
        if number >= 10 :
            raise ValueError
        userNumbers.append(number)

        number = int(input("Enter second number: "))
        if number >= 10 or number in userNumbers:
            raise ValueError
        userNumbers.append(number)

        number = int(input("Enter third number: "))
        if number >= 10 or number in userNumbers:
            raise ValueError
        userNumbers.append(number)

        #If the user enter the right numbers printing congratulations message.
        if randomNumbers == userNumbers:
            print("You Win")
            break

        flag = False
        for i in range(3):
            #If the user enters a number in the right place prints "Match".
            if userNumbers[i] == randomNumbers[i]:
                print("Match")
                print()
                flag = True
                break

            #If the user enters a number from the three numbers
            # ,but not in the right place prints "Close".
            elif userNumbers[i] in randomNumbers:
                print("Close")
                print()
                flag = True
                break

        #If the user didn't enter any number of the randomNumbers prints "Nope".
        #If flag still equals False so it is not "Match" nor "Close".
        if flag == False:
            print("Nope")
            print()

        userNumbers.clear()

    except ValueError:
        print("Invalid numbers!!")
        print()
        userNumbers.clear()
