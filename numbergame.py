import random #importing module
playing = True
number = str(random.randint(10,20)) #random in-built function

print("I will generate a number between 10 to 20, and you have to guess the number one digit at a time")
print("The game wil end when you guess will be correct")
#iterate loop till the condition is true
while playing:
    guess = input("Give me your best guess : \n")
    if number == guess:
        print("Congratulations, you have won the game!")
        print("The number was ",number)
        break
    else:
        print("Your guess isn't correct; try again mate! \n")