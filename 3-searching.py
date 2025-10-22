sorted_list = [-20, -15, -7, -6, -3, -2, -1, 0, 1, 2, 3, 3, 5, 6, 7, 9, 11, 12, 13, 15, 18, 19, 21, 23, 26, 30, 34, 37, 42, 50]

def linear_search(input, value):
    for i in input:
        if i == value:
            return True
    return False

def binary_search(input, value):
    # Creates two indexing variables
    start_index = 0
    end_index = len(input) - 1

    # Indexes through the entire array
    while start_index <= end_index:
        # Recursively splits the size of the array and assigns that value to the midpoint
        midpoint = (start_index + end_index) // 2
        # If that midpoint value is equal to the target, return True
        if input[midpoint] == value:
            return True
        # If not, then check if the value is larger than the midpoint
        elif value > input[midpoint]:
            # If it is then make the starting index the midpoint + 1
            start_index = midpoint + 1
        else:
            # Otherwise, make the ending index midpoint - 1
            end_index = midpoint - 1
        # Loop back to the start with the altered start / end index and loop until target found
    # If the target isn't found, return False
    return False

print(binary_search(sorted_list, -2))

