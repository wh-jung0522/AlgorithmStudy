from collections import deque
def solution(lines):
    answer = 0
    start_end_queue = []
    for line in lines: # O(L)
        _, end_time, period = line.split(" ")
        end_time= str_to_int_time(end_time)
        period = period_to_time(period)
        start_time = end_time - period +1
        if start_time < 0:
            start_time = 0
        start_end_queue.append((start_time,end_time))
    start_end_queue = deque(start_end_queue) # Not sort!! : end time 기준으로 시작, 끝 정해서 pop 하기 때문에
    
    while start_end_queue:
        start, end = start_end_queue.popleft()
        search_start = end
        search_end = end + 1000
        inprocessing_count = 1
        for next_start, next_end in start_end_queue:
            if next_start < search_end and next_end >= search_start:
                inprocessing_count += 1
        answer = max(answer,inprocessing_count)
    
   
    return answer

def str_to_int_time(hhmmss:str):
    hh,mm,ss_sss = hhmmss.split(":")
    return 3600000*int(hh)+60000*int(mm)+int((1000*float(ss_sss)))

def period_to_time(ss_sec:str):
    return int(1000*float(ss_sec.replace("s","")))
    

if __name__ == "__main__":
    lines = [
    "2016-09-15 20:59:57.421 0.351s", ## 57.07 ~57.421
    "2016-09-15 20:59:58.233 1.181s", ## 57.052 ~ 58.233
    "2016-09-15 20:59:58.299 0.8s", ## 57.499 ~ 58.299
    "2016-09-15 20:59:58.688 1.041s", # 
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
    ]
    print(solution(lines),7)