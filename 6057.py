a,b = map(int, input().split())
c = bool(a)
d = bool(b)
print(not(c and (not d) or d and (not c)))