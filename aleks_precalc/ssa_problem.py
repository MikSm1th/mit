import math

aa = input("What is side a: ? ")
bb = input("What is side b: ? ")
AA = input("What is side A(degrees): ? ")

aa = int(aa)
bb = int(bb)
AA = int(AA)

def no_of_solutions(a, b, A):
    if A > 90 and a <= b:
        ans = "No solution"
    elif A > 90 and a > b:
        ans = "One triangle"
    elif A < 90 and (a < b * math.sin(math.degrees(A)) or a < b):
        ans = "No solution"
    elif A < 90 and (a == math.sin(math.degrees(b)) or a >= b):
        ans = "One triangle"
    elif A < 90 and h < a:
        ans = "Two triangles"
    elif A < 90 and ((b * math.sin(math.degrees(A))/a) > 1):
        ans = "No triangles"
    elif A < 90 and ((b * math.sin(math.degrees(A))/a) < 1):
        ans = "Two triangles"
    elif A < 90 and (b * math.sin(A) < a):
        ans = "Two triangles"
    return ans

ans = no_of_solutions(aa, bb, AA)

print(aa,bb,AA)
print(ans)