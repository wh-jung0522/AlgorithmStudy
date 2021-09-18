def solution(numbers, hand):
    answer = ''
    now_right_position = (3,2)
    now_left_position = (3,0)
    for number in numbers:
        next_right_position, next_left_position , isRight = next_position(hand,number,now_right_position,now_left_position)
        if isRight:
            answer+="R"
        else:
            answer+="L"
        now_right_position = next_right_position
        now_left_position = next_left_position
    return answer


'''
    1 : (0,0), 2 : (0,1), 3 : (0,2)
    4 : (1,0), 5 : (1,1), 6 : (1,2)
    7 : (2,0), 8 : (2,1), 9 : (2,2)
    * : (3,0), 0 : (3,1), # : (3,2)
'''

def next_position(hand, next_number, now_right_position, now_left_position):
    if next_number == 0:
        next_number = 11
    isRight = True
    next_position = ((next_number-1)//3 , (next_number-1)%3)
    ## if not middle sides
    if next_number in [3,6,9]:
        return next_position, now_left_position, isRight
    elif next_number in [1,4,7]:
        isRight = False
        return now_right_position, next_position, isRight
    ## if middle sides
    else:
        right_distance = abs(now_right_position[0]-next_position[0]) + abs(now_right_position[1]-next_position[1])
        left_distance = abs(now_left_position[0]-next_position[0]) + abs(now_left_position[1]-next_position[1])
        next_right_position = now_right_position
        next_left_position = now_left_position 
        if right_distance < left_distance:
            next_right_position = next_position
        elif right_distance > left_distance:
            next_left_position = next_position 
            isRight = False
        else:
            if hand == "right":
                next_right_position = next_position
            else:
                next_left_position = next_position
                isRight = False
        return next_right_position, next_left_position , isRight


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],'right'),"LRLLLRLLRRL")