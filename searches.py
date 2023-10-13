import array_utils
import math

def linear_search(an_array, a_target, start=None, end=None):
    '''
    Searches an array using linear algorithm
    '''
    # Initialize Variables
    start_val = start
    end_val = end

    if start is None or start < 0:
        start_val = 0
    if end is None or end > 0:
        end_val = len(an_array)

    for index in range(start_val, end_val):
        if an_array[index] == a_target:
            return an_array[index]
    else:
        return None
    
def binary_search(an_array, target, start=None, end=None):
    '''
    Searches an array using binary search algorithm
    '''
    
    if len(an_array) == 0:
        # Guard clause to check if array is empty
        return None
    
    if start == None:
        # If start is None, set default to 0
        start = 0

    if end == None:
        # If end is None, set default to end index of the array
        end = len(an_array)-1
    
    if start > end: # Not in the array
        return None
    
    midpoint = (start+end) // 2
    if an_array[midpoint] == target:
        return an_array[midpoint]
    elif an_array[midpoint] < target:
        return binary_search(an_array, target, midpoint+1, end)
    else:
        return binary_search(an_array, target, start, midpoint-1)
    
def jump_search(an_array, target, start=0):
    '''
    Searches an array using jump search algorithm
    '''
    search_block = min(len(an_array), start + int(math.sqrt(len(an_array)))) # Gets the search block of a given array
    if search_block <= 0 or search_block is None:
        # Guard clause to check if block is invalid (empty array)
        return None
    search_block -= 1
    if an_array[search_block] == target:
        # the end of the search block matches target, target is found and returned
        return an_array[search_block]
    elif target > an_array[search_block]:
        # If the end value of the block is greater than the target, call itself for next stack with new starting value
        return jump_search(an_array, target, search_block)
    else:
        # Otherwise start linear search of that block
        result = linear_search(an_array, target, start, search_block)
        return result


def main():
    my_arr = array_utils.range_array(1,101)  # 101 is exclusive [1, 100]
    jump_search(my_arr, 100)

if __name__ == "__main__":
    main()