def reverse_array(array):
    first = 0
    last = len(array) - 1
    while first <= last:
        array[first], array[last] = array[last], array[first]
        first += 1
        last -= 1

    return print(array)


reverse_array(['a', 'b', 'c'])
