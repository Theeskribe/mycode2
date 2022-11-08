#!/usr/bin/env python3

def main():
    # create a list contianing 3 items
    my_list = [ "192.168.0.5", 5060, "UP" ]
    
    # display the first item in the list
    print("The first item in the list (IP): " + my_list[0] )
    
    # display the second item in the list
    print("The second item in the list (port): " + str(my_list[1]) )

    # display the third item in the list
    print("The last item in the list (state): " + my_list[2] )

if __name__ == "__main__":
    main()
