from ch9_algorithm import route_algorithm , INF
import heapq
'''가장 빠른 길 찾기 (다익스트라 알고리즘)'''
def ch9_1(graph,total_node,start_node,inter_node,final_node):
    ## floyd algorithm init (total_node < 100)
    route_matrix = [[INF]*(total_node+1) for _ in range(total_node+1)]
    for i in range(1,total_node):
        for j in range(1,total_node):
            if i == 0 or j == 0:
                continue
            if i == j:
                route_matrix[i][j] = 0
            else:
                for k in range(len(graph)):
                    if k == 0:
                        continue
                    first_node, second_node, length = graph[k]
                    route_matrix[first_node][second_node] = length
                    route_matrix[second_node][first_node] = length
    ## floyd start
    for i in range(1,total_node+1):
        for j in range(1,total_node+1):
            for k in range(1,total_node+1):
                route_matrix[i][j] = min(route_matrix[i][j],route_matrix[i][k]+route_matrix[k][j])
    ## answer
    return route_matrix[start_node][inter_node] + route_matrix[inter_node][final_node]
def ch9_2(graph_input,start_node,total_node,total_edge):
    ## Step 1. Graph init
    graph = [[] for i in range(total_node+1)]
    for i in range(total_edge+1):
        if i == 0: continue
        graph[graph_input[i][0]].append((graph_input[i][1],graph_input[i][2]))

    ## Step 2. Fast Dijkstra
    ## Step 2-1. make queue (distance, target_node) , make distance list
    queue = []
    heapq.heappush(queue,(0,start_node))
    distance_list = [INF]*(total_node+1)
    distance_list[start_node] = 0
    ## Step 2-2. if exist queue -> process
    while queue:
        now_distance, now_node = heapq.heappop(queue)
        ## Step 2-3. if shortest list (이미 처리된 거리)가 더 짧으면 패스 
        if now_distance > distance_list[now_node]:
            continue
        ## Step 2-3. 아니면, now_node와 연결된 다른 노드 확인
        for next_node, next_distance in graph[now_node]:
            next_cost = now_distance + next_distance
            ## Step 2-4. 만약 next_node가 now_node를 거쳐 가는게 더 빠르면, update를 위해 queue에 추가
            if distance_list[next_node] > next_cost:
                distance_list[next_node] = next_cost
                heapq.heappush(queue,(next_distance,next_node))
    ## Step 3. counting city & max time 
    count = 0
    max_time = 0
    for i in range(1,total_node+1):
        if i == 0: continue
        if distance_list[i] != INF and i != start_node:
            count += 1
            max_time = max(max_time,distance_list[i])
    
    return count, max_time



if __name__ == "__main__":
    graph_input = [
        [],
        [1,2,4],
        [1,3,2]

    ]
    print(ch9_2(graph_input,1,3,2))
    # graph = [
    #         ## [start, end, cost]
    #         [1], ## ?? Buffer 0 
    #         [1,2,1], ## 1번노드에서 2번노드로 가는데 비용이 2이다.
    #         [1,3,1],
    #         [1,4,1],
    #         [2,4,1],
    #         [3,4,1],
    #         [3,5,1],
    #         [4,5,1]
    #     ]
    # print(ch9_1(graph,5,1,5,4))
