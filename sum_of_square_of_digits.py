N=int(input())
s=0
while N>0:
    r=n%10
    s=s+(r*r)
    N=N//10
print(s)
