''' Program asks user for a number and then prints out a list
of all the divisors of that number'''

def list_of_devisors():
    while True:
        num = input("Please enter a number")
        if not num.isnumeric():
            print("invalid input")
            continue
        num = int(num)
        if num == 0:
            print("{} cannot be divided".format(num))
            continue
        divisor_list = []
        for number in range(2, (num//2)+1):
            if num % number == 0:
                divisor_list.append(number)
        print(divisor_list)
        if input("Do you want to continue?").lower()[0] == 'y':
            continue
        else:
            break
        
        
