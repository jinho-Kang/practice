import sys
sys.stdin=open("input.txt","r")
N=int(input())
l1=list(map(int,input().split()))
M=int(input())
l2=list(map(int,input().split()))
l3=[]
for i in range(N):
    for j in range(M):
        if l1[j]<l2[j+1] and j==M-1:
            l3.append(l1[i])
        else:
            l3.append(l2[j])
for i in l3:
    print(i,end=" ")