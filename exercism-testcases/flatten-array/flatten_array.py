#!/usr/bin/env python3


def flatten(iterable):
    return list(_flatten(iterable))


def _flatten(iterable):
    for i in iterable:
        if isinstance(i, (list, tuple)):
            yield from _flatten(i)
        elif i is not None:
            yield i
