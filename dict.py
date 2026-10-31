
customer = {"cust_id": 111 , "cust_name":"Karan" , "city": "" , "order_no":45643}
# # print(customer.fromkeys("cust","Kara"))
# # print(customer.clear())
# # print(customer.popitem())
# # print(customer.keys())
# # # print(customer.values())
# print(customer.setdefault("city","pune"))



#Adding elements in Dictionary
# student ={"name": "Karan","age": 21}

# student["city"] = "Pune"
# student["course"] = "Python"

# print(student)

#updating elements in Dictionary
# student = {"name": "Karan","age": 21,"city": "Mumbai"}

# student["city"] = "Pune"
# student.update({"city" :"Goa"})

# print(student)




# 1. Create a dictionary containing your name, age, and city.

# student = {"name": "Karan","age": 21,"city": "Pune"}
# print(student)


# 2. Print only the name from a student dictionary.

# student = {"name": "Karan","age": 21,"city": "Pune"}
# print(student["name"])


# 3. Add an email key to an existing dictionary.

# student={"name":"Karan","age":21}
# student["email"]="karan@gmail.com"
# print(student)


# 4. Update an employee's salary.

# employee = {"name": "Rahul","salary": 25000}
# employee["salary"] = 35000
# print(employee)


# 5. Remove the age key from a dictionary.

# student = {"name": "Karan","age": 21,"city": "Pune"}
# student.pop("age")
# print(student)


# 6. Print all keys and values using a for loop.

# student = {"name": "Karan","age": 21,"city": "Pune"}
# for keys,values in student.items():
#     print(keys,":",values)


# 7. Check whether the key 'course' exists.

# student = {"name": "Karan","age": 21,"course": "Python"}
# if "course" in student:
#     print("Course key exists")
# else:
#     print("Course key does not exist")


# 8. Count the number of key-value pairs.

# student = {"name": "Karan","age": 21,"course": "Python"}
# print("Total keys-value:",len(student))


# 9. Create a nested dictionary for three students.

# student={101:{"name":"Karan","age":20,"marks":80},
#          102:{"name":"Pranjal","age":20,"marks":90},
#          103:{"name":"Vaishnavi","age":20,"marks":95}
#          }
# print(student)
# print(student[101])


# 10. Create a dictionary of numbers and their squares from 1 to 10.

# squares = {}
# for i in range(1, 11):
#     squares[i] = i ** 2
# print(squares)

# squares={}
# i = i ** 2 for i in range(1,11):
#     print(i)


# 11. Print only students who scored more than 75.

# students = {"Karan": 85,"Rahul": 65,"Amit": 90,"Priya": 70,"Sneha": 95}
# for name, marks in students.items():
#     if marks > 75:
#         print(name, ":", marks)
        
        
# 12. Count the frequency of each character in a string using a dictionary.

# text = "pythonn"
# count = {}
# for char in text:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
# print(count)


# 13. Use range() to print dictionary entries by position after converting items to a list.

# student = {"name": "Karan","age": 21,"city": "Pune","course": "Python"}
# items = list(student.items())
# for i in range(len(items)):
#     print(items[i])
    
    
# 14. Use fromkeys() to initialize five subject marks to zero.

# subjects = ["Python", "Java", "SQL", "HTML", "CSS"]
# marks = dict.fromkeys(subjects, 0)
# print(marks)

# 15. Copy a dictionary and demonstrate that changing a top-level value in the copy does not change the original.

# student1 = {"name": "Karan","age": 21,"city": "Pune"}
# student2 = student1.copy()
# student2["age"] = 25
# print("Original Dictionary:", student1)
# print("Copied Dictionary:", student2)
