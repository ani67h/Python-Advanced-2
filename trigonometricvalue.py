import math

print("Hey Math enthusiast, how are you all doing? Today, we are going to dive deep in the ocean of Trigonometry! \n")
print("If you want know the angle between the Adjacent and the Hypotenuse Theta (θ); chooce the one that you know (Note : This whole calculations is in terms of a right-angled triangle. So, the length of the Hypotenuse must be larger than other two sides.) : \n 1. OPPOSITE and HYPOTENUSE \n 2. OPPOSITE and ADJACENT \n 3. HYPOTENUSE and ADJACENT \n")

try:
    choice = int(input("Enter your choice here : \n"))

    if choice == 1:
        opp = int(input("Enter the length of Opposite : \n"))
        hyp = int(input("Enter the length of Hypotenuse : \n"))
        result1 = math.asin(opp/hyp)
        print("The angle θ is", result1)
    elif choice == 2:
        opp = int(input("Enter the length of Opposite : \n"))
        adj = int(input("Enter the length of Adjacent : \n"))
        result2 = math.atan(opp/adj)
        print("The angle θ is", result2)
    else:
        hyp = int(input("Enter the length of Hypotenuse : \n"))
        adj = int(input("Enter the length of Adjacent : \n"))
        result3 = math.acos(adj/hyp)
        print("The angle θ is", result3)

except ValueError as err:
    print("Please, enter a integer : ",err)                       