#!/bin/python3

import math
import os
import random
import re
import sys


def getTotalX(a, b):
    c =[]
    for bil in range (a [-1],b[0]+1):
        for x in (a+b):
            if x<bil and bil%x != 0:
                break
            if x> bil and x%bil != 0:
                break
        else:
            c.append(bil)
    return len(c)  
    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
#note masih bingung sama soalnya
