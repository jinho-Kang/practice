import sys
sys.stdin=open("input.txt","r")
n=int(input())
l=list(map(int,input().split()))
r=0
cnt=0
for i in l:
    r+=1
    if r>=i:
        cnt+=1
        r=0
print(cnt)