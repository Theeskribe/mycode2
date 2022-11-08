#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - simple list"""

def main():
    # create a list called list1
    list1 = ["Fox","Fly","Ant"]
    list2 = ["Bee","Cod","Cat"]
    list3 = ["Dog","Yak","Cow"]
    list4 = ["Hen","Koi","Hog"]
    list5 = ["Jay","Kit"]
    

    # extend list1 by list2 
    list1.extend(list2)

    # append list3 to list1
    list1.append(list3)

    # extend list1 by list4 
    list1.extend(list4)

    # append list5 to list1
    list1.append(list5)

    for all_animals in list1:
        for animal in all_animals:
            print(animal, end=" ")

    # display the list the 1st of the IP addresses
    print(list1)

main()

