marks = float(input("enter your marks:"))

if marks >= 80:
    print("your grade is A")
elif 60 <= marks <= 79:
    print("your grade is B")
elif 40 <= marks <= 59:
    print("your grade is C")
else:
    print("Fail")