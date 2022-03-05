import sys
sys.stdin=open("input.txt","r")
n=input()
r=0
sum=0

for i in range(len(n)):
    r=int(n[i])
    if r<=1 or sum<=1:
        sum+=r
    else:
        sum*=r
print(sum)