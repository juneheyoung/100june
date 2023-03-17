import sys
input = sys.stdin.readline
import heapq
N = int(input())
heap = []
for tc in range(N):
    n = int(input())
    if n==0:
        if heap ==[]:
            print('0')
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,n)
        