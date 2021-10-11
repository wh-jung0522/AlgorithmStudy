def solution(a, edges):
    if sum(a) != 0:
        return -1
    graph = [ [] for _ in range(len(a))]
    for edge in edges:
        node1, node2 = edge
        graph[node1].append(node2)
        graph[node2].append(node1)




    return answer

def BFS(graph,index,weight):
    for 




    return



if __name__ == "__main__":
    a = [-5,0,2,1,2]
    edges = [[0,1],[3,4],[2,3],[0,3]]
    result = 9
    print(solution(a,edges), result)