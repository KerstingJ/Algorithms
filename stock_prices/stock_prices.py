#!/usr/bin/python

import argparse


def find_max_profit(prices):
    #                           l
    #  [1050, 270, 1540, 3800, 2]
    #                      h
    store = dict()
    best = None

    for price in prices:
        for key in store:
            if store[key] is None or store[key] < price - key:
                store[key] = price - key

            if best is None or store[key] > best:
                best = store[key]

        store[price] = -float("inf")

    return best


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
