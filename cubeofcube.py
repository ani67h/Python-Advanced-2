number = int(input("Enter a number : "))
#define function to calculate cube
def cube(number):
    return number*number*number

#define a function which will execute cube function if th user entered number is divisible by 3
def by_three(number):
    if number %3 == 0:
        return cube(number)
    else:
        return print("The number is not divisible by 3")
    
print(by_three(number))    