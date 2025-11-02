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

### Problems involving minimizing sums

### Data Compression

## Dynamic Programming