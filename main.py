import string
import random

print("Welcome to our signup page!")

fname = input("Enter First Name: ")

lname = input("Enter Last Name: ")

email = input("Enter Email: ")
	
#Generating random letters of 4
length = 4
random.choice(string.ascii_lowercase)
a = "".join(random.choice(string.ascii_lowercase) for i in range(length))

#Generate Password
print("Your password is: " + "x" + (fname[0:2]) + (lname[-2:]) + a)

y = input("Are you okay with the password? Enter yes or no: ")

if y == "yes":
  print("Password saved!")
  
elif y == "no":
  print("Password must be more than six characters ")

else:
  print(".................")

s = input(" " + "\n" + "Enter password: ")
t = 7
p = len(s)
	
if (t <= p):
  print("Password Accepted!")
else:
  s = input('Please re-enter password: ' )

#t = 7
#p = len(s)

#if (t <= p):
#  print("Password Accepted!")

#List
user1 = [fname, lname, email]
print("User 1." + "\n" + "Your details are " + str(user1))

print("__________________________________________________")
print("__________________________________________________")
print("__________________________________________________")

print("For User 2")

print("Welcome to our signup page!")

fname1 = input("Enter First Name: ")

lname1 = input("Enter Last Name: ")

email1 = input("Enter Email: ")
	
#Generating random letters of 3
length = 3
random.choice(string.ascii_lowercase)
b = "".join(random.choice(string.ascii_lowercase) for i in range(length))

#Generate Password
print("Your password is: " + "bx" + (fname1[0:2]) + (lname1[-2:]) + b)

y = input("Are you okay with the password? Yes or no?: ")

if y == "yes":
  print("Password saved!")
else:
  print(".................")

s = input("Password must be more than six characters " + "\n" + "Enter password: ")
t = 7
p = len(s)
	
if (t <= p):
  print("Password Accepted!")
else:
  s = input('Please re-enter password: ' )

t = 7
p = len(s)

if (t <= p):
  print("Password Accepted!")
#List
user2 = [fname1, lname1, email1]
print("User 2." + "\n" + "Your details are " + str(user2))