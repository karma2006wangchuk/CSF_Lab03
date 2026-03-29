def check_func(num):
    return num % 2 == 0

num = int(input("enter a number: "))
if check_func(num):
    print("the number is even")
else:
    print("the number is odd")