#!/bin/python3

import math
import os
import random
import re
import sys


def divisibleSumPairs(n, k, ar):
    #  Cara 1 
    
    hasil = 0
    for i in range (len(ar)-1):
        for j in range (i+1, len(ar)):
            if (ar[i]+ar[j])%k == 0 :
                hasil += 1
    return hasil
    
    # cara 2
    
    hasil = 0
    for i, item1 in enumerate(ar[:-1]):
        for item2 in ar [i+1:]:
            if (item1+item2)%k == 0:
                hasil += 1
    return hasil
    
    # cara 3
    hasil = 0
    for i, item1 in enumerate(ar[:-1]):
        counter += len([item2 for item2 in ar[i+1:] if (item1 + item2) %k == 0 ])  
    return hasil
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
