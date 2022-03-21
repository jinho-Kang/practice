import sys
sys.stdin=open("input.txt","r")
l=[]
for i in range(10):
    n=tuple(map(int,input().split()))
    l.append(n)
l2=[x for x in range(1,20+1)]
tmp=0
for j,v in enumerate(l):
    for k in range((v[1]-v[0])//2+1):
        tmp=l2[v[0]+k-1]
        l2[v[0]+k-1]=l2[v[1]-k-1]
        l2[v[1]-k-1]=tmp
        # swap문제임
for x in l2:
    print(x, end=" ")
# 풀었다 히히