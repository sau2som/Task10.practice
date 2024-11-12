import math
import os
import random
import re
import sys

weird='Weird'
not_weird='Not Weird'

if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2 !=0:
        print(weird)
    elif n>=2 and n<=5:
        print(not_weird)
    elif n>=6 and n<=20:
        print(weird)
    else:
        print(not_weird)
        