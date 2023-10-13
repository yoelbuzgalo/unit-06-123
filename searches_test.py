import arrays
import array_utils
import searches

def test_linear_search_empty():
    # setup
    arr = arrays.Array(1,"")
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
    arr = array_utils.range_array(1,5)
    target = 4
    expected = 4

    # invoke
    result = searches.linear_search(arr, target)

    # analysis
    assert result == expected