def solution(n, times):
    sorted_times = sorted(times)
    low = 0
    high = sorted_times[-1] * n
    while low != high:
        canProcess = 0
        mid = (low + high)//2 ## 버림이기 때문에
        for time in sorted_times:
            canProcess += mid//time
        if canProcess >= n:
            high = mid
        else:
            low = mid
            ## mid 가 항상 작을 수도있음
            if low == (high-1):
                low = high

    return low


'''
    책보고 해볼 것
    Step 1. time sort
    Step 2. total maximum time 과 total minimum time을 잡는다.
    Step 3. 그 total 중간값을 잡았을 때, 중간값 시간동안 처리할 수 있는 사람수를 계산한다.
    Step 4. 중간값 시간에 처리할 수 있는 사람수가 실제 사람수보다 많으면, high time을 줄여본다.
            반대라면, low 시간을 늘려본다.

'''

if __name__ == "__main__":
    print(solution(6,[10,7]),28)