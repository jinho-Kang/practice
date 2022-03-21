import sys
sys.stdin=open('input.txt',"r")
a=list(range(21))
# 변수가 없는것,변수없이반복함....
for _ in range(10):
    s,e=map(int,input().split())
    for i in range((e-s+1)//2):
        # 파이썬에선 스왑을 이렇게할수있음,,
        a[s+i],a[e-i]=a[e-i],a[s+i]
        # 그리고 내가 짠거하고 다른 이유는
        # 내꺼는 인덱스 0이 1이지만
        # 여기서는 인덱스1이 1이라서그럼.
# 요소하나 제거
a.pop(0)
for x in a:
    print(x,end=' ')