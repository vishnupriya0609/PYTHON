#VOTING SYSTEM:

age = int(input("Enter your age: "))
if age < 0:
    print("Enter the right age, age must not be negative")
elif age > 100:
    print("You are a senior citizen")
elif age < 8:
    print("You are a child")
elif age < 18:
    print("You are not eligible to vote")
else:
    print("You are eligible to vote")