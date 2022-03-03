#!/bin/python3

import math
import os
import random
import re
import sys


def miniMaxSum(arr):
    #perulangan
    """ mengunakan perulangan
    min,max = arr[0], arr[0]
    for bil in arr:
        if bil< min :
            min = bil
        if bil > max :
            max = bil
    print(sum(arr)-max, sum(arr)-min)"""
    
    #menggunakan method sort
    """arr.sort()
    print(sum(arr[:-1]),sum(arr[1:]))"""
    
    #menggunakan fungsi sorted 
    urut = sorted(arr)
    print(sum(urut[:-1]),(sum(urut[1:])))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
