#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    # Write your code here
    # cara 1
    n = 0
    for i in range (len(s)-m+1):
        if sum (s[i:i+m]) == d:
            n+= 1
    return n
    
    # cara 2
    n= 0
    for i in range (len(s)-m+1):
        n+=1 if sum (s[i:i+m]) == d else 0
    return n
    # cara 3
    n = [ 1 if sum (s[i:i+m])==d else 0 for i in range (len(s)-m+1) ]
    return sum(n)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
