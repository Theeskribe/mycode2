#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
A script to demonstrate the power of Regular Expression (regex) and
performing HTTP look-ups with the python standard library."""

# standard library imports
import requests    
import re
import urllib.request

def main():
    """Search a website's content"""

    print("Where should we search?")
    url = input("> ")  # collect user input

    print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
    searchFor = input("> ")


    resp = requests.get(url) # Send HTTP GET
    searchMe = resp.text

    # use the re.search() to determine if our website has the pattern we are looking for
    # it works by taking arguments, the first is the regex search pattern, and the second
    # is the string to search within

    if re.search(searchFor, searchMe):
        print("Found a match!")
    else:
        print("No match!")

if __name__ == "__main__":
    main()

