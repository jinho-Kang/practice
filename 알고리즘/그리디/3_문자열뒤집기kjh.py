import sys
sys.stdin=open("input.txt","r")
n=input()
data=n[0]
cnt_0=0
cnt_1=0
if data=='0':
    cnt_1+=1
else:
    cnt_0+=1
for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        # 다음수가 0인경우 1로 뒤바꿔줌.
        if n[i+1]=='0':
            cnt_1+=1
        else:
            cnt_0+=1
print(min(cnt_0,cnt_1))