import csv
import re

def find_rabbit():
    count = 0
    with open("alice.txt") as file:
        header = next(file).strip().split()
        for line in file:
            line = line.strip().split()
            for word in line:
                if word == "Rabbit":
                    count += 1
    ####Your code goes here

    return count

def find_rabbit_regex ():
    count = 0
    
    ####Your code goes here

    return count

def main ():
    print ("Found Rabbit", find_rabbit (), "times.") #should be 29
    print ("Found Rabbit", find_rabbit_regex (), "times.") #should be 45
    

if __name__ == "__main__":
    main ()