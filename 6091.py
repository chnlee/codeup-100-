a,b,c = map(int, input().split())

result = 1
while result % a !=0 or result % b!=0 or result % c !=0:
  result += 1

print(result)