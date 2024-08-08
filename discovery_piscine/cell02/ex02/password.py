#!/usr/bin/env python3

# Create a program called password.py.
# This program should be executable.
# The program should have a variable containing a password.
# password = "Python is awesome"
# When executed, the program should prompt for a password to be entered.
# If the password is correct, the program should display "ACCESS GRANTED";
# otherwise, it should display "ACCESS DENIED."

password = "Python is awesome"

password_writed = input()
if(password == password_writed):
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")