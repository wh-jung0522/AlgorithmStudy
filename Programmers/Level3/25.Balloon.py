def solution(a):
    answer = 1
    len_a = len(a)
    left_index = 0
    right_index = len_a-1
    left_min = a[left_index]
    right_min = a[right_index]
    while left_index < right_index:
        if left_min > right_min:
            left_index += 1
            left_value = a[left_index]
            if left_value < left_min:
                answer += 1
                left_min = left_value
        else:
            right_index -= 1
            right_value = a[right_index]
            if right_value < right_min:
                answer += 1
                right_min = right_value

    return answer

if __name__ == "__main__":
    a = [9,-1,-5]
    result = 3
    print(solution(a))
    print(result)
