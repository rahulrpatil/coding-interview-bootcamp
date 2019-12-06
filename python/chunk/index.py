
# Given an array and chunk size, divide the array into many subarrays
# where each subarray is of length size
# Examples
# chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
# chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
# chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
# chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
# chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]


def chunk(array, size):
    index = 0
    array_size = len(array)
    chunked_output = []
    while (index < array_size):
        chunked_output.append(array[index:(index + size)])
        index = index + size
    return chunked_output



print(chunk([1, 2, 3, 4, 5], 10))
