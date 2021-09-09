class graph():
    def __init__(self) -> None:
        pass

    def find_root(self,root_list,child):
        if root_list[child] != child:
            root_list[child] = self.find_root(root_list,root_list[child])
        return root_list[child]

    def init_with_union(self, union_set, origin_list):
        for node1, node2 in union_set:
            root1 = self.find_root(origin_list,node1)
            root2 = self.find_root(origin_list,node2)
            if root1 < root2:
                union_root = root1
            else:
                union_root = root2
            origin_list[node1] = union_root
            origin_list[node2] = union_root
        return origin_list ## parent list

    def has_cycle(self, union_set, origin_list):
        cycle = False
        for node1, node2 in union_set:
            root1 = self.find_root(origin_list,node1)
            root2 = self.find_root(origin_list,node2)
            if root1 == root2:
                cycle = True
                break
            else:
                if root1 < root2:
                    origin_list[root2] = root1
                else:
                    origin_list[root1] = root2
        return cycle
    
    def kruskal(self,total_node,union_list): ## O(ElogE)
        total_cost = 0
        origin_list = [i for i in range(total_node+1)]
        linked_list = []
        sorted_union_list = []
        import heapq
        for node1,node2,cost in union_list:
            heapq.heappush(sorted_union_list,(cost,node1,node2))
        ## start     
        while sorted_union_list:   
            cost, node1, node2 = heapq.heappop(sorted_union_list)
            root1 = self.find_root(origin_list,node1)
            root2 = self.find_root(origin_list,node2)
            if root1 != root2: ## root 를 적용한다.
                if root1 < root2:
                    origin_list[root2] = root1
                else:
                    origin_list[root1] = root2
                linked_list.append((node1,node2))
                total_cost += cost
        return total_cost , linked_list, origin_list

    def topology(self,total_node,vector_list):
        from collections import deque
        order_list = [0] * (total_node+1)
        topology_graph = [[] for i in range(total_node+1)]
        queue = deque([])
        result = []
        for start_node, end_node in vector_list:
            order_list[end_node] +=1
            topology_graph[start_node].append(end_node)
        start_node = 0
        for i in range(0,total_node+1):
            if i == 0:
                continue
            if(order_list[i]==0):
                start_node = i
                break
        queue.append(start_node)
        while queue:
            ## Step0. now node = pop , append now node
            now_node = queue.popleft()
            result.append(now_node)
            ## Step1. 현재 노드와 연결된 i node의 차수를 줄임.
            for i in topology_graph[now_node]:
                order_list[i] -= 1
                ## Step2. 다음 차수가 0이면, append
                if order_list[i] == 0:
                    queue.append(i)
            
        return result

if __name__ == "__main__":
    myGraph = graph()
    union_set = [
        [1,4],
        [2,3],
        [2,4],
        [5,6]
    ]
    total_node = 6
    # union_set = [
    #     [1,2],
    #     [1,3],
    #     [2,3]
    # ]
    # total_node = 3
    origin_list = [i for i in range(0,total_node+1)]
    
    ## 1. first init parent list 
    parent_list = origin_list.copy()
    parent_list = myGraph.init_with_union(union_set,parent_list) ## O(EV)
    print(parent_list)

    ## 2. find root list
    root_list = parent_list.copy()
    root_list = [myGraph.find_root(root_list,i) for i in range(0,total_node+1)] ## O(E)
    print(root_list)

    ## 3. find cycle
    print(myGraph.has_cycle(union_set,origin_list))

    ## 4. find tree
    kruskal_union_list = [
        [1,2,29],
        [1,5,75],
        [2,3,35],
        [2,6,34],
        [3,4,7],
        [4,6,23],
        [4,7,13],
        [5,6,53],
        [6,7,25]
    ]
    print(myGraph.kruskal(7,kruskal_union_list))
    
    ## 5. 
    vector_list = [
        (1,2),
        (1,5),
        (2,3),
        (2,6),
        (3,4),
        (4,7),
        (5,6),
        (6,4)
    ]
    topo_total_node = 7
    print(myGraph.topology(topo_total_node,vector_list))