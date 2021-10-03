import heapq
INF = int(1e9)
def solution(n, s, a, b, fares):
    graph = make_graph(fares,n)
    s_to_all = fast_dijkstra_from_start(graph,n,s)
    ## s - a - b vs s - b - a vs s-a + s-b
    answer = INF
    for i in range(1,n+1):
        s_to_i = s_to_all[i]
        i_to_all = fast_dijkstra_from_start(graph,n,i)
        i_to_a = i_to_all[a]
        i_to_b = i_to_all[b]
        answer = min(answer,(s_to_i+i_to_a+i_to_b))
    return answer

    '''
        플루이드 워셜 N^3
        효율성 테스트가 있기때문에, 다익스트라 *2 가 더 빠를 것
        S-all , A-all
        Step 1. to graph
        Step 2. Dijkstra start -> stop index , stop index -> a or b
    '''

def make_graph(fares, node_num):
    graph = [[] for i in range(node_num+1)]
    for node1, node2, length in fares:
        graph[node1].append([length,node2])
        graph[node2].append([length,node1])
    return graph

def fast_dijkstra_from_start(graph,node_num,start_node):
    distance_list = [INF] * (node_num+1)
    distance_list[start_node] = 0
    queue = []
    heapq.heappush(queue,(0,start_node))
    while queue:
        node_distance,now_node = heapq.heappop(queue)
        ## now node 까지 거리가 이미 더 작은 경우에는 pass
        if distance_list[now_node] < node_distance:
            continue
        ## now node 까지 거리가 update 되었을 경우에는 연결된 모든 거리를 update
        for end_distance,end_node in graph[now_node]:
            cost = node_distance + end_distance
            ## now node를 거쳐서 end_node로 가는 경우가 더 작은 경우 update list에 추가
            if cost < distance_list[end_node]:
                distance_list[end_node] = cost
                heapq.heappush(queue,(cost,end_node))
    return distance_list

    







if __name__ == "__main__":
    n=6
    s=4
    a=6
    b=2
    fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    result=82
    print(solution(n, s, a, b, fares),result)
    n=7
    s=3
    a=4
    b=1
    fares=[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    result=14
    print(solution(n, s, a, b, fares),result)
    n=6
    s=4
    a=5
    b=6
    fares=[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]
    result=18
    print(solution(n, s, a, b, fares),result)
