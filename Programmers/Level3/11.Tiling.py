def slow_solution(n):
    from math import comb
    '''
        Step1. n=1 1
            세로 1개 [1]
        Step2. n=2 2 
            n=1 + n=1 [[1,1],[2]]
        Step3. n=3 3
            n=2 [[1,1,1],[1,2],[2,1]]
        Step4. n=4 5 
            [[1,1,1,1] | 3C1 [1,1,2],[1,2,1],[2,1,1] | 2C2 [2,2]]
        Step5. n=5 8
            [[1,1,1,1,1] | 4C1 [1,1,1,2],[1,1,2,1],[1,2,1,1],[2,1,1,1] | 3C2 [1,2,2],[2,1,2],[2,2,1]]
        Step6. n=6 13
            [[1,1,1,1,1,1] | 5C1 [1,1,1,1,2]. [1,1,1,2,1], [1,1,2,1,1], [1,2,1,1,1], [2,1,1,1,1] | 4C2 [1,1,2,2],[1,2,1,2],[2,1,1,2], [1,2,2,1],[2,1,2,1],[2,2,1,1]] | 3C3 [2,2,2]]
        Step7. n=7 21
            fibonacci 수열
    '''
    answer = 1
    i = 1
    while n-i >= i:
        answer +=  comb(n-i,i)
        answer = answer%1000000007
        i+=1
    return answer


def fibonacci_recur(n):
    if n <= 1:
        return 1
    else:
        return fibonacci_recur(n-1)+ fibonacci_recur(n-2)


def fibonacci_non_recur(n):
    before_value = 1
    now_value = 1
    for i in range(n+1):
        if i == 0 or i == 1:
            continue
        else:
            before_value, now_value = now_value, before_value + now_value
    return now_value%1000000007

if __name__ == "__main__":
    print(slow_solution(10),fibonacci_non_recur(10))
    print(slow_solution(11),fibonacci_non_recur(11))
    print(slow_solution(12),fibonacci_non_recur(12))
    print(slow_solution(13),fibonacci_non_recur(13))
    print(slow_solution(14),fibonacci_non_recur(14))
