#!/usr/bin/env python3

# python3 -m pip install netifaces
import netifaces

def getnicconfigs(interface):
    print('\n**************Details of Interface - ' + interface + ' *********************')
    try: # this is a new line, you also need to indent the code below this line by 4 whitespaces
        # print('MAC: ', end='')  # This print statement will always print MAC without an end of line
        # print(netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']) # Prints the IP address
        # print('IP: ', end='')  # This print statement will always print IP without an end of line
        # print(netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']) # Prints the IP address
        print('MAC:', getintmac(interface)) # Prints the MAC address
        print('IP:', getintip(interface)) # Prints the MAC address
    except:
        print('Could not collect adapter information') # Print an error message

def getintmac(interface):
    return netifaces.ifaddresses(interface)[netifaces.AF_LINK][0]['addr']

def getintip(interface):
    # returns IP address for a given interface
    return netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

def main():

    # gather all network interfaces
    interfaces = netifaces.interfaces()

    # print out all of the interfaces names
    print('Installed Interfaces:\n',interfaces) 

    # loop through network interfaces
    for interface in interfaces:
        # print out network configs for each interface
        getnicconfigs(interface)

    # performing IP lookup for primary interface
    for interface in interfaces:
        if interface.startswith('ens'):
            print(f"\nIP address for the primary ethernet interface ({interface}) is {getintip(interface)}")

if __name__ == "__main__":
    main()
