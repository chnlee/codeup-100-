a,b = map(int, input().split())
c = bool(a)
d = bool(b)
print(c and (not d) or d and (not c))