num1 = int(input("enter fist number: "))
num2 = int(input("enter second number: "))
num3 = int(input("enter third number: "))

if num1 > num2:
    if num1 > num3:
        print(f"the largest number is {num1}")
    else: 
        print(f"the largest number is {num3}")
else:
    if num2 > num3:
        print(f"the largest number is {num2}")
    else:
        print(f"the largest number is {num3}")
        