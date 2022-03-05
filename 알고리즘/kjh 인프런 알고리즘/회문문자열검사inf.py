import sys
# sys.stdin=open("input.txt")
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)
    for j in range(size//2):
        # 파이썬에서는 인덱스를 -로도 접근할수있다
        if s[j]!=s[-1-j]:
            print(f"#{i+1} No")
            break
    else:
        print(f"#{i+1} Yes")
# if s!=s[::-1]:
#     print(f"#{i+1} No")
# else:
#     print(f"#{i+1} Yes")
# 이렇게 파이썬처럼 짜는것도 가능.