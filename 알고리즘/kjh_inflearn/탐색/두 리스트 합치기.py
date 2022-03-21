import sys
sys.stdin=open("input.txt","r")
n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
p1=p2=0
c=[]
while p1<n and p2<m:
    if l1[p1]<=l2[p2]:
        c.append(l1[p1])
        p1+=1
    else:
        c.append(l2[p2])
        p2+=1
if p1<n:
    # 이게 됨,,, c리스트요소의
    # 마지막부터 l1의 요소를 넣어주는것임
    c=c+l1[p1:]
if p2<m:
    c=c+l2[p2:]
print(c)
# sort쓰면 복잡도가 nlog(n)이 됨...
