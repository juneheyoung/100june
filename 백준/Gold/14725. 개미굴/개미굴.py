import sys
input = sys.stdin.readline
N = int(input())
arr = []
for i in range(N):
    data = list(input().split())
    arr.append(data[1:])

arr.sort()

dash = '--'
answer = []
for i in range(N):
    # 첫 번째는 부모, 자식 노드의 중복이 없으므로 그대로 출력.
    if i == 0:
        for j in range(len(arr[i])):
            answer.append(dash * j + arr[i][j])
    else:
        idx = 0   # 이전의 리스트와 현재 리스트에서 맨 왼쪽부터 겹치는 원소의 개수를 저장.
        for j in range(len(arr[i])):
            # 이전의 리스트의 원소가 없거나, 이전의 리스트와 현재 리스트가 겹치지 않을 때
            if arr[i - 1][j] != arr[i][j] or len(arr[i - 1]) <= j:
                break
            # 겹치는 원소가 존재한다면 해당 원소를 출력할 필요가 없으므로 idx를 조정.
            else:
                idx = j + 1
        for j in range(idx, len(arr[i])):
            answer.append(dash * j + arr[i][j])

for ans in answer:
    print(ans)