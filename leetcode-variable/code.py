#!/usr/bin/env python3

# Given an array nums of n integers where n > 1, return an
# array output such that output[i] is equal to the product
# of all the elements of nums except nums[i].
# Constraint: It's guaranteed that the product of the elements of any prefix
# or suffix of the array (including the whole array) fits in a 32 bit integer.
# Note: Please solve it without division and in O(n).

def product_except_self(nums):
    answer = [1 for _ in enumerate(nums)]
    for i in range(1, len(nums)):
        answer[i] = nums[i - 1] * answer[i - 1]
    right = 1
    for j in range(len(nums) - 1, -1, -1):
        answer[j] *= right
        right *= nums[j]
    return answer

# Given a set of distinct integers, nums, return all possible subsets
# (the power set). Note: The solution set must not contain duplicate subsets.

def subsets(nums):
    n = len(nums)
    return [[nums[j] for j in range(n) if bin(i)[3:][j] == "1"] for i in range(2**n, 2**(n + 1))]
