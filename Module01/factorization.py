from math import sqrt
import numpy as np

n = 100

n2 = int(n/2)
fn = []
for x in range(2, n2+1):
    if n % x == 0:
        fn.append(x)  # lower member of factor pair
        fn.append(n/x)  # upper member of factor pair
print('N has the following factors: ' + str(fn))

for i in range(1, int(n / 2) + 1):
    for j in range(1, i):
        if i * j == n:
            print(j, ' times ', i, ' equals ', n)

# Greated common divisor
a = np.gcd(6, 15)
b = np.gcd.reduce([5,25,35])

print(a, ',' , b)
