import sys
sys.stdin=open("완전탐색기초\input.txt","r")

# L은 index
def DFS(L,sum):
    if sum>total//2:
        return 
    # 이번에는 0번인덱스부터시작하니까
    if L==n:
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)

if __name__=="__main__":
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    DFS(0,0)
    print("NO")