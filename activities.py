import arrays
import random
import time
import array_utils
import searches

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

def linear_search_timer(arr, target):
    start = time.perf_counter()
    searches.linear_search(arr, target)
    end = time.perf_counter()
    elapsed = end - start
    return elapsed


def linear_timer():
    arr = array_utils.range_array(1, 10000001)
    print(linear_search_timer(arr,1))
    print(linear_search_timer(arr, 5000000))
    print(linear_search_timer(arr, 10000000))

def print_odds(an_array):
    for index in range(len(an_array)):
        if an_array[index] % 2 == 1:
            print(an_array[index], end=" ")

def print_odds_rec(an_array, index = 0):
    if an_array[index] % 2 == 1:
        print(an_array[index], end=" ")
    # recurse
    print_odds_rec(an_array, index + 1)

def main():
    # random.seed(1)
    # making_arrays()
    # print(while_fill(arrays.Array(10)))
    # print(for_fill(arrays.Array(10)))
    # for _ in range(10):
    #     print(roll_the_die(6))
    # linear_timer()
    an_array = array_utils.range_array(0,100)
    # print_odds(an_array)
    print_odds_rec(an_array)



if __name__ == "__main__":
    main()