#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # perulangan 
    
    n = len(arr)
    rata2pos = 0
    rata2neg = 0
    rata2zer = 0
    for bil in arr:
        if bil > 0 :
            rata2pos += 1
        elif bil < 0 :
            rata2neg += 1
        else:
            rata2zer += 1
    print (rata2pos/n)
    print (rata2neg/n)
    print (rata2zer/n)
    
    # list comperhension
    
    n = len(arr)
    positif = len([bil for bil in  arr if bil > 0])
    negatif = len ([bil for bil in  arr if bil < 0])
    nol = len([bil for bil in  arr if bil == 0])
    print(positif/n)
    print(negatif/n)
    print(nol/n)
    
    #filter,ambda,tuple
    n= len(arr)
    positif = len(tuple(filter(lambda x:x>0, arr )))
    negatif = len(tuple(filter(lambda x:x<0, arr )))
    nol = len(tuple(filter(lambda x:x==0, arr )))
    print (positif/n)
    print (negatif/n)
    print (nol/n)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
