#!/bin/python3

import math
import os
import random
import re
import sys

def migratoryBirds(arr):
    
    highest_count = 0
    highest_bird = 0
    for i in range (1,6):
        count  = len([bird for bird in arr if bird == i ])
        if highest_count < count:
            highest_count = count
            highest_bird = i
    return highest_bird 
# menggunakan index dan method max
    bird_count = [0] * 5
    for burung in arr :
        bird_count [burung-1] += 1
    return bird_count.index (max (bird_count)) + 1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
