# Competitive Programming Techniques Notes

## Complete Search

Complete search is a general method that can be used to solve almost any algorithm problem. The idea is to generate all possible solutions to the problem using brute force, and then select the best result or count the number of solutions, depending on the problem. 

Complete search is a good technique if there is enough time to go through all the solutions, because the search is usually easy to implement and it gives the correct answer. If complete search is too slow, other techniques, such as greedy algorithms or dynamic programming, may be used.

### Backtracking

A *backtracking* algorithm begins with an empty solution and extends the solution step by step. The search recursively goes through all different ways how a solution can be constructed. 

As an example, consider the problem of calculating the number of ways $n$ queens can be placed on an $n * n$ chessboard so that no two queens are attacking each other. 

The problem can be solved by using backtracking. More precisely, we will place queens on the board row by row. Exactly one queen will be placed on each row so that no queens attacks queens previously placed. 

### Pruning

We can often optimize algorithms by pruning the search. The idea is to add a routine to the algorithm so that it will notice when a partial solution cannot be extended to a complete solution. 

### Meet in the Middle

Furthermore, meet in the middle is a technique where the search space is divided into two parts of about equal size. A separate search is performed for both parts, and finally the results are combined. 

The technique is usually used when there is an efficient way to combine the results of the searches. In a situation, two searches may require less time than one large (combined) search. 

## Greedy Algorithms

A *greedy algorithm* constructs a solution by always making a choice that looks the best at the moment. A greedy algorithm doesn't take back its choices, but directly constructs the final solution. For this reason, greedy algorithms are usually very efficient but can be slow in worst-case scenarios. 

### Problems involving scheduling

Many problems involving schedules are solved with greedy algorithms. For example, given $n$ events with starting and ending times, find a schedule that includes as many events as possible without having overlap / partial events. 

The best method is to make an algorithm that always selects the next possible event that ends as early as possible. It turns out that this algorithm always produces an optimal solution, no matter the number of events. The reason for this is that it is always optimal to first select an event that ends as early as possible. After, the algorithm selects the next event using the same strategy. This is an example of a greedy algorithm being correct. 

Again, let us consider a different problem where we are given $n$ tasks with durations and deadlines and our task is to choose an order to perform the task. For each task, we earn $d-x$ points where $d$ is the task's deadline and $x$ is the moment we can finish the task. What is the largest possible total score we can obtain?

For example, suppose that the tasks are as follows:
| task | duration | deadline |
|------|----------|----------|
| A    | 4        | 2        |
| B    | 3        | 5        |
| C    | 2        | 7        |
| D    | 4        | 5        |

In this case, an optimal schedule would be C, B, A, D. This solution earns -10 points in total. The correct strategy for this would be to perform the tasks sorted by their durations in increasing order. The reason for this is that if we ever perform two tasks one after another such that the first task takes longer than the second task, we can obtain a better solution if we swap the order of the two tasks. 

### Data Compression

In data compression, a binary code gives each character in a string its own unique sequence of bits (called a codeword). In simpler terms, characters in a string get represented by ones and zeros to take up less space. 

If each character is represented by codewords with the same length, the code would be a constant-length code. However, to further compress strings, we can use variable-length codes, meaning that lesser used characters would be represented by longer codewords, as opposed to often used codewords. The length of most strings would then decrease. 

The most optimal code would produce a compressed string as short as possible, in order to reduce the size it takes. 

## Dynamic Programming

Dynamic programming is a technique that combines the correctness of complete search and the efficiency of greedy algorithms. Dynamic programming can be applied if the problem can be divided into smaller subproblems which are solved independently. There are two main uses for dynamic programming:

- Finding an optimal solution
- Counting the total number of possible solutions 

Let us focus on a problem that involves money. Given a set of values ```coins = {c1, c2, c3, ...}``` and a target sum of money ```n```, our task is to form the sum ```n``` using as few coins as possible. 

The idea in dynamic programming is to formulate the problem recursively so that the final solution to the problem can be calculated from the solutions of smaller subproblems. Let ```solve(x)``` denote the minimum number of coins required for a sum $x$. The value of the function depends on the value of the coins. For example, if ```coins = {1, 3, 4}```, the first values of the function are as follows:

$solve(0) = 0$\
$solve(1) = 1$\
$solve(2) = 2$\
$solve(3) = 1$\
$solve(4) = 1$\
$solve(5) = 2$\
$solve(6) = 2$\
$solve(7) = 2$\
$solve(8) = 2$\
$solve(9) = 3$\
$solve(0) = 3$

