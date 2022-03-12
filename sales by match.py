#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    """warna_unik = set(ar)
    jumlah_warna = { warna :0 for warna in warna_unik } 
    for warna in ar :
        jumlah_warna[warna]+= 1
    total_pasangan = 0 
    for warna in warna_unik:
        total_pasangan += jumlah_warna[warna]//2
    return total_pasangan"""
    
    return sum([len([kaosKaki for kaosKaki in ar if kaosKaki == warna])// 2  for warna in set (ar) ])
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
