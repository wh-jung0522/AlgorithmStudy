import heapq
'''
최소 신장 트리 - kruskal algorithm
'''
def solution(n, costs):
    answer = 0
    min_cost_union = []
    root_node_list = [i for i in range(n)]
    list_set = set()
    for union in costs:
        node1,node2,cost = union
        heapq.heappush(min_cost_union, (cost,node1,node2))
        
    while min_cost_union:
        cost,node1,node2 = heapq.heappop(min_cost_union)
        root1 = find_root(node1,root_node_list)
        root2 = find_root(node2,root_node_list)
        if root1 != root2:
            if root1 < root2:
                root_node_list[root2] = root1
            else:
                root_node_list[root1] = root2
            answer += cost
            list_set.add(node1)
            list_set.add(node2)

    return answer

def find_root(n,root_node_list):
    if root_node_list[n] != n:
        root_node_list[n] = find_root(root_node_list[n],root_node_list)
    return root_node_list[n]