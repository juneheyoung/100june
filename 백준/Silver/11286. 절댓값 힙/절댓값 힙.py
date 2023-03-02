import sys
input = sys.stdin.readline
import heapq
N = int(input())
stack = []
for i in range(N):
    x = int(input())
    if x !=0:
        heapq.heappush(stack,(abs(x),x))
    else:
        if not stack:
            print(0)
        else:
            print(heapq.heappop(stack)[1])     

