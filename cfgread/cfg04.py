#!/usr/bin/env python3

linecount = 0 # counter for lines in file
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    for line in configfile.readline():
        print(line, end="")
        linecount += 1
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print("num lines:",linecount)
