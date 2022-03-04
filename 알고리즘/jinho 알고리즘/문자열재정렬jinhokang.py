import sys
sys.stdin=open("input.txt","r")
s=list(input())
s.sort()
sum=0
for i in s:
    if i.isdecimal():
        sum+=int(i)
for i in s:
    if not i.isdecimal():
        print(i,end="")
print(sum)
# isdecimal()사용