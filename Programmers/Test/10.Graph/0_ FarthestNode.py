INF = int(10e9)

## Floyd Warshall -> Fail ##
def solution(n, edge):
    maximum_distance = 0
    count = 0
    ## Step1. initialize with edge
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for node1,node2 in edge:
        graph[node1][node2] = 1
        graph[node2][node1] = 1
    ## Step2. floyd
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i==j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j],(graph[i][k]+graph[k][j]))
    # Step3. find maximum
    for i in graph[1]:
        if i > maximum_distance and i != INF:
            maximum_distance = i
            count = 1
        elif i == maximum_distance:
            count += 1
        else:
            continue
    return count

## Dijkstra -> 이유 : start node가 정해져 있으니까
def solution(n, edge):
    ## Step0. make graph
    graph = [[] for _ in range(0,n+1)]
    for node1,node2 in edge:
        ## 주의 : 양방향 그래프이기 때문에, 전부 더해줘야함.
        # min_node = min(node1,node2)
        # max_node = max(node1,node2)
        # graph[min_node].append(max_node)
        graph[node1].append(node2)
        graph[node2].append(node1)
    maximum_distance = 0
    count = 0
    ## Step1. initialize with edge
    distance_list = [INF] * (n+1)
    import heapq
    ## Step2. update distance list using edge
    queue = []
    distance_list[1] = 0
    heapq.heappush(queue,(distance_list[1],1))
    while queue:
        distance_from_start, now_node = heapq.heappop(queue)
        ## Step2-1. 이미 업데이트가 된 경우 처리 안함
        if distance_from_start > distance_list[now_node]:
            continue
        ## Step2-2 업데이트가 필요한 경우 (현재노드를 경유하는게 더 빠른 경우)
        for linked_node in graph[now_node]:
            cost = distance_from_start+1
            if cost < distance_list[linked_node]:
                distance_list[linked_node] = cost
                heapq.heappush(queue,(cost,linked_node))
    

    for i in range(0,n+1):
        if i == 0 or distance_list[i] == INF:
            continue
        if distance_list[i] > maximum_distance:
            count = 1
            maximum_distance = distance_list[i]
        elif distance_list[i] == maximum_distance:
            count += 1
        else:
            continue

    return count





if __name__ == "__main__":
    print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]),3)
    print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
    print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
    print(solution(2, [[1, 2]]), 1)
    print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
    print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
    print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
    print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
    print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)