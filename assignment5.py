#CHECK NUMBER IS POSITUVE OR NEGATIVE:
n=int(input("enter the number: "))
result="positive" if n>0 else "negative"
print(result)

#GREATER OF TWO NUMBERS:
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
result="greater is greater than b" if a>b else "b is greater than a"
print(result)

#CHECK NUMBER IS EVEN OR ODD:
n=int(input("enter a number: "))
result="even" if 2%n==0 else "odd"
print(result)

#CHECH PASS OR FAIL:
mark=int(input("enter the mark: "))
result="pass" if mark>=35 else "fail"
print(result)

#VOTING ELIGIBILITY:
age=int(input("enter your age: "))
result="eligible to vote" if age>=18 else "not eligible to vote"
print(result)

#FIDING SMALLEST OF TWO N UMBERS:
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
result="a is smaller than b"if a<b else "b is smaller than a"
print(result)

#DISPLAY ADULT OR MINOR BASED ON AGE:
age=int(input("enter your age: "))
result="adult" if age>=18 else "minor"
print(result)

#CHECK UPPERCASE OR LOWERCASE:
a=input("enter a character: ")
result="uppercase" if a.isupper() else "lowercase"
print(result)

#CHECK LEAP YEAR OR NOT:
year=int(input("enter a year: "))
result="leap year" if year%4==0 else "not a leap year"
print(result)

#ASSIGN GRADES USING NESTED TERNARY OPERATOR:
mark=int(input("enter your mark: "))
result="A" if mark>=90 else "B" if mark>=80 else "C" if mark>=70 else "D" if mark>=60 else "E" if mark>=50 else "F"
print(result)