def multi_table(n):
    for x in range (1,11):
        result = n * x
        print(f"{n} x {x} = {result}")
num = int(input("enter a number: "))
multi_table(num)