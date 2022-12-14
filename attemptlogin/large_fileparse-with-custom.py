#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0 # counter for success

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as kfile:

    # loop over the list of lines
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            print("Failed login from:", line.split(' ')[-1].rstrip("\n"))
        elif " -] Authorization failed" in line:
            loginsuccess += 1 # this is counting successful logins
            print("Sucessfull login from:", line.split(' ')[-1].rstrip("\n"))

print("The number of failed log in attempts is", loginfail)

