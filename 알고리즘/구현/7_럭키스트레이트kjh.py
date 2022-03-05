import sys
sys.stdin=open("input.txt","r")
n=input()
l=list(n)
left_s=0
right_s=0
for i,v in enumerate(l):
    v=int(v)
    if i<=len(l)//2-1:
        left_s+=v
    else: 
        right_s+=v
if left_s==right_s:
    print("LUCKY")
else:
    print("READY")
# 정수로주어진다.
# 인풋은항상짝수이다.