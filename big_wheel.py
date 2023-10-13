import array_utils

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
    for index in range(len(big_wheel_arr)):
        print(big_wheel_arr[index], end=",")

def main():
    '''
    Main entry of this program
    '''
    big_wheel_array = create_big_wheel()
    print_big_wheel(big_wheel_array) # Testing


if __name__ == "__main__":
    main()