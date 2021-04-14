def solution(progresses, speeds):
    ## TODO: 1. Calculate each task spend time
    ##       2. Compare Time list
    spend_time_list = cal_spend_time_list(progresses, speeds)
    return spend_time_list2release_list(spend_time_list)

def cal_spend_time_list(progresses, speeds):
    spend_time_list = []
    for i in range(len(speeds)):
        spend_time_list.append(cal_spend_time_each_task(progresses[i],speeds[i]))
    return spend_time_list

def cal_spend_time_each_task(progress, speed):
    if((100-progress)%speed==0):
        return (int)((100-progress)/speed)
    else:
        return ((int)((100-progress)/speed))+1

def spend_time_list2release_list(spend_time_list):
    release_list = []
    while(True):
        release_order = 1
        if (len(spend_time_list)==0):
            break
        task_day = spend_time_list[0]
        while(True):
            if(release_order >= len(spend_time_list)):
                release_list.append(release_order)
                for j in range(release_order):
                    spend_time_list.pop(0)
                break
            if(spend_time_list[release_order]>task_day):
                release_list.append(release_order)
                for j in range(release_order):
                    spend_time_list.pop(0)
                break
            else:
                release_order += 1
    return release_list

if __name__ == '__main__':
    progresses = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    sol = solution(progresses,speeds)
    print(sol)