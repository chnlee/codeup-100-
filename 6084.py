h,b,s,c = map(int, input().split())
a =h*b*s*c/8/1024/1024
print(round(a,1),"MB")