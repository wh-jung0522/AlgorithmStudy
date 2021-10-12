from collections import deque

def solution(routes):
    sort_routes = deque(sorted(routes,key=lambda x: x[1]))
    answer = 0
    while sort_routes:
        index_start, index_end = sort_routes.popleft()
        answer += 1
        while True:
            if len(sort_routes) == 0:
                break
            next_start, next_end = sort_routes[0]
            if next_start <= index_end <= next_end:
                sort_routes.popleft()
            else:
                break

    '''
    Strategy : while routes

        end를 통과하는 route pop

        next first end 를 통과하는 route pop

        if len(routes) == 0:
            break

    '''
    return answer


if __name__ == "__main__":
    routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
    result = 2
    print(solution(routes), result)