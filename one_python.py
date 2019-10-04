import random

n = random.randint(0,10000)

while True:

    a = random.randint(2,10)

    if a  < 11:

        break


def converter(n,a):

    s = str()

    while n>0:

        s = str(n%a)+s

        n = n//a

    return s

print("{} digit representation of {} is {}".format(a,n,converter(n,a)))
