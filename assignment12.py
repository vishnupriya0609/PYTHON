#DICTIONARY:

#CREATE DICT:
student={"name":"vishnu","age":21,"course":"python"}
print(student)

#PRINT NAME:
student={"name":"vishnu","age":21,"course":"python"}
print(student["name"])

#PRINT ALL KEYS:
student={"name":"vishnu","age":21,"course":"python"}
print(student.keys())

#PRINT ALL VALUES:
student={"name":"vishnu","age":21,"course":"python"}
print(student.values())

#PRINT ALL KEY-VALUE PAIRS USING FOR LOOP:
student={"name":"vishnu","age":21,"course":"python"}
for key,value in student.items():
    print(key,":",value)

#ADD NEW KEY"CITY":
student={"name":"vishnu","age":21,"course":"python"}
student["city"]="chennai"
print(student)

#UPDATE AGE TO 22:
student={"name":"vishnu","age":21,"course":"python"}
student["age"]=22
print(student)

#REMOVE COURSE USING POP:
student={"name":"vishnu","age":21,"course":"python"}
student.pop("course")
print(student)

#DELETE CITY USING DEL:
student={"name":"vishnu","age":21,"course":"python","city":"chennai"}
del student["city"]
print(student)

#REMOVE ALL:
student={"name":"vishnu","age":21,"course":"python"}
student.clear()
print(student)

#STUDENTS MARK:

#CREATE DICT FOR 5 STUDENT AND MARKS:
marks={"vishnu":90,"priya":80,"sandhiya":70,"nithiya":60,"pavi":50}
print(marks)

#PRINT ALL STUDENT NAMES:
for name in marks:
    print(name)

#PRINT ALL STUDENT MARKS:
for mark in marks.values():
    print(mark)

#TOTAL MARKS:
total=sum(marks.values())
print(total)

#AVERAGE:
average=total/len(marks)
print(average)

#HIGHEST MARK:
highest=max(marks.values())
for name,mark in marks.items():
    if mark==highest:
        print(name,mark)

#LOWEST MARK:
lowest=min(marks.values())
for name,mark in marks.items():
    if mark==lowest:
        print(name,mark)

#CHECK VISHNU EXISTS:
if "vishnu" in marks:
    print("vishnu exists")
else:
    print("vishnu does not exists")

#COUNT TOTAL NO OF KEY-VALUE PAIRS:
print(len(marks))

#COPY:
new_mark=marks.copy()
print(new_mark)

#ACCEPT 5 STUDENT NAME AND MARK FROM USER:
mark={}
for i in range(5):
    name=input("enter student name: ")
    mark=int(input("enter student mark: "))
    marks[name]=mark
print("student dictionary: ")
print(marks)

#MARK>80:
for name,mark in marks.items():
    if mark>80:
        print(name)

#LESS THAN 50:
for name,mark in marks.items():
    if mark<50:
        print(name)

#CREATE NEW DICT CONTAINING ONLY STUDENTS WHO PASSED (MARK>=50):
passed={}
for name,mark in marks.items():
    if mark>=50:
        passed[name]=mark
print(passed)

#SUM OF ALL EVEN MARKS:
for name,mark in marks.items():
    if mark %2==0:
        print("even marks")
    else:
        print("odd marks")

#MERGE TWO DICT:
d1={"A":10,"B":20}
d2={"C":30,"D":40}
d1.update(d2)
print(d1)

#ASCENDING BY KEYS:
result=dict(sorted(marks.items()))
print(result)

#ASCENDING BY VALUES:
result=dict(sorted(marks.items(),key=lambda x:x[1]))
print(result)

#FREQUENCY:
text=input("enter a string: ")
frequency={}
for i in text:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
print(frequency)

#CHECK KEY EXISTS:
key=input("enter key: ")
if key in marks:
    print("key exists")
else:
    print("key does not exists")