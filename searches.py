import arrays
import array_utils

def linear_search(an_array, a_target):
    for index in range(len(an_array)):
        if an_array[index] == a_target:
            return index
    else:
        return None

def main():
    my_arr = array_utils.range_array(1,101)
    print(linear_search(my_arr, 1))
    print(linear_search(my_arr, 50))
    print(linear_search(my_arr, 100))
    print(linear_search(my_arr, 101))

if __name__ == "__main__":
    main()