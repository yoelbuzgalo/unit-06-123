import csv
import re

def find_rabbit():
    count = 0 # Keeps track of how many 'Rabbit' word was found
    with open("alice.txt") as file: # Opens the file
        for line in file: # Iterates over every line in file
            line = line.strip().split() # Remove whitespaces and splits words
            for word in line: # Iterates words in a splitted line
                if word == "Rabbit":
                    count += 1 # Adds to the count tracker for every match of word 'Rabbit'
    return count

def find_rabbit_regex ():
    count = 0 # Keeps track of how many 'Rabbit' word was found
    with open("alice.txt") as file: # Opens the file
        for line in file: # Iterates over every line in file
            if re.findall("[A-Za-z]*Rabbit", line) or re.findall("Rabbit[A-Za-z]*", line): # Uses regular expression to find all matched words in a line based on pattern
                count += 1 # Adds to the count tracker for every match of word 'Rabbit'
    return count

def main ():
    print ("Found Rabbit", find_rabbit (), "times.") #should be 29
    print ("Found Rabbit", find_rabbit_regex (), "times.") #should be 45
    

if __name__ == "__main__":
    main ()