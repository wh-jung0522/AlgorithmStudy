from collections import deque
def solution(play_time, adv_time, logs):

    '''
    Strategy : 
    adv_start_time을 log start time 부터 < 995959 - adv time
    sliding window 

    Step 1. 
    String time -> integer time

    Step 2. pseudo code : Two pointer algorithm
    max time = 0
    
    return max time
    '''
    ## Step 1.
    MAX = str2int(play_time)
    max_view = 0
    ans_time = 0
    adv_time = str2int(adv_time)
    logs = [[str2int(log.split("-")[0]),str2int(log.split("-")[1])] for log in logs]
    view_list = [0] * (MAX+1)
    ## Step 2.
    ## 도함수
    for start_time,end_time in logs:
        view_list[start_time] += 1
        view_list[end_time] -= 1

    ## 함수
    for i in range(1,MAX+1):
        view_list[i] = view_list[i]+view_list[i-1]

    ## 누적 합
    for i in range(1,MAX+1):
        view_list[i] = view_list[i]+view_list[i-1]
    

    for start_time in range(MAX-adv_time+1):
        ## start time  0,1,2,... MAX-adv_time
        ## end time adv_time, ... MAX
        end_time = start_time + adv_time
        temp_view = view_list[end_time] - view_list[start_time]
        if temp_view > max_view:
            max_view = temp_view
            ans_time = start_time
            if ans_time != 0:
                ans_time += 1
    return int2str(ans_time)

def str2int(strtime:str):
    hh,mm,ss = strtime.split(":")
    return 3600*int(hh)+60*int(mm)+int(ss)

def int2str(inttime:int):
    hh = inttime//3600
    mm = (inttime%3600)//60
    ss = inttime%60
    return str(hh).zfill(2)+":"+str(mm).zfill(2)+":"+str(ss).zfill(2)


if __name__ == "__main__":
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]
    result = "01:30:59"
    print(solution(play_time, adv_time, logs))
    print(result)
    play_time = "99:59:59"
    adv_time = "25:00:00"
    logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    result = "01:00:00"
    print(solution(play_time, adv_time, logs))
    print(result)
    play_time = "50:00:00"
    adv_time = "50:00:00"
    logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
    result = "00:00:00"
    print(solution(play_time, adv_time, logs))
    print(result)