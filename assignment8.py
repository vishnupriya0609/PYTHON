#LENGTH OF STRING WITHOUT USING LEN():
a=input("enter the string: ")
count=0
for i in a:
    count+=1
print(count)

#REVERSE STRING USING LOOP:
string=input("enter the string to reverse: ")
reverse=""
for i in string:
    reverse=i+reverse
print(reverse)

#COUNT NO OF WORDS:
string=input("enter the string to count: ")
count=0
for i in string:
    count+=1
print(count)

#FIND LARGEST ELEMENT IN AN ARRAY:
number=[10,20,30,40,50]
largest = number[0]
for num in number:
    if num > largest:
        largest = num
print("Largest element is:", largest)

#FIND SECOND LARGEST NUMBER IN ARRAY:
number=[10, 50, 30, 80, 60]
largest=second=number[0]
for num in number:
    if num>largest:
        second=largest
        largest = num
    elif num > second and num !=largest:
        second=num
print("Second Largest:", second)

#REMOVE DUPLICATE:
number=[10, 20, 10, 30, 20, 40]
unique=[]
for num in number:
    if num not in unique:
        unique.append(num)
print("Array without duplicates:", unique)

#MERGE TWO ARRAYS:
arr1 = [10, 20, 30]
arr2 = [40, 50, 60]
merged = arr1 + arr2
print("Merged Array:", merged)

#FIND COMMON ELEMENT BETWEEN TWO ARRAYS:
arr1=[10, 20, 30, 40]
arr2=[20, 40, 50, 60]
common=[]
for num in arr1:
    if num in arr2:
        common.append(num)
print("Common Elements:", common)

#ANAGRAMS:
str1=input("Enter first string: ")
str2=input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

#SORT ARRAY WITHOUT USING SORT():
num=[10,20,60,80,30]
n=len(num)
for i in range(n):
    for j in range(n-i-1):
        if num[j]>num[j+1]:
            num[j],num[j+1]=num[j+1],num[j]
print(num)