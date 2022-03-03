#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    #menggunakan max
    """total = 0
    paling_tinggi = max(candles)
    for lilin in candles :
        if lilin == paling_tinggi:
            total += 1
    return total"""
    #menggunakan list comperhension dan max
    siTinggi = max(candles)
    return len([lilin for lilin in candles if lilin == siTinggi]) 
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
