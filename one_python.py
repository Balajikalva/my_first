import random

n = random.randint(0,10000)

while True:

    a = random.randint(2,10)

    if a  < 11:

        break

print("n and a values are :",n,a)

def func(n,a):

    s = str()

    while n>0:

        s = str(n%a)+s

        n = n//a

    return s

print(func(n,a))
