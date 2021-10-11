def solution(stones, k):
    end_num = max(stones)
    start_num = 0
    answer = 0
    while end_num >= start_num:
        mid_num = (start_num+end_num)//2
        if mid_num == start_num:
            answer = end_num ## solution([2], 1), result : 2
            break
        conti_count = 0
        avilable = True
        for stone in stones:
            if stone - mid_num <= 0:
                conti_count += 1
            else:
                conti_count = 0
            if conti_count >= k: ## 징검다리 못건넘 mid num 줄여야함.
                avilable = False
                break
        if avilable: ## 징검다리 건널 수 있음, num 증가
            start_num = mid_num
        else: ## 징검다리 못 건넘, num 감소
            answer = mid_num
            end_num = mid_num
    return answer

    
print(solution([2], 1),2)
