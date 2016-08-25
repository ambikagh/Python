'''Program asks for users name and age, displays when
user is going to turn 100 years old'''

import datetime

name = input("Please enter your name: ")
while(not name.isalpha()):
    name = input("Please enter a valid name: ")
    

age = input("Please enter your age: ")
while(True):
    age = int(age)
    if age not in range(0,101):
        age = input("Please enter a valid age: ")
        continue
    break
    
remaining_age = 100 - age

year = year = datetime.datetime.now().year
year = year + remaining_age

count = int(input("how many times you would like to print the message? "))
while count>0:
    print("{} will turn 100 years old in the year {}".format(name, year))
    count -= 1
