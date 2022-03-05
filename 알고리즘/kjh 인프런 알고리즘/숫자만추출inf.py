import sys
sys.stdin=open("input.txt","r")
s=input()
res=0
for x in s:
    if x.isdecimal():
        # 핵심코드:나랑다른코드,,
        res=res*10+int(x)
    # isdecimal은 0부터9까지만찾아주는것
    # isdigit은 숫자 다찾아줌.2^3
    # 이런것도 digit으로처리한다고함.
print(res)
cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)