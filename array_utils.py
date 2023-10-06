import random
import arrays

def random_array(size, min_value=0, max_value=None):
    if max_value == None:
        max_value = size
    new_arr = arrays.Array(size)
    for index in range(size):
        new_arr[index] = random.randint(min_value, max_value)
    return new_arr

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    an_array = arrays.Array(len(a_range))
    for index in range(len(an_array)):
        an_array[index] = a_range[index]
    return an_array

def main():
    # random.seed(1)
    # an_array = random_array(10)
    # print(an_array)
    print(range_array(1, 10))

if __name__ == "__main__":
    main()