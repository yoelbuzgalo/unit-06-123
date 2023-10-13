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
    if index >= len(an_array):
        return
    if an_array[index] % 2 == 1:
        print(an_array[index], end=" ")
        # recurse
    print_odds_rec(an_array, index + 1)

def countdown(n, sum=0):
    sum += n
    if n < 0:
        print("Undefined")
    elif n == 0:
        print(0)
        return 0
    else:
        print(n)
        sum = n + countdown(n-1)
        return sum

def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    fact = n * factorial(n-1)
    return fact

def count_up(n, count=0):
    if n < 0:
        print("Undefined")
    elif count == n:
        print(count)
        return count
    else:
        print(count)
        sum = count + count_up(n, count+1)
        return sum

def binary_search_timer(an_array, target):
    start = time.perf_counter()
    searches.binary_search(an_array, target)
    end = time.perf_counter()
    elapsed = end - start
    return elapsed

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
    # print_odds_rec(an_array)
    # print("Sum:",countdown(5))
    # print(count_up(5))
    print("Binary Search:", binary_search_timer(an_array, 1)) # First Index
    print("Binary Search:", binary_search_timer(an_array, 50)) # Middle Index
    print("Binary Search:", binary_search_timer(an_array, 100)) # Last Index

    print("Linear Search:", linear_search_timer(an_array, 1)) # First Index
    print("Linear Search:", linear_search_timer(an_array, 50)) # Middle Index
    print("Linear Search:", linear_search_timer(an_array, 100)) # Last Index



if __name__ == "__main__":
    main()