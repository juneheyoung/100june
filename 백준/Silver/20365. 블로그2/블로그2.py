N = int(input())
s = input()
count = 0
while s!='':
    if s[0]=='B':
        s = s.lstrip('B')
        s = s.rstrip('B')
        count+=1
    else:
        s = s.lstrip('R')
        s = s.rstrip('R')
        count +=1
print(count)
