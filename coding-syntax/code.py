#!/usr/bin/env python3

# Given a list of n numbers, determine if it contains any duplicate numbers.
def find_duplicates(n):
    seen = set()
    for _ in n:
        if _ not in seen:
            seen.add(_)
        return False
    return True

# Given a string of text and a number k, find the k
# words in the given text that appear most frequently.
# Return the words in a new array sorted in decreasing order.
def find_frequent_words(text, k):
    from collections import Counter
    frequency = text.split()
    return Counter(frequency).most_common(k)
