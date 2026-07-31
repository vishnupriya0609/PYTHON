#PRINT NUMBERS FROM 1 TO 10:
i=1
while i<=10:
    print(i)
    i+=1

#PRINT NUMBERS FROM 1 TO 10 IN REVERSE:
i=10
while i>=1:
    print(i)
    i-=1

#PRINT ALL EVEN  NUMBERS FROM 1 TO 50:
i=0
while i<=50:
    print(i)
    i+=2

#PRINT ALL ODD NUMBERS FROM 1 TO 50:
i=1
while i<=50:
    print(i)
    i+=2

# PRINT MULTIPLES OF 5 FROM 5 TO 100:
i=5
while i<=100:
    print(i)
    i+=5

#MULTIPLICATION TABLE:
n=int(input("enter the number to develop a multiplication table: "))
i=0
while i<=10:
    print(n,"*", i,"=", n*i)
    i+=1

#SUM OF NUMBERS FROM 1 TO N:
n=int(input("enter the number to sum: "))
i=1
sum=0
while i<=n:
    # print("the sum of number is: ",i)
    sum+=i
    i+=1
print("the sum of number is: ",sum)

#PRINT THE PRODUCT OF NUMBERS FROM 1 TO N:
n=int(input("enter the number tp product: "))
i=1
product=1
while i<=n:
    product*=i
    i+=1
print("the product of number is :",product)

#FACTORIAL:
n=int(input("enter the number to calculate factorial: "))
i=1
fact=1
while i<=n:
    fact*=i
    i+=1
print("factorial of the number given: ",fact)

#REVERSE A NUMBER:
n=int(input("enter the number to reverse: "))
while n>0:
    digit=n%10
    print(digit,end=" ")
    n//=10

#SUM OF DIGITS:
n=int(input("enter a number of digits to sum: "))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)
  
#FIND LARGEST DIGIT:
n=int(input("enter the digit to find largest: "))
largest=0
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    n=n//10
print(largest)

#FIND SMALLEST DIGIT:
n=int(input("enter the digit to find smallest: "))
smallest=n%10
while n>0:
    digit=n%10
    if digit<smallest:
        smallest=digit
    n=n//10
print(smallest)

#PALINDROME:
n=int(input("enter a number to calculate palindrome:"))
original=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
if original==reverse:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")

#AMSTRONG NUMBER:
n=int(input("enter a number: "))
i=n
sum=0
while i>0:
    digit=i%10
    sum+=digit**3
    i=i//10
if sum==n:
    print("amstrong number")
else:
    print("not an amstrong number")

#PATTERN:
i=1
while i<=5:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i+=1

#REVERSE PATTERN:
i=5
while i>=1:
    j=1
    while j<=i:
        print("*",end=" ")
        j+=1
    print()
    i-=1

#NUMBER PATTERN:
i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    print()
    i+=1

#REVERSE NUMBER PATTERN:
i=1
while i<=5:
    j=5
    while j>=6-i:
        print(j,end=" ")
        j-=1
    print()
    i+=1

#MENU-DRIVEN CALCULATOR:
while True:
    print("\n MENU ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Calculator Closed")
        break
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if choice == 1:
        print("Result =", a + b)
    elif choice == 2:
        print("Result =", a - b)
    elif choice == 3:
        print("Result =", a * b)
    elif choice == 4:
        if b != 0:
            print("Result =", a / b)
        else:
            print("Division by zero is not possible.")
    else:
        print("Invalid Choice")

#PASSWORD:
password=input("enter a password: ")
while True:
    if password=="python":
        print("access granted")
        break
    else:
        print("access denied")
        break

#ACCEPT NUMBERS TO SUM UNTIL IT IS 0:
sum=0
while True:
    n=int(input("enter a number: "))
    if n==0:
        break
    sum+=n
print(sum)

#FIBONACCI SERIES:
n=int(input("enter a number of terms: "))
a=0
b=1
i=1
while i<=n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    i+=1

#NUMBER GUESSING GAME:
secret = 5
attempts = 0
while True:
    guess = int(input("Guess the number: "))
    attempts += 1
    if guess == secret:
        print("Correct!")
        break
    else:
        print("Wrong!")
print("Attempts:", attempts)