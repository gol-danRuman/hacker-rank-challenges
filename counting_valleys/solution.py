#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    # starting point sea level is 0 and above sea level are no of valley
    valley=level=0
    for i in range(n):
        # if movement is U then we move up level
        if s[i] == 'U':
            level+=1
            # if we move up than sea level it is valley
            if level==0:
                valley+=1
        # else we are moving down from current level
        else:
            level-=1
    # total number of valley than is above sea level
    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
