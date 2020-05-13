#!/usr/bin/env python3

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top? Note: Given n will be a positive integer.

# The function takes parameter n(int), which represents steps.
# Returns the amount of unique ways to reach the top.


def climb(n):  # Fibonacci approach will be used as it's the simplest approach.
    first, second = 1, 1  # Set values for the first and second steps.
    for _ in range(n - 1):  # Run code block n times.
        third = first + second  # Add first and second to get third step.
        first = second  # Store the value of second into first.
        second = third  # Store the value of third into second.
    return second  # Actually returns the final value.

# Time Complexity -> O(n)

# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one. Your algorithm should have a linear runtime
# complexity. Could you implement it without using extra memory?

# The function takes parameter arr(list), which represents the non-empty array.
# Returns the unique value that's in the list.


def find_single_number(arr):  # Bitwise approach since it's the fastest.
    x = 0  # Set initial value for x.
    for y in arr:  # Iterate through parameter arr (list).
        x ^= y  # Use bitwise exclusive or (XOR) to find unique number.
    return x  # Return the unique number.

# Time Complexity -> O(n)


if __name__ == "__main__":
    # Run first problem
    print(climb(5))
    print(climb(10))
    # Run second problem
    print(find_single_number([0, 0, 1, 1, 2, 3, 3, 4, 4]))
    print(find_single_number([5, 5, 6, 6, 7, 7, 8, 8, 9]))
