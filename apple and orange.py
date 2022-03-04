#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    #list comperhension
    total_apel, total_jeruk = 0, 0
    apl = [ a+d for d in apples]  
    jrk = [ b+d for d in oranges ]  
    for d_baru in apl:
      if s<=d_baru<=t:
            total_apel += 1
            
    for d_baru in jrk :
        if s<=d_baru<=t:
            total_jeruk +=1
    print(total_apel)
    print(total_jeruk)
    
    #fungi sum + list comperhension
    apl=[ 1 if s<=a+d<=t else 0 for d in apples]
    jrk=[ 1 if s<=b+d<=t else 0 for d in oranges]
    print (sum(apl))
    print (sum(jrk))
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
