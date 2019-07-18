#!/usr/bin/python

import sys

import time
start = time.time()


def rock_paper_scissors(n):
    moves = ["rock", "paper", "scissors"]
    cache = {
        0: [[]],
        1: [["rock"], ["paper"], ["scissors"]]
    }

    def recurse(n):
        nonlocal moves, cache

        # cache starts with base case and edge case
        if n in cache:
            return cache[n]

        # this list comprehension looks so smoooooth
        cache[n] = [r + [m] for r in recurse(n-1) for m in moves]
        # works out to
        """
        l = []
        for r in recurse(n-1):
          for m in moves:
            l.append(r + [m])
        """

        return cache[n]

    return recurse(n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(len(rock_paper_scissors(num_plays)))
    else:
        print('Usage: rps.py [num_plays]')

    end = time.time()
    print(end - start)
