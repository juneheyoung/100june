def solution(participant, completion):
    answer = ''
    mydict={}
    for i in completion:
        if mydict.get(i):
            mydict[i]+=1
        else:
            mydict[i]=1
    for i in participant:
        if mydict.get(i) and mydict.get(i)>0:
            mydict[i]-=1
        else:
            return i