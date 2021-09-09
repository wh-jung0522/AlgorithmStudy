''' BFS DFS '''
from collections import deque
INF = 999999

def recurrent_example(index=0):
    if index==10:
        return
    print(index)
    index+=1
    recurrent_example(index)

def factorial(index):
    if index <1:
        return 1
    return index*factorial(index-1)

class Graph():
    def __init__(self, graph = [], MatrixType = False) -> None:
        self.isMatrix = MatrixType
        self.graph = graph
    def toAdjMatrix(graph_list:list):
        AdjMatrix = []
        for i in range(len(graph_list)):
            temp_Adjacency = []
            for j in range(len(graph_list)):
                if i == j:
                    temp_Adjacency.append(0)
                else:
                    match = False
                    for node, edge in graph_list[i]:
                        if j == node:
                            match = True
                            temp_Adjacency.append(edge)
                    if not match:
                        temp_Adjacency.append(INF)    
            AdjMatrix.append(temp_Adjacency)
        return AdjMatrix
    def toAdjList(graph_Matrix:list):
        AdjList = []
        for i in range(len(graph_Matrix)):
            temp_Adjacency = []
            for j in range(len(graph_Matrix)):
                if (i != j and graph_Matrix[i][j] <INF ):
                    temp_Adjacency.append((j,graph_Matrix[i][j]))
            AdjList.append(temp_Adjacency)
        return AdjList
    
    ''' DFS를 사용하기 위해서는 그래프와, 방문 리스트, 현재 노드 사용해서 재귀함수 호출'''
    def DFS(self,graph_list,node_index,visited_list):
        visited_list[node_index] = True ## 방문
        print(node_index,end=" ")
        for i,length in graph_list[node_index]:
            if not visited_list[i]:
                self.DFS(graph_list,i,visited_list)

    ''' BFS를 사용하기 위해서는 Queue를 사용'''
    def BFS(self,graph_list,node_index,visited_list):
        visited_list[node_index] = True
        print(node_index,end=" ")
        queue = deque([node_index]) ## 방문한 위치
        while queue: ## queue가 있으면 반복
            '''현재 node는 뺀 이후 현재 node와 연결되어있고, visit하지 않은 node는 queue에 추가'''
            node_index = queue.popleft()
            for next_node, length in graph_list[node_index]:
                if not visited_list[next_node]:
                    queue.append(next_node)
                    visited_list[next_node] = True ## 한번에 방문
                    print(next_node, end= " ")
if __name__ == "__main__":
    Matrix_Graph = [
        [0,7,5],
        [7,0,INF],
        [5,INF,0]
    ]
    List_Graph = [
        [(1,7),(2,5)],
        [(0,7)],
        [(0,5)]
    ]
    # myListGraph = Graph.toAdjList(Matrix_Graph)
    # myMatrixGraph = Graph.toAdjMatrix(List_Graph)
    # print(Matrix_Graph)
    # print(myMatrixGraph)
    # print(List_Graph)
    # print(myListGraph)
    myGraph = Graph()
    graph_list = [
        [],
        [(2,1),(3,1),(8,1)],
        [(1,1),(7,1)],
        [(1,1),(4,1),(5,1)],
        [(3,1),(5,1)],
        [(3,1),(4,1)],
        [(7,1)],
        [(2,1),(6,1),(8,1)],
        [(1,1),(7,1)]
    ]
    visit_list = [False]*9
    myGraph.DFS(graph_list,1,visit_list)
    print("")
    visit_list = [False]*9
    myGraph.BFS(graph_list,1,visit_list)
    # recurrent_example()
    # print(factorial(10))