"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""



def binary_search(input_array, value):
    """Your code goes here."""
    l = 0
    r = len(input_array)

    while (l <= r):
        m = int(l + (r - l) / 2)
        # print("left: {0:5}, right: {1:5}, middle: {2:5}".format(l, r, m))
        if (input_array[m] == value):
            # print("found")
            return m

        if (input_array[m] < value):
            l = m + 1
        else:
            r = m - 1

    return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
