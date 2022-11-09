#!/usr/bin/env python3

# python3 -m pip install netifaces
import netifaces

# print out all of the interfaces names
print(netifaces.interfaces())

# loop through network interfaces
for i in netifaces.interfaces():
    # print out network configs for each interface
    print('\n**************Details of Interface - ' + i + ' *********************')
    try: # this is a new line, you also need to indent the code below this line by 4 whitespaces
        print('MAC: ', end='')  # This print statement will always print MAC without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']) # Prints the IP address
    except:
        print('Could not collect adapter information') # Print an error message

