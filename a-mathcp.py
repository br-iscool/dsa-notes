import math

"""
# Input normally
a, b, c = input().split(' ')
print(a, b, c)

# Input with map
a, b, c = map(int, input().split(' '))
print(a, b, c)
"""

# Set methods
# .add() adds an element to a set
# .clear() clears the entire set
# .discard() removes a specific element in the set
# .remove() also removes a specific element in the set, but it will raise an error if the element specified does not exist, while .discard() does not
# .pop() removes a random element in the set (note that it is different from list.pop())
a = set({1, 4, 6, 7})
b = set({2, 4, 6, 10})
c = a.union(b) 
# you can use a.union, .intersection .difference, etc.
# you can also use the following symbols
# - for difference
# & for intersection
# | for union
print(c)

# Min / max methods
print(min([1, 2, 3]))
print(max([1, 2, 3]))

# Factorial
print(math.factorial(10))

# Fibonacci using recursion (no memoization)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(6))