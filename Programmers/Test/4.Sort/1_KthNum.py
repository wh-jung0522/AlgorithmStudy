def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(sol_each_command(array,command))
    return answer

def sol_each_command(array, command):
        temp_array = array[command[0]-1:command[1]]
        temp_array.sort()
        return temp_array[command[2]-1]


if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]), [5, 6, 3])