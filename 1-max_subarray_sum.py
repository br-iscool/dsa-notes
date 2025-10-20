"""
Given an array of n numbers, calculate the maximum subarray sum. 

The maximum subarray sum is the largest possible sum of a sequence of consecutive values in the array.
"""

arr = [-1, 2, 4, -3, 5, 2, -5, 2]

# O(n^3) solution
best = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        sum = 0
        for k in range(i, j + 1):
            sum += arr[k]
        best = max(best, sum)
print(best)

# O(n^2) solution
best = 0
for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum += arr[j]
        best = max(best, sum)
print(best)

# O(n) solution (Kadane's algorithm)
best, sum = 0, 0
for i in arr:
    # In the array above, the algorithm compares the current index to the sum + the index. 
    # In the first loop, sum and best will equal i.
	sum = max(i, sum + i)
    # Then, if the current sum is better than the current best, the current sum becomes the new current best. 
	best = max(best, sum)
    # This will loop over every single index, adding the current index to the end of the sum and comparing it to the best until it is finished looping.
print(best)