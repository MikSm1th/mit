from math import acos, degrees, radians

a = 226
b = 284
c = 160

cosA = ((a**2 - b**2 - c**2) / (-2*b*c))

print(cosA)

ans = acos(cosA)

print(degrees(ans))