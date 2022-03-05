import sys
sys.stdin=open("input.txt","r")
n,k=map(int,(input().split()))
l=list(map(int,input().split()))

cnt=0

for i,v in enumerate(l):
    for j in l[i+1:]:
        if v!=j:
            cnt+=1
print(cnt)