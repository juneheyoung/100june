city = int(input())
road = list(map(int,input().split()))
price = list(map(int,input().split()))
count = 0
road_count = road[0]
price_count = price[0]
for i in range(1,len(price)-1):
    if price[i]>price[i-1]:
        road_count+=road[i]
    else:
        count += price_count*road_count
        price_count = price[i]
        road_count = road[i]
count += price_count*road_count
print(count)