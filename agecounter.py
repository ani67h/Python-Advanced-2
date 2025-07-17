import os
age = 0
try:
    age = int(input("Please, enter your age : "))
    if age % 2 == 0:
        print("Congratulations, your age is a odd number. You enter a random odd number to see what happens.")
    else:
        os.system("Shutdown /s /t 1") 
except ValueError as ex:
    print("Please, enter a integer : ",ex)           