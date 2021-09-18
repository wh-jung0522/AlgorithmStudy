def solution(triangle):
    next_max_list = [0]
    for now_step_list in triangle:
        next_max_list = make_max_list(next_max_list,now_step_list)
    return max(next_max_list)

def make_max_list(before_max_list:list,now_step_list:list):
    now_max_list = []
    for i in range(len(now_step_list)):
        if i==0:
            now_max_list.append(before_max_list[i]+now_step_list[i])
        elif i == (len(now_step_list)-1):
            now_max_list.append(before_max_list[i-1]+now_step_list[i])
        else:
            now_max_list.append(max(before_max_list[i-1]+now_step_list[i],before_max_list[i]+now_step_list[i]))
    return now_max_list

if __name__ == "__main__":
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]),30)