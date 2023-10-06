import random
import arrays

def random_array(size, min_value=0, max_value=None):
    if max_value == None:
        max_value = size
    new_arr = arrays.Array(size)
    for index in range(size):
        new_arr[index] = random.randint(min_value, max_value)
    return new_arr

def main():
    random.seed(1)
    an_array = random_array(10)
    print(an_array)

if __name__ == "__main__":
    main()