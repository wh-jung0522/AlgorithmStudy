import heapq
def solution(scoville, K):
    scoville_heap = heap_sort(scoville)
    answer = 0
    while(True):
        a = heapq.heappop(scoville_heap)
        if(a>=K):
            break
        if (len(scoville_heap)==0):
            answer = -1
            break
        b = heapq.heappop(scoville_heap)
        c = a+(b*2)
        heapq.heappush(scoville_heap,c)
        answer += 1

    return answer

def heap_sort(Inlist):
    temp_heap = []
    for component in Inlist:
        heapq.heappush(temp_heap,component)

    return temp_heap

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    sol = solution(scoville,K)
    print(sol)