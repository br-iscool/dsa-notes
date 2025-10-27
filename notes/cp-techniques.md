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

### Scheduling

### Tasks and Deadlines

### Minimizing Sums

### Data Compression

## Dynamic Programming