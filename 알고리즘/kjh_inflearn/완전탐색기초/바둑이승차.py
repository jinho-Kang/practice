import sys
sys.stdin=open("input.txt","r")

def DFS(L,sum,tsum):
    global result
    # total-tsum은 앞으로 더해야할 값이고
    # sum은 지금까지 더한값인데 그값이 result보다 작다면
    # 볼필요가없는거지
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])



if __name__=="__main__":
    c,n=map(int,(input().split()))
    a=[0]*n
    result=-2147000000
    for i in range(n):
        a[i]=int(input())
    total=sum(a)
    DFS(0,0,0)
    print(result)