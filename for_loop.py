# # Shopping Discount

# sum = 0
# prices = [500, 1000, 1500, 2000]
# for i in prices:
#     discount = i * 10 / 100
#     f_price = i - discount
#     print("Price after discount ",f_price) 


# #Positive & Negative no's
# p_count=0
# n_count=0
# z_count=0
# numbers = [10, -5, 20, -8, 0, 15, -3]
# for no in numbers:
#     if(no>0):
#         p_count += 1
#     elif(no<0):
#         n_count += 1
#     else:
#         z_count += 1
# print("Count of positive no's ",p_count)
# print("Count of Negative no's ",n_count)
# print("Count of Zero's ",z_count)



# # Customer Purchase total

# p_worth =[250,500,150,700,400]
# total=0
# for price in p_worth:
#     total += price
# print("Total Purchases Of Products ",total)


# Find failed student

# marks = [35, 78, 22, 90, 40, 18, 65]
# for mark in marks:
#     if(mark < 35):
#      print("marks less than 35",mark)


# Electricity Bill

# units = [100, 150, 200, 250, 300]
# charge = 5
# for unit in units:
#     unit *= 5
#     print("electricity charge after ₹5 per unit ", unit)


# # Count Vowels
# count =0

# str = input("Enter a string ")
# for s in str.lower():
#     if s in "aeiou":
#         count += 1    
# print("Total Vowels",count)

#Email Validation

# emails = ["abc@gmail.com", "hello", "user@yahoo.com", "test.com"]
# for email in emails:
#     if "@" in email and "." in email:
#         print(email)


#Inventory Management

# stock = [10, 0, 25, 3, 0, 15, 2]
# for s in stock:
#     if(s<5 or s==0):
#         print("less stock",s)


#Bank Deposits

# total_d_amt=0
# deposit = [1000,2500,3000,1500]
# for d in deposit:
#     total_d_amt += d
# print("deposited amt",total_d_amt)


#Employee Experience atleast 3

# experience = [1, 3, 5, 2, 7, 4, 0]
# for ex in experience:
#     if(ex >=3):
#         print(ex)


#Online Order Tracking

# count=0
# statuses = ["Delivered", "Pending", "Shipped", "Delivered", "Cancelled"]
# for status in statuses:
#     if(status == "Delivered"):
#         count += 1
# print(count)


#Calculate Average Marks

# t_marks=0
# count=0
# marks = [80, 75, 90, 65, 85]
# for mark in marks:
#     t_marks +=mark
#     count +=1
# print("Avg marks ",t_marks/count)


#Mobile Recharge Plans

# plans = [199, 299, 399, 599, 799]
# for plan in plans:
#     if(plan<500):
#         print(plan)


#Count Characters

# str = "KARAN"
# count=0
# for s in str:
#     count +=1
# print(count)


#E-Commerce Sales Report


# sales = [1500, 2500, 1800, 3200, 4000, 1200]

# total = 0
# count = 0

# for sale in sales:
#     total += sale

#     if sale > 2000:
#         count += 1

# print("Total Sales:", total)
# print("Sales above 2000:", count)


# #Student Grade Calculator


# marks = [95, 82, 67, 45, 30, 88, 74]

# for mark in marks:
#     if mark >= 90:
#         grade = "Outstanding"
#     elif mark >= 80:
#         grade = "Excellent"
#     elif mark >= 70:
#         grade = "Good"
#     elif mark >= 35:
#         grade = "Pass"
#     else:
#         grade = "Fail"

#     print(mark, ":", grade)


#ATM Transaction History

# deposit=0
# withdraw=0
# transactions = [-500, 1000, -200, -300, 2000, -100]
# for t in transactions:
#     if(t >0):
#         deposit += t
#     else:
#         withdraw +=t
# print(deposit)
# print(withdraw)


#Hospital Patient Records


# ages = [25, 65, 45, 72, 18, 80, 60]

# count = 0

# for age in ages:
#     if age >= 60:
#         count += 1

# print("Patients aged 60 or above:", count)


#Restaurant Orders


# orders = [250, 400, 150, 600, 350, 200]

# total = 0
# count = 0

# for order in orders:
#     total += order

#     if order > 300:
#         count += 1

# print("Total Bill:", total)
# print("Orders above 300:", count)
