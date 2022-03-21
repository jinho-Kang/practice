





s="01033334444"
l=[]
for i in range(len(s[0:-4])):
    l.append("*")
for i in range(4):
    l.append(s[-1-i])
str1=''.join(l)
print(str1)