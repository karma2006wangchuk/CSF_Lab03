def check_num(num):
    if num %2 == 0:
        return "the number is even"
    else:
        return "the number is odd"
x = int(input("enter a number: "))
for i in range(1, x+1):
    result = check_num(i)
print(f"{i} = {result}")