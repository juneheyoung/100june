s = input()
temp = ''
lst = []
for i in s:
    if i =='+':
        lst.append(temp)
        temp = ''
        lst.append(i)
    elif i =='-':
        lst.append(temp)
        temp =''
        lst.append(i)
    else:
        temp = temp+i
    
if temp!='':
    lst.append(temp)
temp = 0
ans = 0
while lst:
    x = lst.pop()
    if x  =='+':
        continue
    elif x =='-':
        ans -= temp
        temp = 0
    else:
        temp += int(x)
if temp!=0:
    ans+=temp
print(ans)