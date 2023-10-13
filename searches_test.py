import arrays
import array_utils
import searches


# Tests for linear search

def test_linear_search_empty():
    # setup
    arr = arrays.Array(0)
    target = 5
    expected = None

    # invoke
    result = searches.linear_search(arr, target)

    # analysis
    assert result == expected

def test_linear_search_first():
    # setup
    arr = array_utils.range_array(1,5)
    target = 1
    expected = 1

    # invoke
    result = searches.linear_search(arr, target)

    # analysis
    assert result == expected

def test_linear_search_mid():
    # setup
    arr = array_utils.range_array(1,5)
    target = 2
    expected = 2

    # invoke
    result = searches.linear_search(arr, target)

    # analysis
    assert result == expected

def test_linear_search_end():
    # setup
    arr = array_utils.range_array(1,101) # Array is [1,2,3,... 100] (5 is not inclusive)
    target = 3
    expected = 3 # Last number for search in the array is 3, not including 4.

    # invoke
    result = searches.linear_search(arr, target)

    # analysis
    assert result == expected


# Tests for jump search

def test_jump_search_empty():
    # setup
    arr = arrays.Array(0)
    target = 5
    expected = None

    # invoke
    result = searches.jump_search(arr, target)

    # analysis
    assert result == expected

def test_jump_search_first():
    # setup
    arr = array_utils.range_array(1,5)
    target = 1
    expected = 1

    # invoke
    result = searches.jump_search(arr, target)

    # analysis
    assert result == expected

def test_jump_search_mid():
    # setup
    arr = array_utils.range_array(1,5)
    target = 2
    expected = 2

    # invoke
    result = searches.jump_search(arr, target)

    # analysis
    assert result == expected

def test_jump_search_end():
    # setup
    arr = array_utils.range_array(1,5) # Array is [1,2,3,4] (5 is not inclusive)
    target = 4
    expected = 4 # Last number for search in the array is 3, not including 4.

    # invoke
    result = searches.jump_search(arr, target)

    # analysis
    assert result == expected

    # Tests for binary search

def test_binary_search_empty():
    # setup
    arr = arrays.Array(0)
    target = 5
    expected = None

    # invoke
    result = searches.binary_search(arr, target)

    # analysis
    assert result == expected

def test_binary_search_first():
    # setup
    arr = array_utils.range_array(1,5)
    target = 1
    expected = 1

    # invoke
    result = searches.binary_search(arr, target)

    # analysis
    assert result == expected

def test_binary_search_mid():
    # setup
    arr = array_utils.range_array(1,5)
    target = 2
    expected = 2

    # invoke
    result = searches.binary_search(arr, target)

    # analysis
    assert result == expected

def test_binary_search_end():
    # setup
    arr = array_utils.range_array(1,5) # Array is [1,2,3,4] (5 is not inclusive)
    target = 4
    expected = 4 # Last number for search in the array is 3, not including 4.

    # invoke
    result = searches.binary_search(arr, target)

    # analysis
    assert result == expected