#CREATE TUPLE:
color=("red","blue","green","yellow")
print(color)

#PRINT FIRST ELEMENT:
color=("red","blue","green","yellow")
print(color[0])

#PRINT LAST ELEMENT:
color=("red","blue","green","yellow")
print(color[-1])

#LENGTH:
color=("red","blue","green","yellow")
length=len(color)
print(length)

#PRINT THIRD ELEMENT:
color=("red","blue","green","yellow")
print(color[2])

#PRINT ALL ELEMENTS USING FOR LOOP:
color=("red","blue","green","yellow")
for i in color:
    print(i)

#BLUE EXISTS:
color=("red","blue","green","yellow")
if "blue" in color:
    print("blue exists")
else:
    print("not exists")

#PRINT 1 TO 3 USING SLICING:
color=("red","blue","green","yellow")
print(color[1:])

#CONACTENATE:
t1=(1,2,3)
t2=(4,5,6)
concate=t1+t2
print(concate)

#REPEAT 3 TIMES:
t=("python")
for i in range(3):
    print(t)

#CRAETE NUMBERS FROM 1 TO 10:
num=(1,2,3,4,5,6,7,8,9,10)
print(num)

#MAX ELEMENT:
num=(1,2,3,4,5,6,7,8,9,10)
maximum=max(num)
print(maximum)

#MIN ELEMENT:
num=(1,2,3,4,5,6,7,8,9,10)
minimum=min(num)
print(minimum)

#SUM:
num=(1,2,3,4,5,6,7,8,9,10)
sum=sum(num)
print(sum)

#AVERAGE:
num=(1,2,3,4,5,6,7,8,9,10)
average=sum(num)/len(num)
print(average)

#COUNT:
t=(1,5,2,5,6,5)
print(t.count(5))

#INDEX OF 8:
num=(1,2,3,4,5,6,7,8,9,10)
index=num.index(8)
print(index)

#REVERSE TUPLE USING SLICING:
num=(1,2,3,4,5)
reverse=num[: : -1]
print(reverse)

#CONVERT TUPLE TO LIST:
num=(1,2,3,4,5)
list=list(num)
print("tuple: ",num)
print("list: ",list)

#CONVERT LIST TO TUPLE:
num=[1,2,3,4,5]
tuple=tuple(num)
print("list:",num)
print("tuple:",tuple)

#ASCENDING:
t=(5,6,2,3,4,1)
sort=tuple(sorted(t))
print(sort)

#DESCENDING:
t=(2,3,5,1,4,6)
sort=tuple(sorted(t,reverse=True))
print(sort)

#MERGE:
t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)

#SECOND LARGEST:
t=(40,20,30,60,50)
t=tuple(sorted(t))
print("second largest: ",t[-2])

#ELEMENT EXISTS:
t=(10,20,30)
num=int(input("enter the number:"))
if num in t:
    print("element exists")
else:
    print("element not exists")