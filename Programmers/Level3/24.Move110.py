def solution(s):
    answer = []
    for element in s:
        answer.append(processing(element))
    return answer

def processing(element):
    processed_string = element
    while can_process(processed_string):
        index = processed_string.find("110")
        temp_string = ''
        break_index = index-1
        for i in range(index-1,-1,-1):
            break_index = i
            if processed_string[i] == '0':
                break
        processed_string = processed_string[0:break_index+1] + '110'+ processed_string[break_index+1:index] +processed_string[index+3:]
    return processed_string

def can_process(processed_string):
    processed_list = processed_string.split("110")
    if len(processed_list[0]) ==0 or (len(processed_list[0]) != 0 and processed_list[0][-1] == '0'):
        if len(processed_list[-1]) == 0 or (len(processed_list[-1]) != 0 and processed_list[-1][0] == '1'):
            return False
    return True

if __name__ == "__main__":
    s = ["0111111010"]
    print(solution(s))
    result = ["0110110111"]
    print(result)