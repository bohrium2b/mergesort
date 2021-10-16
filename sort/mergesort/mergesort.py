"""
This program defines a function to implement merge sort.
"""
from typing import List


def sort(array: List[int]) -> List[int]:
    """
    This function sorts a list of integers using merge sort.
    Arguments:
    Array - list of integers
    Output:
    Sorted array

    Usage:
    sort([1,3,9,4,8,5])
    """
    if len(array) == 1:
        # If array is only 1 element, it is sorted
        return array
    # Get middle
    mid = len(array) // 2
    # Left half
    left = array[:mid]
    # Sort left
    leftsorted = sort(left)
    # Right half
    right = array[mid:]
    # Sort right
    rightsorted = sort(right)
    # Merge
    sortedarray = merge(leftsorted, rightsorted)
    return sortedarray


def merge(array1: List[int], array2: List[int]) -> List[int]:
    """
    This function merges two sorted arrays in sorted order.
    """
    # print("Original Array 1: " + str(array1))
    # print("Original Array 2: " + str(array2))
    # print("=====MERGING=====")
    # Final array
    finalarray = []
    # Look at start of each list and compare
    while array1 and array2:
        # # Debugging
        # print("Array 1: " + str(array1))
        # print("Array 2: " + str(array2))
        # Choose smallest number at start of array
        if array1[0] < array2[0]:
            # Array1's first is smaller
            # Use it
            finalarray.append(array1[0])
            # Remove it so we can compare next numbers
            array1.remove(array1[0])
            # print("Using array 1")
        elif array1[0] > array2[0]:
            # array2's first is smaller
            # Use it
            finalarray.append(array2[0])
            # Remove it so we can compare next numbers
            array2.remove(array2[0])
            # print("Using array 2")
        elif array1[0] == array2[0]:
            # Use both
            finalarray.append(array1[0])
            finalarray.append(array2[0])
            # Delete both
            array1.remove(array1[0])
            array2.remove(array2[0])
        # print("Final array: " + str(finalarray))
        # print("=====")
    if array1:
        finalarray += array1
    elif array2:
        finalarray += array2
    # print("=====END MERGE=====")
    # print("Final merged array: " + str(finalarray))
    # print("==========")
    return finalarray
