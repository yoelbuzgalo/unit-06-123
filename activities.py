import arrays
import random

def making_arrays():
    print(arrays.Array(5))
    print(arrays.Array(1, 0))
    print(arrays.Array(10, ""))
    print(arrays.Array(20, False))

def while_fill(an_array):
    index = 0
    while index < len(an_array):
        an_array[index] = index
        index += 1
    return an_array

def for_fill(an_array):
    for index in range(len(an_array)):
        an_array[index] = index
    return an_array

def roll_the_die(sides):
    
    return random.randint(1, sides)

def main():
    random.seed(1)
    # making_arrays()
    # print(while_fill(arrays.Array(10)))
    # print(for_fill(arrays.Array(10)))
    for _ in range(10):
        print(roll_the_die(6))

if __name__ == "__main__":
    main()