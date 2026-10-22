# # ATM System

# balance = 500000
# # withdraw= 0
# # deposit = 0

# choice = int(input("1. Check Balance \n 2. Withdraw \n 3. Deposit \n 4. Exit \n Enter ur choice...!"))
# match choice:
#     case 1:
#         print(f"Your Balance is {balance}")
#     case 2:
#        withdraw = int(input("Enter amount to withdraw..."))
#        print(f"Withdrawal Amount {withdraw}\nUpdated balance is",balance-withdraw) 
#     case 3:
#         deposit = int(input("Enter amount to deposit"))
#         print(f"Deposited amount {deposit}\nUpdated balance is",balance-withdraw)
#     case 4:
#         print("U r exited.")
#     case _:
#         print("Invalid Input")
        
        
        
# #Restaurant Menu

# pizza = 210
# burger = 120
# pasta = 270
# sandwich = 80
# choice = int(input(" What whould u like to order \n 1. Pizza -> 210RS \n 2. Burger -> 120Rs \n 3. Pasta -> 270Rs \n 4. Sandwich ->80Rs \n Enter ur choice...!"))
# match choice:
#     case 1:
#         print("U choose Pizza..\nIt's price is ",pizza)
#     case 2:
#         print("U choose Burger..\nIt's price is ",burger)
#     case 3:
#         print("U choose Pasta..\nIt's price is ",pasta)
#     case 4:
#         print("U choose Sandwich..\nIt's price is ",sandwich)
#     case _:
#         print("Invalid input....!") 
      
      
#Delivery Tracking

# choice = int(input("Enter a package status \n 1. Packed \n 2. Dispatched \n 3. Out for Delivery \n 4. Delivered \n Enter ur choice...! "))
# match choice:
#     case 1:
#         print("ur order is packed. \nThe next step is your package will Dispatch soon...")
#     case 2:
#         print("ur order is Dispatched. \nThe next step is your package will Out For Delivery soon...")
#     case 3:
#         print("ur order is Out For Delivery. \nThe next step is your package will Delivered soon...")
#     case 4:
#         print("ur order is Delivered. \nThankyou for ur order...!")
#     case _:
#         print("Invalid input..!")



#Movie Booking System

# choice = int(input("Enter which type of movie u want to watch  \n 1. Action \n 2. Comedy \n 3. Horror \n 4. Romance \n Enter ur choice...! "))
# match choice:
#     case 1:
#         print("Recommended Movies :\n 1. John Wick \n 2. Jawan, Pathaan \n 3. Mission: Impossible \n 4. The Dark Knight")   
#     case 2:
#         print("Recommended Movies :\n 1. 3 Idiots \n 2. Hera Pheri \n 3. Welcome \n 4. Dhamaal \n 5. Chup Chup Ke")
#     case 3:
#         print("Recommended Movies :\n 1. The Conjuring\n 2. Insidious\n 3. Stree\n 4. Bhool Bhulaiyaa\n5.  Tumbbad")
#     case 4:
#         print("Recommended Movies :\n 1. Sita Ramam\n 2.Titanic\n 3.Jab We Met\n 4. Aashiqui 2\n 5. Yeh Jawaani Hai Deewani")
#     case _:
#         print("Genre not available")



#Fitness Center

# choice = int(input("choose a  gym membership for U\n 1. Monthly \n 2. Quarterly \n 3. Half-Yearly \n 4. Yearly \n Enter ur choice...! "))
# match choice:
#     case 1:
#         print("U selected Monthly Membership. It's fees is 1700Rs")
#     case 2:
#         print("U selected Quarterly Membership. It's fees is 4800Rs")
#     case 3:
#         print("U selected Half-Yearly Membership. It's fees is 7100Rs")
#     case 4:
#         print("U selected Yearly Membership. It's fees is 12,500Rs")
#     case _:
#         print("This membership is not available")


# College Admission System
# course = input("Enter course (BCA, BBA, BSc, BCom, BTech): ").upper()

# match course:
#     case "BCA":
#         print("Course Name: Bachelor of Computer Applications")
#         print("Duration: 3 years")

#     case "BBA":
#         print("Course Name: Bachelor of Business Administration")
#         print("Duration: 3 years")

#     case "BSC":
#         print("Course Name: Bachelor of Science")
#         print("Duration: 3 years")

#     case "BCOM":
#         print("Course Name: Bachelor of Commerce")
#         print("Duration: 3 years")

#     case "BTECH":
#         print("Course Name: Bachelor of Technology")
#         print("Duration: 4 years")

#     case _:
#         print("Invalid course selection")
        
        
        
# #Cybersecurity Login System

# role = input("Enter user role (admin, manager, employee, guest): ").lower()

# match role:
#     case "admin":
#         print("Role: Admin")
#         print("Access: Full system access")
#         print("Permissions: Manage users, modify data, and view reports")

#     case "manager":
#         print("Role: Manager")
#         print("Access: Department-level access")
#         print("Permissions: View reports, manage employees, and update records")

#     case "employee":
#         print("Role: Employee")
#         print("Access: Limited access")
#         print("Permissions: View and update assigned tasks")

#     case "guest":
#         print("Role: Guest")
#         print("Access: Read-only access")
#         print("Permissions: View public information only")

#     case _:
#         print("Invalid role")
        
        
        
# #E-commerce Order Status

# status = input("Enter order status (placed, shipped, delivered, cancelled, returned): ").lower()

# match status:
#     case "placed":
#         print("Your order has been placed successfully.")

#     case "shipped":
#         print("Your order has been shipped and is on its way.")

#     case "delivered":
#         print("Your order has been delivered successfully.")

#     case "cancelled":
#         print("Your order has been cancelled.")

#     case "returned":
#         print("Your order has been returned successfully.")

#     case _:
#         print("Invalid order status.")
        
        

# #Hotel Room Booking

# room = input("Enter room type (standard, deluxe, suite, presidential): ").lower()

# match room:
#     case "standard":
#         print("Room Type: Standard")
#         print("Facilities: Bed, TV, Wi-Fi")

#     case "deluxe":
#         print("Room Type: Deluxe")
#         print("Facilities: King-size bed, TV, Wi-Fi, Mini fridge")

#     case "suite":
#         print("Room Type: Suite")
#         print("Facilities: Bedroom, living room, TV, Wi-Fi")

#     case "presidential":
#         print("Room Type: Presidential")
#         print("Facilities: Luxury bedroom, private lounge, premium bathroom, room service")

#     case _:
#         print("Invalid room type.")
        
        
        
# #Library Management System

# operation = input("Enter operation (borrow, return, search, renew): ").lower()

# match operation:
#     case "borrow":
#         print("You have selected the borrow operation.")
#         print("You can borrow a book from the library.")

#     case "return":
#         print("You have selected the return operation.")
#         print("Please return the book to the library.")

#     case "search":
#         print("You have selected the search operation.")
#         print("You can search for books by title or author.")

#     case "renew":
#         print("You have selected the renew operation.")
#         print("You can request an extension for your borrowed book.")

#     case _:
#         print("Invalid operation.")