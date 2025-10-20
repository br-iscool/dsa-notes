# Competitive Programming Notes

### Time Complexity

The time complexity of an algorithm estimates the amount of time an algorithm will use for some input. It is represented as a function whose variable is the size of the input (usually the variable ```n```). 

The time complexity of an algorithm is denoted *O(...)*, where the three dots represent a function. 

The following time complexity classes detail the most common classes algorithms take.

- *O*(1), constant time:
  - The running time of a constant time algorithm doesn't depend on the input size. Examples include accessing a specific index in an array, pushing and popping in a stack, and direct formulas (Binet's formula for Fibonacci numbers as an example). 
- *O*(log n), logarithmic time:
  - Logarithmic time algorithms often halves the input size at each step. Examples include a binary search, calculating the *n*th Fibonacci number using recursion with memoization, and finding the smallest / largest number in a binary search tree. 
- *O*($\sqrt{n}$), square root time:
  - A square root time algorithm is slower than logarithmic time but faster than linear time. Examples include finding Euler's totient, or finding the sum of divisors for prime numbers.
- *O*($n$), linear time:
  - Linear time algorithms goes through the input a constant number of times. This is most commonly the best possible time complexity for algorithms. Examples include a linear search, traversing an array, and comparing two strings. 
- *O*(n log n), linearithmic time:
  - Divide and conquer algorithms, like most efficient sorting algorithms usually have linearithmic time. Examples include merge sort, heap sort, and quick sort.
- *O*($n^{2}$), quadratic time:
  - A quadratic time algorithm often contains two nested loops. Examples include iterative sorting algorithms like bubble sort, selection sort, and insertion sort.
- *O*($n^{3}$), cubic time:
  - A cubic time algorithm often contains three nested loops. Examples include solving cubic equations. 
- *O*($k^{n}$), exponential time:
  - Exponential time algorithms are in the form $k^{n}$, where k is an integer. Algorithms with this time complexity often iterate through all subsets of the input elements. Examples include finding the *n*th Fibonacci number without memoization, or generating a power set of a set with *n* unique elements. 
- *O*($n!$), factorial time:
  - This is one of the slowest time complexity classes. Factorial time algorithms often iterate through all permutations of the input elements. Examples include most brute-force algorithms. 

An algorithm is in polynomial time if its time complexity is at most *O*($n^{k}$) where $k$ is a constant. All of the above time complexity classes are polynomial except exponential and factorial time. In most algorithms, the constant $k$ is usually small, meaning polynomial time algorithms are usually efficient. 

### Sorting

Sorting is a fundamental algorithm that many efficient algorithms use as a subroutine. For example, the problem "does an array contain two equal elements?" is easier to solve after sorting. 

The basic problem is as follows:\
*Given an array that contains n elements, your task is to sort the elements in increasing order.*

The most simple sorting algorithms work in *O*($n^{2}$) time. Examples include bubble sort, insertion sort, and selection sort. However, more optimized algorithms usually sort in *O*(n log n) time. Examples include merge sort, quick sort, and heap sort. 

In competition, however, it is usually not required to use your own implementation of a sorting algorithm over the built in function ```sort```. Only if the datasets are large should you implement a sorting algorithm. 

### Searching