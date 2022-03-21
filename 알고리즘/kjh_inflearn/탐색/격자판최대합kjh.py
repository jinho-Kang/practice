import sys
sys.stdin=open("input.txt","r")
n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
sum1=0
d_sum1=0
d_sum2=0
row_sum=[]
col_sum=[]
diagonal_sum=[]

# row_sum 구하기
for value in l:
    row_sum.append(sum(value))

# col_sum 구하기,두 대각선의 합 구하기
for i in range(len(l)):
    sum1=0
    d_sum1+=l[i][i]
    d_sum2+=l[i][len(l)-1-i]
    for j in range(len(l)):
        sum1+=l[j][i]
    col_sum.append(sum1)
row_sum.sort()
col_sum.sort()

print(max(row_sum[4],col_sum[4],d_sum1,d_sum2))