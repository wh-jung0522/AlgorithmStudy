def solution(n:int, lost:list, reserve:list):
    lost = sorted(lost)
    reserve = sorted(reserve)
    lost_len = len(lost)
    lost_save = [element for element in lost]
    reserve_len = len(reserve)


    for i in range(lost_len):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost_save.remove(lost[i])

    ## lost에서 작은것 부터 빼기
    lost_len = len(lost_save)
    reserve_len = len(reserve)
    answer = n-lost_len
    for i in range(reserve_len):
        if (reserve[i]-1) in lost_save:
            lost_save.remove(reserve[i]-1)
            answer += 1
        elif reserve[i] in lost_save:
            lost_save.remove(reserve[i])
            answer += 1
        elif (reserve[i]+1) in lost_save:
            lost_save.remove(reserve[i]+1)
            answer += 1
    return answer

if __name__ == '__main__':
    # print(solution(5, [2, 4], [1, 3, 5]), 5)
    # print(solution(5, [2, 4], [3]), 4)
    # print(solution(7, [1, 2, 3, 4, 5, 6, 7], [1, 2, 3]), 3)
    # print(solution(4, [3, 1], [2, 4]),4)
    # print(solution(5, [2, 3, 4], [1, 2, 3]), 4)
    print(solution(5, [1, 2, 3], [2, 3, 4]), 4)