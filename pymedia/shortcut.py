import random
import math
import datetime
import r

#print
def prt(str):
    print(str)

#random
def Random(a,b):
    return random.randint(a,b)

#square_root
def sqrt(a):
    return math.sqrt(a)

#time
def timedate():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")






