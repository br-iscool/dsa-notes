# Mathematics for Competitive Programming Notes

## Summation

There are a few basic sum formulas that should be memorized. 

- *n*th triangular number (sum of natural numbers):
  - Each sum of the form $\Sigma  x^k$, where x starts at 1 and increases by 1 and k > 0 can be calculated using a formula. 
  - This formula is ```n(n+1) / 2```.
- Arithmetic progression
  - An arithmetic progression is a sequence of numbers for which the difference between any two consecutive numbers is constant. 
  - For example: 3, 7, 11, 15
  - The sum of an arithmetic progression is calculated by ```n(a+b) / 2```, where *n* is the number of terms, *a* is the first term, and *b* is the last term. 
- Geometric progression
  - The idea of a geometric progression is the same as an arithmetic progression, except the ratio between any two consecutive numbers is constant. 
  - For example: 2, 4, 8, 16, 32
  - The sum is calculated by ```(bk - a) / (k - 1)```, where *k* is the ratio between two consecutive numbers. 

## Set Theory

A set is a collection of elements, defined using curly braces. For example, ```X = {3, 5, 6}```. This set would contain the elements *2, 4, 7*. The symbol $\emptyset$ denotes an empty set and |S| refers to the size of a set (the number of elements in a set). 

For sets *A* and *B*, set operations can be used to construct new sets. 

- Intersection:
  - The intersection of sets A and B contains elements in both sets. For example, if ```A = {3, 5, 7}``` and ```B = {3, 6, 8}```, then the intersection of A and B would be ```{3}```. 
- Union
  - The union of sets A and B contains elements that are in either set, or both. For example, if ```A = {3, 7}``` and ```B = {2, 3, 8}```, then the union of A and B would be ```{2, 3, 7, 8}```. (You can think of this like merging two lists together.)
- Difference 
  - The difference of set A and B contains elements that are in A but not in B. However, B can still contain elements that are not in A. For example, if ```A = {2, 3, 7, 8}``` and ```B = {3, 5, 8}```, then the difference of A and B would be ```{2, 7}```.
- Complement
  - The complement of set A contains elements that are not in A. The complement depends on a universal set, which contains all possible elements. For example if ```A = {2, 3, 6}``` and the universal set is ```{1, 2, ..., 10}```, then the complement of set A is ```{1, 4, 5, 7, 8, 9, 10}```.

Let S be a set of numbers.\
If all elements of set A are also elements of set S, then A is known as a subset of S, and S a superset of A. For example, subsets of the set ```{2, 4}``` are $\emptyset$, ```{2}```, ```{4}```, and ```{2, 4}```.

The total number of subsets can always be found with $2^{|S|}$, where $|S|$ is the size of the set. 

## Functions

The value of a logical expression is either True (1) or False (0). 

The function $\lceil x \rceil$ can be used to round a function up to the nearest integer (ceiling function), while the function $\lfloor x \rfloor$ rounds a function down to the nearest integer (floor function).\
For example: $\lceil 3/2 \rceil = 2$ and $\lfloor 3/2 \rfloor = 1$.

The functions ```min([1, 2, 3])``` and ```max([1, 2, 3])``` get the smallest and largest values in the list, respectively. 

The factorial of any number can be calculated by using ```math.factorial(x)``` where x is the number to factorial.

The *n*th Fibonacci number can be calculated using the formula ```f(n) = f(n-1) + f(n-2)``` recursively or using *Binet's Formula*, which 