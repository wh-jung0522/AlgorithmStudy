def solution(play_time, adv_time, logs):

    '''
    Strategy : 
    adv_start_time을 log start time 부터 < 995959 - adv time
    sliding window 

    Step 1. 
    String time -> integer time

    Step 2. pseudo code
    max time = 0
    loop log ## start time change
        adv start time = log start time
        temp time = 0
        loop log ## start time ~ log time  cal
            if log start <= adv start time <= log end
                temp time += log end - adv start time
        max time = max(max time, temp time)
    return max time
    '''
    ## Step 1.
    MAX = str2int(play_time)
    nadv_time = str2int(adv_time)
    nlogs = [[str2int(log.split("-")[0]),str2int(log.split("-")[1])] for log in logs]
    nlogs = sorted(nlogs)
    ## Step 2.
    max_time = 0
    ans_time = 0
    for nlog_start, nlog_end in nlogs:
        if nlog_start + nadv_time > MAX:
            nadv_start = MAX - nadv_time
            nadv_end = MAX
        else: 
            nadv_start = nlog_start
            nadv_end = nlog_start + nadv_time
        temp_time = 0
        for log_start, log_end in nlogs:
            if log_end < nadv_start:
                continue
            if log_start > nadv_end:
                break
            ## case 1. log start -> adv start
            if log_start <= nadv_start:
                ## case 1-1 log end -> adv end
                if log_end <= nadv_end:
                    add_time = log_end-nadv_start
                ## case 1-2 adv end -> log end
                else:
                    add_time = nadv_end - nadv_start
            ## case 2. adv start -> log start
            else:
                ## case 2-1 log end -> adv end
                if log_end <= nadv_end:
                    add_time = log_end-log_start
                ## case 2-2 adv end -> log end
                else:
                    add_time = nadv_end-log_start
            temp_time += add_time
        if max_time < temp_time:
            max_time = temp_time
            ans_time = nadv_start
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
    # play_time = "99:59:59"
    # adv_time = "25:00:00"
    # logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    # result = "01:00:00"
    # print(solution(play_time, adv_time, logs))
    # print(result)
    # play_time = "50:00:00"
    # adv_time = "50:00:00"
    # logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]
    # result = "00:00:00"
    # print(solution(play_time, adv_time, logs))
    # print(result)