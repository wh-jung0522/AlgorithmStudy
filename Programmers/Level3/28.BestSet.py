def solution(n, s):
    '''
    Step1. 평균값 구하기, 몫이 0보다 크면 일단 그걸로 채워넣기
    Step2. 나머지가 0이 아니면, 나머지 수만큼은 몫 + 1씩

    '''
    answer = []
    avg_num = s//n
    if avg_num == 0:
        return [-1]
    num_of_larger = s%n
    for i in range(n-num_of_larger):
        answer.append(avg_num)

    for i in range(num_of_larger):
        answer.append(avg_num+1)

    return answer

print(solution(2,1))
print([4,4])