def solution(s):
    answer = []
    for element in s:
        answer.append(processing(element))
    return answer

def processing(processed_string):
    '''
        sliding window 
        find prev '1'string start index, next '0'string end index,
    '''
    stack = []
    count_110 = 0
    for i in processed_string:
        stack.append(i)
        if len(stack) >= 3 and stack[-3:] == ['1','1','0']:
            del stack[-3:]
            count_110 += 1

    start_index = -1
    for i in range(len(stack)):
        if stack[i] == '0':
            start_index = i ## 마지막으로 나오는 0 이후
    if start_index == -1: ## 앞이 전부 1인 경우
        processed_string = '110'*count_110 + ''.join(stack)
    else:
        processed_string = ''.join(stack[:start_index+1]) + '110'*count_110 + ''.join(stack[start_index+1:])
    return processed_string


if __name__ == "__main__":
    s = ["0111111010"]
    print(solution(s))
    result = ["0110110111"]
    print(result)