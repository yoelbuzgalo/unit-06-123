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
    print("Big Wheel Options:")
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
            return stat_big_wheel_rec(result_arr, (current_index+1), (count + 1)) # If number is less or equal to 100, it will add count and call the next stack
        else:
            return stat_big_wheel_rec(result_arr, (current_index+1), count) # If number is not less or equal to 100, it will only proceed to call next stack
    else:
        return count # Otherwise, just return the count if the index has reached to max
    
def avg_big_wheel(result_sum, rounds):
    '''This function returns the average calculation given a result sum and amount of rounds'''
    return (result_sum/rounds) # Calculates the average by dividing result sum with the amount of rounds


def main():
    '''
    Main entry of this program
    '''

    big_wheel_array = create_big_wheel() # Creates a big wheel array, between 5 to 100

    # User input (try block to validate inputs)
    try:
        print() # Makes new line
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

    result_sum = sum_big_wheel_rec(results_array)
    result_stats = stat_big_wheel_rec(results_array)
    average_stat = avg_big_wheel(result_sum, len(results_array))
    
    # Prints desired output in order
    print() # New line
    print_big_wheel(big_wheel_array)
    print("\n") # New line + another line to fix formatting because print big wheel removes \n after its statement print
    print("Results from", len(results_array), "rounds")
    print_big_wheel_rec(results_array)
    print() # New line
    print("Sum:", result_sum)
    print("Rounds less than or equal to $100:", result_stats)
    print("Average:", average_stat)

if __name__ == "__main__":
    main()