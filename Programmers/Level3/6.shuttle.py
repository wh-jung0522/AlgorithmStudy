import heapq
def solution(n, t, m, timetable):
    bus_start_time = 540 ## 9:00
    integertime_heap = []
    for strtime in timetable:
        heapq.heappush(integertime_heap,integertime(strtime))
    
    for nth_bus in range(n):
        bus_stop_time = t*nth_bus + bus_start_time
        crew_count = 0
        while len(integertime_heap)!=0 and integertime_heap[0] <= bus_stop_time :
            next_crew = heapq.heappop(integertime_heap)
            crew_count += 1
            if crew_count == m:
                break
    # next_crew ## 마지막으로 탑승한 승객
    # bus_stop_time ## 마지막 출발 버스
    # integertime_heap[0] ## 탑승하지 못한 첫 승객
    # crew_count ## 마지막 버스 탑승 승객 수
    if crew_count < m: ## 마지막 버스가 빈 공간이 있을 경우
        intanswer = bus_stop_time
    else: ## 마지막 버스가 꽉 찬 경우
        intanswer = next_crew-1

    answer = str(intanswer//60).zfill(2) + ":"+str(intanswer%60).zfill(2)
    return answer

def integertime(strtime):
    hour,minuate = strtime.split(":")
    return 60*int(hour) + int(minuate)

if __name__ == "__main__":
    # n = 1
    # t = 1
    # m = 5
    # timetable = ["08:00", "08:01", "08:02", "08:03"]
    # ans = "09:00"
    n = 2
    t = 10
    m = 2
    timetable = ["09:10", "09:09", "08:00"]
    ans = "09:09"


    print(solution(n,t,m,timetable),ans)