numbers = [3,5,7,9,11,13,15]

print("list",numbers)
target = int(input("enter any number: "))
print(f"searching for: {target}")

for num in numbers:
    if num == target:
        print("number found")
    else:
        while num != target:
            print("target not found")
            break 
