#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    #menggunakan slicing
    jam = int(s[:2])
    if s[-2:] == 'PM' and jam != 12 and jam>= 1:
        jam += 12
    elif s[-2:] == 'AM' and jam == 12 :
        jam = 0
    return '{j:02d}{md}'.format(j=jam, md=s[2:-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