For example, ```solve(10) = 3```, because at least three coins are required to form the sum 10. The optimal solution is $(3 + 3 + 4) = 10$.

The values of ```solve()``` can be recursively calculated from its smaller values. The idea is to focus on the first coin that we choose for the sum. For example, in the above scenario, the first coin can either be 1, 3, or 4. If we choose coin 1, the remaining task is to form the sum 9 using the minimum number of coins, which is a subproblem of the entire problem. The same applies to coins 3 and 4. The following formula can be then derived to calculate the minimum number of coins for this set.

```solve(x) = min(solve(x - 1) + 1, solve(x - 3) + 1, solve(x - 4) + 1)```

The base case of this recursion is ```solve(0) = 0```, because no coins are needed for an empty sum. 

Now, we are ready to get a general recursive function that calculates the minimum number of coins needed for a sum $x$:

$$
f(x) =
\begin{cases}
\infty, & \text{if } x < 0, \\
0, & \text{if } x = 0, \\
f(x - c) + 1, & \text{if } x > 0.
\end{cases}
$$

If the value of x is less than 0, then the function would return infinity, as we cannot have a negative amount of coins. If the function is 0, then x would also be 0, as no coins are needed for an empty sum. If the value of x is greater than 0, then we recursively go through the possibilities of choosing the first coin for the sum. 

### Memoization

The main idea of dynamic programming is to use memoization to efficiently calculate values of a recursive function. This means that the values of the function are stored in an array after calculating them. For each parameter, the value of the function is calculated recursively once, and in future uses, the value can be directly retrieved from the array. 

Memoization is much more efficient, because the answer for each parameter $x$ is calculated recursively only once. Because the values can be efficiently retrieved, the time complexity of the coin problem algorithm with memoization is $O(nk)$, where n is the target sum and k is the number of coins. 

### Problems involving finding specific subsets

These types of problems often involve a set of objects, and subsets with specific properties have to be found from the original set. Problems like these are often solved with dynamic programming. 

Consider the following problem:\
Given a list of weights ```[w1, w2, ...]```, determine all sums that can be constructed using the weights. For example, if the weights are ```[1, 3, 3, 5]```, then all numbers between 0 and 12 are possible sums, with the exception of the numbers 2 and 10. For example, the number 7 is possible because we can select the weights ```[1, 3, 3]```. 

To solve the problem, we use dynamic programming to focus on subproblems where we only use the first $k$ weights to construct sums. If we can construct a sum $x$ using the first $k$ weights, then ```possible(x, k) = true```. Otherwise, let ```possible(x, k) = false```. This can be calculated using the following equation:\
```possible(x, k) = possible(x, wk, k - 1) OR possible(x, k - 1)```, where ```wk``` is the first $k$ weights. 

The formula is based on the fact that we can either use or not use the weight $wk$ in the sum. If we do use it, the remaining task is to form the sum $x - wk$ using the first $k - 1$ weights, and if we do not use $wk$, then form the sum $x$ using the first $k - 1$ weights. 

After calculating all these values, ```possible(x, n)``` tells us whether we can construct a sum $x$ using ALL of the weights. 

## Amortized Analysis

The time complexity of an algorithm is often easy to assess just by examining the structure of the algorithm. Specifically, analyzing the number of loops the algorithm contains and how many times each loop is performed usually works. However, sometimes a straightforward analysis is not completely accurate for getting the time complexity of an algorithm.

Amortized analysis is a method that can be used to analyze algorithms for their time complexity. The idea is to estimate the total time used for all operations during the execution of the algorithm, instead of just focusing on individual operations.

### Problems involving nearest smallest elements

Amortized analysis is often used to estimate the number of operations performed on a data structure. The operations might be distributed unevenly so that most operations occur during a certain phase of the algorithm, but the total number of operations is limited. 

For example, consider the problem of finding for each list element the nearest smallest element (the first smaller element that precedes the current element in the list). It's possible that this element doesn't exist, in which case the algorithm should return that the element does not exist. 

To solve the problem, we go through the list from left to right and maintain a stack of list elements. At each list position, we remove elements from the stack until the top element is smaller than the current element, or if the stack is empty.

## Range Queries

### Static Array Queries

### Binary Indexed Tree

### Segment Tree

## Bit Manipulation

### Bit Representation & Operations

### Bit Optimizations