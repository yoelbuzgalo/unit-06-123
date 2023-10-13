import array_utils
import arrays
import random

def create_big_wheel():
    '''
    Returns an array with 20 values on the price of Right Big Wheel
    '''
    return array_utils.range_array(5,105, 5)

def print_big_wheel(big_wheel_arr):
    '''
    Prints every element in the passed array
    '''
    print("Big Wheel Values:")
    big_wheel_string = ""
    for index in range(len(big_wheel_arr)):
        print(big_wheel_arr[index], end=",")

def spin_wheel(big_wheel_arr):
    '''
    Selects a random integer in the big_wheel_arr array
    '''
    selected = random.randrange(0, len(big_wheel_arr)) # Chooses a random integer between 0 to the length of big_wheel_arr
    return big_wheel_arr[selected]

def run_round(big_wheel_arr, spin_thres):
    '''
    This function calls spin_wheel, if the number is greater or equal to the number of spin_threshold, it will return that value otherwise return a sum of two values
    '''
    result = spin_wheel(big_wheel_arr)
    if result >= spin_thres:
        return result
    else:
        result_2 = spin_wheel(big_wheel_arr)
        return result + result_2
    
def print_big_wheel_rec(result_arr, current_index=0):
    '''
    This function prints every element in the array recursively
    '''
    if current_index < len(result_arr):
        print(result_arr[current_index])
        print_big_wheel_rec(result_arr, (current_index+1))

def sum_big_wheel_rec(result_arr, current_index=0, arr_sum=0):
    '''
    This recursive function gets the sum of all elements in the array
    '''
    if current_index < len(result_arr):
        return sum_big_wheel_rec(result_arr, (current_index+1), (arr_sum + result_arr[current_index]))
    else:
        return arr_sum
    
def stat_big_wheel_rec(result_arr, current_index=0, count=0):
    '''
    This recursive function counts how many rounds were less than or equal to 100
    '''
    if current_index < len(result_arr):
        if result_arr[current_index] <= 100:
            return stat_big_wheel_rec(result_arr, (current_index+1), (count + 1))
        else:
            return stat_big_wheel_rec(result_arr, (current_index+1), count)
    else:
        return count

def main():
    '''
    Main entry of this program
    '''
    big_wheel_array = create_big_wheel() # Creates a big wheel array, between 5 to 100
    print_big_wheel(big_wheel_array)

    try:
        print() # Clears the previous \n deletion in print_big_wheel function
        spin_threshold = int(input("Enter Spin Threshold To Spin a Second Time (between 5 and 100):"))
        simulation_run = int(input("How Many Rounds to run the simulation (between 1 and 100):"))
        if spin_threshold < 5 or spin_threshold > 100:
            raise ValueError()
        if simulation_run < 1 or simulation_run > 100:
            raise ValueError()
    except ValueError:
        print("Invalid input, please try again")

    results_array = arrays.Array(simulation_run) # Creates results array given the amount of simulation runs it'll need

    # loops simulation to run at a specific amount of times and adds it to the array
    for index in range(simulation_run):
        results_array[index] = run_round(big_wheel_array, spin_threshold)

    # print_big_wheel_rec(results_array)
    result_sum = sum_big_wheel_rec(results_array)
    result_stats = stat_big_wheel_rec(results_array)
    print("Sum:", result_sum)
    print("Stats:", result_stats)

if __name__ == "__main__":
    main()