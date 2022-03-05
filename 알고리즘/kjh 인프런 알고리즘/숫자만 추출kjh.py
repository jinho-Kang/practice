import sys
sys.stdin=open("input.txt","r")
s=input()
cnt=0
sum=""
for i in s:
    if i.isdecimal():
        if i=='0' and cnt==0:
            continue 
        else:sum+=i
        cnt+=1
int_sum=int(sum)
print(int_sum)
cnt=0
for i in range(1,int_sum+1):
    if int_sum%i==0:
        cnt+=1
print(cnt)