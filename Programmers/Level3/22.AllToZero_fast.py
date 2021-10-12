import sys
import copy
sys.setrecursionlimit(300000)
def solution(a, edges):
    if sum(a) != 0:
        return -1
    len_a = len(a)
    graph = [[] for _ in range(len_a)]
    for edge in edges: ## O(E)
        node1, node2 = edge
        graph[node1].append(node2)
        graph[node2].append(node1)
    visited_list = [False for _ in range(len_a)]

    return DFS_fast(graph,0,a,visited_list)[1]


def DFS_fast(graph, start_node, weight, visited_list):
    return_sum = weight[start_node]
    return_count = 0
    visited_list[start_node] = True
    
    for next_node in graph[start_node]:
        if visited_list[next_node] == False:
            next_sum, next_count = DFS_fast(graph,next_node,weight,visited_list)
            return_sum += next_sum
            return_count += next_count
    return_count += abs(return_sum)
    return return_sum, return_count



if __name__ == "__main__":
    a = [-5,0,2,1,2]
    edges = [[0,1],[3,4],[2,3],[0,3]]
    result = 9
    print(solution(a,edges), result)