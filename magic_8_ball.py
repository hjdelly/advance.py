import random

response1 = 'It is certain'
response2 = 'It is decidely so'
response3 = 'Without a doubt'
response4 = 'As i see it'
response5 = "Don't count on it"
response6 = 'My source say no'
response7 = 'Outlook not so good'


choice = random.randint(1,7)

name = input("Please, enter your name: ")
input(name + ", What is your desired question for me?")

if choice == 1:
    response = response1
elif choice == 2:
    response = response2
elif choice == 3:
    response = response3
elif choice == 4:
    response = response4
elif choice == 5:
    response = response5
elif choice == 6:
    response = response6
elif choice ==7:
    response = response7

print("Magic 8 ball:", response)