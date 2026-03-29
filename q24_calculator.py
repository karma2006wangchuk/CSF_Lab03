def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide (a,b):
    return a / b

while True:
    num1 = float(input("enter first number: "))
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")

    choice = int(input("enter any operator: "))
    num2 = float(input("enter second number: "))
    
    if choice == 5:
        print("exixting......")
        break
    
    if choice == 1:
        result = num1 + num2
        print(num1,"+",num2,"=",result)
    elif choice == 2:
        result = num1 - num2
        print(num1,"-",num2,"=",result)
    elif choice == 3:
        result = num1 * num2
        print(num1,"*",num2,"=",result)
    elif choice == 4:
        print(num1,"/",num2,"=",result)
        result = num1 / num2
    else:
        print("invalid operation")