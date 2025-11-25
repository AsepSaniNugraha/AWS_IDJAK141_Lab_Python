import random

print("Let's play Guess Number")
print("I will choose a number in a certain range, and you try to guess it")
print("First, please determine number range")
minNum=input("Enter your minimum number: ")
maxNum=input("Enter your maximum nunber: ")
print("My number is between {} and {}".format(minNum, maxNum))
number=random.randint(int(minNum),int(maxNum))
# print(number)

isGuess=False

while isGuess==False:
    guessNumber = input("Enter your number: ")
    if int(guessNumber) == number:
        print("Correct")
        isGuess=True
    elif int(guessNumber) > number:
        print("Too high. Try a lower number")
    elif int(guessNumber) < number:
        print("Too low. Try a higher number")