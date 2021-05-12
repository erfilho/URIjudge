from math import pow
from math import sqrt

p1x, p1y = input().split(" ")
p2x, p2y = input().split(" ")

p1x = float(p1x)
p1y = float(p1y)

p2x = float(p2x)
p2y = float(p2y)

dist = sqrt(pow(p2x - p1x, 2)+pow(p2y - p1y, 2))

print(f'{dist:.4f}')