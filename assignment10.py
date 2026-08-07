#DISLAY MONTHS NAME:
month=int(input("Enter month number (1-12): "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")

#CALCULATOR:
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
op = input("Enter operator (+,-,*,/): ")
match op:
    case "+":
        print("Result:", num1 + num2)
    case "-":
        print("Result:", num1 - num2)
    case "*":
        print("Result:", num1 * num2)
    case "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid Operator")

#VOWEL OR CONSONANT:
string=input("enter a letter: ").lower()
match string:
    case "a"|"e"|"i"|"o"|"u":
        print("vowel")
    case _:
        print("consonant")

#MENU-DRIVEN PROGRAM:
print("1. Add")
print("2. Subtract")
print("3. Multiply")
choice=int(input("Enter your choice: "))
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
match choice:
    case 1:
        print("Addition:", a + b)
    case 2:
        print("Subtraction:", a - b)
    case 3:
        print("Multiplication:", a * b)
    case _:
        print("Invalid Choice")

#GRADE:
grade=input("Enter Grade: ").upper()
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Pass")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")

#TRAFFIC SIGNAL:
color=input("Enter Signal Color: ").lower()
match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")

#DISPLAY WEEKDAY:
day=int(input("Enter day number: "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid Day")

#ATM :
balance=1000
print("1. Balance")
print("2. Deposit")
print("3. Withdraw")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Balance =", balance)
    case 2:
        deposit = int(input("Enter amount: "))
        print("Amount Deposited")
    case 3:
        withdraw = int(input("Enter amount: "))
        print("Amount Withdrawn")
    case _:
        print("Invalid Choice")

#SHAPES:
shape=input("Enter Shape: ").lower()
match shape:
    case "circle":
        print("Round Shape")
    case "square":
        print("4 Equal Sides")
    case "rectangle":
        print("Opposite Sides Equal")
    case "triangle":
        print("3 Sides")
    case _:
        print("Unknown Shape")

#SEASONS:
month=int(input("Enter Month Number: "))
match month:
    case 12 | 1 | 2:
        print("Winter")
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Monsoon")
    case 9 | 10 | 11:
        print("Autumn")
    case _:
        print("Invalid Month")
