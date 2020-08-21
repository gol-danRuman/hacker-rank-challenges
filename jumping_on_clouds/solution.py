#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # how many time we jump and our current position
    total_jump = index = 0
    while index < len(c) -1 :
        # if our index is 2 path sort and our 2 jump is safe as current cloud then we jump 2
        if (index < len(c)-2) and (c[index] == c[index+2]):
            index+=2   
        # else we jump next cloud comming
        else:
            index+=1
        # count number of jump taken
        total_jump+=1
    # number of jump we take fastes to reach our goal
    return total_jump

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
