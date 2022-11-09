#!/usr/bin/env python3
"""Alta3 Research || Author: RZFeeser@alta3.com"""

# import external libraries
import crayons
import json

# function to push commands
def commandpush(devicecmd): # devicecmd==dict

    for ip in devicecmd.keys(): # looping through the dict
        print (crayons.blue(f'Handshaking. .. ... connecting with {ip}', bold=True)) # fstring
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[ip]:
            print (crayons.yellow(f'Attempting to sending command --> {mycmds}'))
            # we'll learn to write code that sends cmds to device here
    return None

#functgion to reboots devices
def devicereboot(devicelist):
    
    # loop through device list
    for device in devicelist:
        print (crayons.blue(f'Connecting to... {device}', bold=True)) # fstring
        # display reboot warning to user
        print (crayons.red(f'REBOOTING NOW!', bold=True))

    return None

# start our main script
def main():
    """called at runtime"""

    # dict containing IPs mapped to a list of physical interfaces and their state
    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile) # decode the JSON from the file to pythonic data

    # devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    # ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}


    print (crayons.yellow("Welcome to the network device command pusher", bold=True)) # welcome message

    ## get data set
    print (crayons.green("\nData set found\n")) # replace with function call that reads in data from file

    ## run
    commandpush(devicecmd) # call function to push commands to devices

    print (crayons.blue('Initiating reboots on device list:', bold=True))
    ## run reboot function on all devices
    devicereboot(devicecmd.keys())

if __name__ == "__main__":
    # call our main function
    main()
