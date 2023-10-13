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

    results_array = arrays.Array(simulation_run)
    
    

if __name__ == "__main__":
    main()