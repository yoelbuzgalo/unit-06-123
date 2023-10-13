import arrays
import array_utils

def linear_search(an_array, a_target):
    for index in range(len(an_array)):
        if an_array[index] == a_target:
            return an_array[index]
    else:
        return None
    
def binary_search(an_array, target, start=None, end=None):
    if start == None:
        start = 0
        end = len(an_array) - 1

    elif start > end: # Not in the array
        return None
    
    midpoint = (start+end) // 2
    if an_array[midpoint] == target:
        return an_array[midpoint]
    elif an_array[midpoint] < target:
        binary_search(an_array, target, midpoint+1, end)
    else:
        binary_search(an_array, target, start, midpoint-1)
    


def main():
    my_arr = array_utils.range_array(1,101)
    # print(linear_search(my_arr, 1))
    # print(linear_search(my_arr, 50))
    # print(linear_search(my_arr, 100))
    # print(linear_search(my_arr, 101))
    print(binary_search(my_arr, 50))

if __name__ == "__main__":
    main()