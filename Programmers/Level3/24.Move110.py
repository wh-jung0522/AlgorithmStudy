def solution(s):
    answer = []
    for element in s:
        answer.append(processing(element))
    return answer

def processing(element):
    processed_string = element
    index=find_next_index(processed_string)
    while -1 != index:
        break_index = index-1
        for i in range(index-1,-1,-1):
            break_index = i
            if processed_string[break_index] == '1':
                break
        processed_string = processed_string[0:break_index] + '110'+ processed_string[break_index:index] +processed_string[index+3:]
        index=find_next_index(processed_string)
    return processed_string

def find_next_index(processed_string):
    index = processed_string.find("110")
    next_index = index
    index_list = []
    while -1 != next_index:
        index_list.append(index)
        next_index = processed_string[index+3:].find('110')
        index = index+3 + next_index
    for temp_index in index_list:
        if temp_index != 0:
            if processed_string[temp_index-1] == '1':
                return temp_index
        if temp_index != len(processed_string)-3:
            if processed_string[temp_index+3] == '0':
                return temp_index
    return -1

if __name__ == "__main__":
    s = ["0111111010"]
    print(solution(s))
    result = ["0110110111"]
    print(result)