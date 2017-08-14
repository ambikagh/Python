''' Program asks the user to input a number.
Program outputs whether number is even of odd'''

def even_odd():
    while True:
        number = input("Enter a number of your choice: ")
        if not number.isnumeric():
            continue
        number = int(number)
        if number % 2 == 0:
            print("number is even")
        else:
            print("number is odd")
        if input("do you want to continue?").lower()[0] == 'y':
            continue
        else:
            break
    
    
