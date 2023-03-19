def ispel(n):
    s = str(n)
    l = len(s)
    for i in range(l//2):
        if s[i]!=s[l-i-1]:
            return 0
    return 1
def isprime(n):
    if n==1:
        return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1
N = int(input())
while True:
    if ispel(N)==1:
        if isprime(N)==1:
            answer = N
            break
    N+=1
print(answer)