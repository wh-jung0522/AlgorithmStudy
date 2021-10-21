from math import factorial as fac
def solution(n, k):
    answer = []
    start_list = [i for i in range(1,n+1)]
    answer = recur_result(answer,start_list,k-1)
    return answer

'''
    0번째, 2!
    1번째, 2!
    ...

    즉, k가 (i-1)*(n-1!) ~ i*(n-1!) 이면, 첫번째 숫자는 i-1번째
    그 다음 나머지 가  ...

'''

def recur_result(answer,remain_list,remain_k):
    remain_n = len(remain_list)
    if remain_n == 0:
        return answer
    for i in range(1,remain_n+1):
        if (i-1)*fac(remain_n-1) <= remain_k < i*fac(remain_n-1):
            remain_k -= (i-1)*fac(remain_n-1)
            answer.append(remain_list.pop(i-1))
            break
    remain_list = sorted(remain_list)
    return recur_result(answer,remain_list,remain_k)


print(solution(3,5))