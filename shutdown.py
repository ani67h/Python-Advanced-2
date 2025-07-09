import os

shutdown = input("Do you want to shutdown your computer? (Yes or No) : ")

if shutdown == "No":
    exit()
else:
    os.system("Shutdown /s /t 1")    