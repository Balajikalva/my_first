from one_python import converter as convo

import random

t = random.randint(0,100)

print("value of t is",t)

for _ in range(t):

    n = random.randint(1,10000)

    a = random.randint(2,10)

    ans = convo(n,a)

    print(n,a,ans)
