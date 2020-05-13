#!usr/bin/env python3

import random

# Given a fixed length array arr of integers, duplicate each occurrence of zero
# shifting the remaining elements to the right. Note that elements beyond the
# length of the original array are not written. Do the above modifications
# to the input array in place, do not return anything from your function.

# Time/Space Complexity -> O(n), O(1)
def duplicate_zeros(iterable):
    length = len(iterable) - 1
    match = 0
    for left in range(length + 1):
        if left > length - match:
            break
        if iterable[left] == 0:
            if left == length - match:
                iterable[length] = 0
                length -= 1
                break
            match += 1

# Shuffle a set of numbers without duplicates.

# Time/Space Complexity -> O(n), O(n)
class ShuffleArray:
    def __init__(self, nums):
        self.list = nums
        self.old_list = list(nums)

    def reset(self):
        self.list = self.old_list
        self.old_list = list(self.old_list)
        return self.list

    def shuffle(self):
        for i in range(len(self.list)):
            shuffle = random.randrange(i, len(self.list))
            self.list[i], self.list[shuffle] = self.list[shuffle], self.list[i]
        return self.list
