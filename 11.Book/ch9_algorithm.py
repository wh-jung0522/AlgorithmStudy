'''Route Algorithm'''
import heapq
INF = int(1e9)
class route_algorithm():
    def __init__(self, graph, total_node) -> None:
        self.total_node = total_node
        self.total_edge = len(graph)
        self.graph = [[] for i in range(self.total_node+1)]
        for i in range(self.total_edge): ## list graph -> adjacent 
            if i == 0:
                continue
            self.graph[graph[i][0]].append((graph[i][1],graph[i][2]))
        
        self.distance_matrix = [[INF]*(self.total_node+1) for i in range(self.total_node+1)]
        for i in range(self.total_node+1):
            for j in range(self.total_node+1):
                if i == 0 or j == 0:
                    continue
                if i == j:
                    self.distance_matrix[i][j] = 0
                else:
                    for end_node, end_distance in self.graph[i]:
                        self.distance_matrix[i][end_node] = end_distance

        '''
        graph 예시 1. Adjacent list Node
        [
            []
            [(2,2),(3,5),(4,1)], ## 1번노드, 2번노드로 가는데 비용이 2이다. ## start node list [(end,cost),(end,cost)]
            [(3,3),(4,2)], ## 2번노드
            [(2,3),(6,5)], ## 3번노드
            [(3,3),(5,1)],
            [(3,1),(6,2)],
            [] ## 6번노드
        ]

        graph 예시 2. list Node
        [
            ## [start, end, cost]
            [1], ## ??
            [1,2,2], ## 1번노드에서 2번노드로 가는데 비용이 2이다.
            [1,3,5],
            [1,4,1],
            [2,3,3],
            [2,4,2],
            [3,2,3],
            [3,6,5],
            [4,3,3],
            [4,5,1],
            [5,3,1],
            [5,6,2]
        ]
        '''
        pass
    def get_smallest_node(self, distance, visited):
        min_value = INF
        index = 0
        for i in range(1,self.total_node):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index
    def dijkstra(self,start_node): ## O(V^2)
        distance = [INF] * (self.total_node+1)
        visited = [False] * (self.total_node+1)
        distance[start_node] = 0
        visited[start_node] = True
        '''loop 한번돌리면 문제점 : 이전상황을 저장 못함. (정렬되었을 때, 1번노드로만 사용가능)'''
        
        '''Step1. Start node 초기화'''
        for end_node, end_distance in self.graph[start_node]:
            distance[end_node] = end_distance
        
        '''Step2. '''
        for i in range(self.total_edge-2): ## O(V)
            now = self.get_smallest_node(distance,visited) ## 방문하지 않은 연결 된 노드 중 가장 거리가 짧은 노드로부터 시작한다.
            visited[now] = True ## 방문처리한다.
            for end_node, end_distance in self.graph[now]: ## 현재 노드가 연결되어있는 간선만 본다. 
                cost = distance[now] + end_distance ## 현재 노드를 거쳐 k[0]으로 가는 비용을 계산한다.
                if cost < distance[end_node]: ## 만약, 현재 노드를 거쳐가는 비용이 더 저렴하다면, 업데이트 한다.
                    distance[end_node] = cost
        return distance
    def fast_dijkstra(self,start_node): ## O (E log V)
        distance = [INF] * (self.total_node+1)
        queue = []
        distance[start_node] = 0
        ## start node로 부터 목적지까지의 거리 queue
        heapq.heappush(queue,(0,start_node)) ## (거리, 목적지)
        while queue: ## queue 가 존재하면
            node_distance, now_node = heapq.heappop(queue) ## 가장 거리가 짧은 node에서 시작
            if distance[now_node] < node_distance: ## 이전에 이미 처리한 distance가 더 짧을 경우 pass
                continue
            ## graph 내용을 토대로 현재 노드와 인접한 노드 처리
            for end_node, end_distance in self.graph[now_node]:
                cost = node_distance + end_distance
                ## 만약 인접한 노드가 거리가 줄었으면, 아직 처리가 덜 되었다는 것이니, queue에 추가함
                if cost < distance[end_node]:
                    distance[end_node] = cost
                    heapq.heappush(queue,(cost,end_node))
        return distance
    def floyd(self): ## O(V^3)
        ## distance matrix initialize
        ## algorithm
        for i in range(self.total_node+1):
            for j in range(self.total_node+1):
                for k in range(self.total_node+1):
                    self.distance_matrix[i][j] = min(self.distance_matrix[i][j],self.distance_matrix[i][k]+self.distance_matrix[k][j])
        return self.distance_matrix

if __name__ == "__main__":
    graph = [
            ## [start, end, cost]
            [1], ## ?? Buffer
            [1,2,2], ## 1번노드에서 2번노드로 가는데 비용이 2이다.
            [1,3,5],
            [1,4,1],
            [2,3,3],
            [2,4,2],
            [3,2,3],
            [3,6,5],
            [4,3,3],
            [4,5,1],
            [5,3,1],
            [5,6,2]
        ]
    total_node = 6
    myRoute = route_algorithm(graph,total_node)
    shortest = myRoute.dijkstra(3)
    shortest_fast = myRoute.fast_dijkstra(3)
    floyd_test = myRoute.floyd()
    print(shortest)
    print(shortest_fast)
    print(floyd_test[3])