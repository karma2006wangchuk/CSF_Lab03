num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

choice = int(input("enter your operator: "))

if choice == 1:
    result = num1 + num2
    print(num1,"+",num2,"=",result)
elif choice == 2:
    result = num1 - num2 
    print(f"{num1} - {num2} = {result}")
elif choice == 3:
    result = num1 * num2 
    print(f"{num1} x {num2} = {result}")
else:
    result = num1/num2
    print(f"{num1} / {num2} = {result}")