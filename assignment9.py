#CREATE LIST:
fruits=["apple","banana","mango","orange"]
print(fruits)

#PRINT FIRST ELEMENT IN LIST:
fruits=["apple","banana","mango","orange"]
print(fruits[0])

#PRINT LAST ELEMENT USING NEGATIVE INDEXING:
fruits=["apple","banana","mango","orange"]
print(fruits[-1])

#LENGTH OF THE LIST:
fruits=["apple","banana","mango","orange"]
print(len(fruits))

#REPLACE BANANA WITH GRAPES:
fruits=["apple","banana","mango","orange"]
index=fruits.index("banana")
fruits[index]="grapes"
print(fruits)

#ADD PINEAPPLE TO END OF THE LIST:
fruits=["apple","banana","mango","orange"]
append=fruits.append("pineapple")
print(fruits)

#REMOVE ORANGE FROM THE LIST:
fruits=["apple","banana","mango","orange"]
remove=fruits.remove("orange")
print(fruits)

#DELETE THIRD ELEMENT USING DEL:
fruits=["apple","banana","mango","orange"]
del[fruits[2]]
print(fruits)

#CLEAR ALL ELEMENTS FROM THE LIST:
fruits=["apple","banana","mango","orange"]
clear=fruits.clear()
print(fruits)

#CREATE LIST FROM 1 TO 10:
num=[1,2,3,4,5,6,7,8,9,10]
print(num)

#PRINT FIRST 5 ELEMENTS USING SLICING:
num=[1,2,3,4,5,6,7,8,9,10]
print(num[0:5])

#PRINT LAST 4 ELEMETS:
num=[1,2,3,4,5,6,7,8,9,10]
print(num[-4:])

#REVERSE THE LIST USING SLICING:
num=[1,2,3,4,5,6,7,8,9,10]
reverse=num[: : -1]
print(reverse)

#LARGEST NUMBER:
num=[1,2,3,4,5,6,7,8,9,10]
largest=max(num)
print(largest)

#SMALLEST NUMBER:
num=[1,2,3,4,5,6,7,8,9,10]
smallest=min(num)
print(smallest)

#SUM OF ALL ELEMENTS:
num=[1,2,3,4,5,6,7,8,9,10]
sum=sum(num)
print(sum)

#AVERAGE OF ALL ELEMENTS:
num=[1,2,3,4,5,6,7,8,9,10]
average=sum(num)/len(num)
print(average)

#COUNT:
num=[1,2,3,4,5,6,7,8,9,10]
print(num.count(5))

#FIND INDEX NUMBER OF 8:
num=[1,2,3,4,5,6,7,8,9,10]
index=num.index(8)
print(index)

#ACCEPT 10 NUMBERS FROM THE USER AND STORE THEM FROM THE LIST:
number=[]
for i in range(10):
    num=int(input(f"enter the number {i+1}: "))
    number.append(num)
print("list of elements: ",number)

#PRINT ALL EVEN NUMBERS FROM THE LIST:
number=[10, 15, 20, 25, 30, 35, 40]
print("Even numbers are: ")
for num in number:
    if num % 2 == 0:
        print(num)

#PRINT ALL ODD NUMBERS FROM THE LIST:
number=[10,20,30,18,17,15,60]
print("odd numbers are: ")
for num in number:
    if num%2!=0:
        print(num)

#CREATE NEW LIST CONTAINING SQUARE OF EVERY NUMBER:
number=[1, 2, 3]
square=[]
for i in number:
    square.append(i ** 2)
print(square)

#REMOVE ALL DUPLICATES:
number=[1, 2, 2, 3, 4, 4, 5]
new_list=[]
for i in number:
    if i not in new_list:
        new_list.append(i)
print(new_list)

#ASCENDING ORDER:
number=[5, 2, 8, 1, 4]
number.sort()
print(number)

#DESCENDING ORDER:
number=[5, 2, 8, 1, 4]
number.sort(reverse=True)
print(number)

#MERGE TWO LIST:
list1=[1, 2, 3]
list2=[4, 5, 6]
list3=list1 + list2
print(list3)

#SECOND LARGEST:
num=[1,2,3,4,5,6,7,8]
num.sort()
print("second largest: ",num[-2])

#ELEMENT EXIST IN LIST:
number=[10, 20, 30, 40]
n=int(input("enter the element to find: "))
if n in number:
    print("Element Found")
else:
    print("Element Not Found")