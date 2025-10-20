arr = [-3, 5, 1, 2, 19, 54, 3, 6, 7, 7, 10, 15, 28, -16, -5]
sorted_arr = [-16, -5, -3, 1, 2, 3, 5, 6, 7, 7, 10, 15, 19, 28, 54]

# Bubble sort
def bubble_sort(data):
    for i in range(len(arr) - 1):
        # Go through the array, one value at a time.
        # Compare each value with the next value
        for j in range(len(arr) - i - 1):
            # If the current value is greater than the next value, swap the two elements
            if arr[j] > arr[j + 1]:
                # Repeat until sorted
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

"""
Bubble sort is an example of an algorithm that swaps two consecutive elements in an array.
The time complexity of such algorithms is always at least O(n^2). 
"""

# Merge sort
def merge(list1, list2):
    # Create an array that will hold the sorted data
    result = []
    # Create two indices to track the merged lists
    i, j = 0, 0
    
    # As long as i is less than the length of the recursively divided left list, and j is less than the length of the recursively divided right list
    while i < len(list1) and j < len(list2):
        # If the current element in the left list is less than the current element in the right list
        if list1[i] < list2[j]:
            # Append the current element in the left list to results
            result.append(list1[i])
            # Increment the first index 
            i += 1
        else:
            # If the current element in the left list is more than the current element in the right list
            # Append the current element in the right list
            result.append(list2[j])
            # Increment the second index
            j += 1
            
    # After the loop, the lists might still contain elements, but they are already in sorted order so they get extended to the results
    result.extend(list1[i:])
    result.extend(list2[j:])
    
    return result


def merge_sort(data):
    # If the length of the array is 1 or less, return the array (it is already sorted)
    if len(data) <= 1:
        return data
    
    # Otherwise, divide the array into two sections
    midpoint = len(data) // 2
    # The left list is the left side of the divided array
    left_list = merge_sort(data[:midpoint])
    # The right list is the right side of the divided array
    right_list = merge_sort(data[midpoint:])
    # Then, recursively divide the left and right lists until we have a list for each element in the array
    # Afterwards, send the data to the merge() function to remerge the lists
    return merge(left_list, right_list)

"""
Merge sort is a classic divide-and-conquer algorithm. It recursively splits the input until each piece has length 1 or 0.
Then, it recombines the pieces using the merge() function. The split is done at the midpoint, so each recursive level halves the size. 
This algorithm has O(nlogn) time complexity.
"""