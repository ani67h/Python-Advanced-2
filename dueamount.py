total = int(input("Enter the total cost of the product or products : "))
paid = int(input("Enter the amount that have already paid : "))
due = 0

def due_amount():
     due = total - paid
     print("You need to pay ",due,"$ later on.")

due_amount()