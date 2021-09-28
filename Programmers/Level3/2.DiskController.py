import heapq
def solution(jobs):
    time_sum = 0
    total_jobs = len(jobs)
    nowjobs_queue = []
    jobs = sorted(jobs)
    request_time, job_time = jobs.pop(0)
    heapq.heappush(nowjobs_queue,(job_time, request_time))
    now_time = request_time
    while nowjobs_queue:
        inprocess = heapq.heappop(nowjobs_queue)
        for i in range(inprocess[0]):
            while len(jobs)!=0 and now_time == jobs[0][0]:
                request_time, job_time = jobs.pop(0)
                heapq.heappush(nowjobs_queue,(job_time, request_time))
            now_time += 1
        time_sum += (now_time- inprocess[1])
        while len(nowjobs_queue) == 0 and len(jobs) != 0:
            request_time, job_time = jobs.pop(0)
            heapq.heappush(nowjobs_queue,(job_time, request_time))
            now_time = request_time
    
    answer = time_sum//total_jobs
    return answer

if __name__ =="__main__":
    # print(solution([[0, 3], [1, 9], [2, 6]]),9)
    # print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 74)
    # print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]), 72)
    # print(solution([[0, 3], [0, 2], [1, 9], [2, 6]]), 8)
    # print(solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]), 13)
    # print(solution([[0, 3], [4, 6]]), 4)
    # print(solution([[0, 3], [1, 9], [500, 6]]), 6)
    # print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]), 13)
    # print(solution([[0, 5], [1, 4], [6, 1], [7, 1]]), 5)

    print(solution([[0, 3], [4, 4], [5, 3], [4, 1]]), 4)