def price(x,arr,pay):
    if x==0:
        return 0
    for i in range(len(arr)):
        if x<=arr[i]:
            return pay[i]
    else:
        return 0

T = int(input())
a_arr = [1,3,6,10,15,21]
a_pay = [500,300,200,50,30,10]
b_arr = [1,3,7,15,31]
b_pay = [512,256,128,64,32]

for _ in range(T):
    ans = 0
    a,b = map(int,input().split())
    ans += price(a,a_arr,a_pay)
    ans += price(b,b_arr,b_pay)
    print(ans*10000)