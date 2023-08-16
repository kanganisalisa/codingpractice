import time

"""Chapter 8: Recursion and Dynamic Programming"""


def fibRecursion(n):
    """
    class fib recursion.
    """
    if n == 0 or n == 1:
        return n
    return fibRecursion(n-1) + fibRecursion(n-2)

def fibTopDown(n):
    """
    top down DP approach to fib.
    """
    memo = [0 for i in range(n+1)]
    return fibTopDownHelper(n, memo)

def fibTopDownHelper(n, memo):
    if n == 0 or n == 1:
        return n
    memo[n] = fibTopDownHelper(n-1, memo) + fibTopDownHelper(n-2, memo)
    return memo[n]

def fibBottomUp(n):
    """
    bottom down DP approach to fib.
    """
    if n == 0 or n == 1:
        return n
    memo =[0 for i in range(n+1)]
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

def fibSaveSpace(n):
    """
    bottom down DP approach to fib.
    saves values in 3 vars rather than O(n) list.
    """
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
    return c

def triplestep(n):
    """
    8.1
    n stairs, can either hop 1, 2, 3 at a time.
    how many ways can run up n stairs?
    """
    if n == 0 or n == 1 or n == 2:
        return n
    a, b, c = 0, 1, 2
    for i in range(3, n+1):
        d = a + b + c
        a = b
        b = c
        c = d
    return d

n = 10
print("recursive fibonacci: ", fibRecursion(n))
print("top down fibonacci: ", fibTopDown(n))
print("bottom up fibonacci: ", fibBottomUp(n))
print("save space fibonacci: ", fibSaveSpace(n))
print("8.1 triple step: ", triplestep(n))
