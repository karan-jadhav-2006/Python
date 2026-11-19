#
#1  Write a function calculate_area(length, breadth) that returns the area of a rectangle. Take both values from the user and display the result

def rect(*args):
    area=1
    for n in args:
        area*=n
    print(area)
rect(10,20)

#2.  Write a function simple_interest(principal, rate, time) that returns the simple interest. Call it with positional arguments for two different sets of values.

def simple_interest(*args):
    si = 1
    for num in args:
        si*=num
        si/100
    print(si)

simple_interest(1000,2,3)
      

# 3. Write a function student_info(name, branch, year) that prints a formatted line. Call it using keyword arguments in a different order than defined.

def student_info(**kwargs):
    print(kwargs)
student_info(name="xyz", branch = "comp", year= 2018)


# Write a function create_profile(name, age, city) and call it by mixing one positional argument with two keyword arguments.

def create_profile(**kwargs):
    for i,j in kwargs.items():
     print(i,":",j)

create_profile(name="xyz", age = 20, city="pune")  


# 5. Write a function power(base, exponent=2) that returns base ** exponent. Call it with only the base, with both values positionally, and with the exponent as a keyword argument.
def power(base, exponent=2):
    print(base**exponent)

power(2)
power(2,3)


# 6. Declare a global variable x = 50. Write a function that creates a local variable x = 10 and prints it. Print x outside the function and show that the global value is unchanged.
x=50
def globallocal():
    x=10
    print(x)

print(x)
globallocal()

# 7. Write a program with a global variable counter = 0 and a function increment() that uses the global keyword to increase it by 1. Call it five times and print the final value.
counter = 0
def increment():
    global counter 
    counter +=1

increment()
increment()
increment()
increment()
increment()
print("final", counter)


# 8. Write a program with a global list marks = [70, 80]. Write a function that appends a new mark to it *without* using the global keyword. Print the list and explain in a comment why this works.

marks = [70,80]
def lmark():
    marks.append(10)
lmark()
print(marks)


# 9. Write a function outer(a, b) that defines an inner function inner() returning a + b. Call inner() inside outer() and print the result.
def outer(a,b):
    def inner():
        return a+b
    print("addition ",inner())
outer(10,20)


# Write a function make_counter() with a local variable count = 0 and a nested function increment() that uses nonlocal to increase count and return it. Return increment from make_counter(), store it in a variable, and call it three times to show the count persisting.


