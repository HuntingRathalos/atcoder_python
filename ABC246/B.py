A, B = map(int, input().split())
from math import sqrt
d = sqrt(A ** 2 + B ** 2)
x = A / d
y = B / d
print(x, y)
