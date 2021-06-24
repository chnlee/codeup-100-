# n = int(input())
# a = input().split()

# for i in range(9,-1,-1):
#  print(a[i],end=" ")


n = int(input())
a = input().split()
d = []
for i in a:
  d.append(i)

d.reverse()

for n in d:
  print(n,end=" ")

