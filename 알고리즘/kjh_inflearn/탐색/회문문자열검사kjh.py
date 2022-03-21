import sys
sys.stdin=open("input.txt","r")
n=int(input())
l=[]
for i in range(n):
    l.append(input())
left=""
right=""
for i in l:
    j=0
    while j<len(i)//2:
    # 걍 다 대문자로 바꿔버림 ㅋㅋ
        left+=i[j].upper()
        right+=i[len(i)-j-1].upper()
        j+=1
    # gooG이면 회문문자열로친다고 문제에서나와서 위에서 꼼수씀
    if left==right:
        print("YES")
    else:
        print("NO")
    left=""
    right=""
    