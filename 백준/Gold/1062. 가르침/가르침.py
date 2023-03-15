def combination(s,K):
    global subset
    if len(s)==K:
        subset.append(s)
        return s
    else:
        if not s:
            for i in range(1,22):          
                s = alpha[i]  #s + alpha[i]
                combination(s,K)
                s  ='' #s[:-1]
        else:
            x=s[-1]
            for i in range(reverse_alpha[x]+1,22):
                
                s=s+alpha[i]
                combination(s,K)
                s  = s[:-1]

N, K = map(int,input().split())
arr = []
for _ in range(N):
    s = list(input())
    s.sort()
    s=set(s)
    s = s - set(['a','n','t','i','c'])
    ans = ''
    for i in s:
        ans = i + ans
    arr.append(ans)
#print(arr)
alpha = {1:'b' ,2:'d',3:'e',4:'f',5:'g',6:'h',7:'j',8:'k',9:'l',10:'m',11:'o',12:'p',13:'q',14:'r',15:'s',16:'u',17:'v',18:'w',19:'x',20:'y',21:'z'}
reverse_alpha = {v:k for k,v in alpha.items()}
subset=[]
# alpha = ['b','d','e','f','g','h','j','k','l','m','o','p','q','r','s','u','v','w','x','y','z']
if K<5:
    answer=0
    print(answer)
elif K==5:
    answer=0
    for j in arr:
        if not j:
            answer+=1
    print(answer)
else:
    answer =0
    combination('',K-5)
    #print(subset)
    for i in subset:
        count=0
        for j in arr:
            for k in j:
                if k not in i:    ############ 어떻게 체크할것인지 
                    break
            else:
                count+=1
        if count>answer:
            answer = count

    print(answer)
