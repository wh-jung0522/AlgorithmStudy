def solution(priorities, location):
    answer = 0
    while(True):
        que_length = len(priorities)
        if (que_length==0):
            break
        top_priority_location = priorities.index(max(priorities))
        if(top_priority_location > location):
            location = location+que_length-top_priority_location
        elif(top_priority_location < location):
            location = location - top_priority_location
        else:
            answer += 1
            break
        priorities = priorities[top_priority_location:]+priorities[:top_priority_location]
        priorities.pop(0)
        location -= 1
        answer += 1

    return answer


if __name__ == '__main__':
    priorities = [2, 1, 3, 2]
    location = 0
    sol = solution(priorities,location)
    print(sol)