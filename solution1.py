#!/usr/bin/env python

import urllib2
import math


UNIQUE_CARDS = 5
OPEN_SPOT_CHAR = "*"


def combination(n, k):
    return math.factorial(n) / math.factorial(n - k)


if __name__ == '__main__':

    # from URL
    url = "http://www.trywildcard.com/problem1input.txt"
    data = urllib2.urlopen(url)

    bulletin_board = []

    # get line combinations
    line_combinations = 0
    for line in data:
        line = line.rstrip()
        bulletin_board.append([spot for spot in line])
        open_spots = line.count(OPEN_SPOT_CHAR)
        if open_spots >= UNIQUE_CARDS:
            line_combinations += combination(open_spots, UNIQUE_CARDS)

    columns = ["".join([x[idx] for x in bulletin_board])
               for idx in xrange(len(bulletin_board))]

    # get columns combinations
    column_combinations = 0
    for column in columns:
        open_spots = column.count(OPEN_SPOT_CHAR)
        if open_spots >= UNIQUE_CARDS:
            column_combinations += combination(open_spots, UNIQUE_CARDS)

    # # of ways it's possible to position 5 cards in open spots
    total_combinations = line_combinations + column_combinations

    print "Answer: %s" % total_combinations  # 167160
