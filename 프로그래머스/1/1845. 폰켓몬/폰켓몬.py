def solution(nums):
    answer = 0
    nums.sort()
    n = len(nums)//2
    x = set(nums)
    if len(x) > n:
        return n
    else:
        return len(x)
