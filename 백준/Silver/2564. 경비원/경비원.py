def func(a,b,x,y):
    ans =0  
    if a == 1:
        if x==3:
            ans += b+y
        elif x ==4:
            ans += N-b+y
        elif x == 2:
            ans += M + min(b+y,2*N-b-y)
        else:#x==1
            ans += abs(b-y)
    elif a ==3:
        if x==4:
            ans +=N+min(y+b,2*M-b-y)
        elif x==1:
            ans += b+y
        elif x==2:
            ans += M-b+y
        else:
            ans+= abs(b-y)
    elif a ==4:
        if x==3:
            ans+= N+min(b+y,2*M-b-y)
        elif x==2:
            ans+=M-b+N-y
        elif x==1:
            ans+=b+N-y
        else:
            ans += abs(b-y)
    else:# a==2
        if x==3:
            ans += M-y+b
        elif x==4:
            ans+=N-b+M-y
        elif x == 1:
            ans += M + min(b+y, 2*N-b-y)
        else:#x==2
            ans += abs(b-y)
    return ans


N , M = map(int,input().split())
store = int(input())
check = []
answer = 0
for tc in range(store):
    a, b = map(int,input().split())
    check.append((a,b))
a, b = map(int,input().split())
for i in check:
    x,y = i
    answer+= func(a,b,x,y)
print(answer)
