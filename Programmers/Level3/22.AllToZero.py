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
    _, minimum_result = DFS(graph,0, a)
    return minimum_result

def DFS(graph,start_node,weight):
    return_sum = weight[start_node]
    return_count = 0
    if len(graph[start_node]) == 0:
        return return_sum, return_count
    for next_node in graph[start_node]:
        temp_graph = copy.deepcopy(graph)
        temp_graph[next_node].remove(start_node)
        temp_sum, temp_count = DFS(temp_graph, next_node, weight)
        if temp_sum == 0:
            return_count += temp_count
        else:
            return_count += temp_count + abs(temp_sum)
            return_sum += temp_sum
    return return_sum, return_count




if __name__ == "__main__":
    a = [-5,0,2,1,2]
    edges = [[0,1],[3,4],[2,3],[0,3]]
    result = 9
    print(solution(a,edges), result)