#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # total number of pair of socks
    count = 0
    # sort list to check next high order number
    ar.sort()
    # add # to array to check last value with #
    ar.append('#')
    # for looping array
    i = 0
    while i < n:
        # if current color and next color match set them pair and check i+2 index color
        if ar[i] == ar[i+1]:
            count+=1
            i+=2
        # if not select next color to compare
        else:
            i+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()