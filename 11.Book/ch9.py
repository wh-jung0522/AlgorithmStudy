from ch9_algorithm import route_algorithm , INF
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
def ch9_2(graph):
    return

if __name__ == "__main__":
    print(ch9_2())
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
