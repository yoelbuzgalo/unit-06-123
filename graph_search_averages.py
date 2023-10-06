"""
Graphs the average search times of linear, binary, and jump searches
across varying array sizes

@author GCCIS Faculty
"""
import array_utils
import searches
import time
import plotter

MIN_ARRAY_SIZE = 100
MAX_ARRAY_SIZE = 10000
PARTITIONS = 25

def average_search_time(search_func,an_array):
    """
    Given a search function (that accepts an array and target), and an array,
    calculates the average search time of targets distributed across that
    array.
    """
    total_time = 0
    count = 0
    array_size = len(an_array)
    for i in range(0,array_size,array_size//PARTITIONS):
        start = time.perf_counter()
        search_func(an_array,an_array[i])
        end = time.perf_counter()
        total_time += end - start
        count += 1

    return total_time / count

def graph_average_search_times(search_func):
    """
    Given a search function (that accepts an array and target), graphs
    the average search times of arrays of increasing sizes.
    """
    step = (MAX_ARRAY_SIZE - MIN_ARRAY_SIZE) // PARTITIONS
    for size in range(MIN_ARRAY_SIZE,MAX_ARRAY_SIZE,step):
        an_array = array_utils.range_array(0,size)
        avg_time = average_search_time(search_func,an_array)
        plotter.add_data_point(avg_time)

def main():
    print("Plotting Linear Search")
    plotter.init("Average Linear Search Time","Array Size",
                 "Average\nSearch\nTime")
    plotter.new_series("Linear Search")
    graph_average_search_times(searches.linear_search)
    print("Close the window to plot binary and jump searches...")
    plotter.plot()

    # Linear and Binary/Jump searches are plotted separately as Binary/Jump
    # searches are best visualized with logarithmic plotting

    plotter.init("Average Binary and Jump Search Times","Array Size",
                 "Average\nSearch\nTime")
    plotter.new_series("Binary Search")
    graph_average_search_times(searches.binary_search)
    plotter.new_series("Jump Search")
    graph_average_search_times(searches.jump_search)
    plotter.plot(log=True)

if __name__ == "__main__":
    main()
        



