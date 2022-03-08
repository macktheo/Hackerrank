#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    # menggunakan slicing 
    low,high = scores[0],scores[0]
    n_low,n_high = 0,0
    for bil in scores [1:]:
        if bil < low :
            low = bil
            n_low += 1
        elif bil > high:
            high = bil
            n_high+=1
    return n_high,n_low
    
    # menggunakan  slicing dan packing unpacking
    
    lo,hi = scores [0],scores [0]
    nLow,nHigh = 0,0 
    
    for bil in scores [1:]:
        lo,nLow = (bil,nLow+1) if bil < lo else (lo,nLow)
        hi,nHigh = (bil,nHigh+1) if bil > hi else (hi,nHigh)
        
    return nHigh,nLow
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
