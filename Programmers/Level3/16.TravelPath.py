import heapq
import copy
def solution(tickets):
    answer = []
    graph = make_graph(tickets)
    now_queue = ['ICN']
    now_node = 'ICN'
    total_tickets = len(tickets)
    total_route = total_tickets+1
    answer = find_route(now_queue,now_node,graph,total_route)
    
    return answer

def make_graph(tickets):
    graph_dict = {}
    for source_node, drain_node in tickets:
        if graph_dict.get(source_node) == None:
            graph_dict[source_node] = [drain_node]
        else:
            heapq.heappush(graph_dict[source_node],drain_node)
        if graph_dict.get(drain_node)==None:
            graph_dict[drain_node] = []
    return graph_dict

def find_route(now_queue:list, now_node, graph:dict, total_route_length):
    if len(graph[now_node]) == 0:
        if total_route_length == len(now_queue):
            return now_queue
        else:
            return []
    for next_node in graph[now_node]:
        next_graph = copy.deepcopy(graph)
        next_graph[now_node].remove(next_node)
        next_queue = copy.deepcopy(now_queue)
        next_queue.append(next_node)
        temp_queue = find_route(next_queue,next_node,next_graph,total_route_length)
        if len(temp_queue) == total_route_length:
            return temp_queue
    return now_queue


if __name__ == "__main__":
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    result = ["ICN", "JFK", "HND", "IAD"]
    print(solution(tickets))
    print(result)
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    result = ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    print(solution(tickets))
    print(result)
    tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "BOO"], ["BOO", "AOO"], ["BOO", "FOO"], ["FOO", "COO"], ["COO", "ZOO"]]
    result = ["ICN", "AOO", "BOO", "AOO", "BOO", "FOO", "COO", "ZOO"]
    print(solution(tickets))
    print(result)
    tickets = [["ICN", "AOO"], ["AOO", "BOO"], ["AOO", "COO"], ["COO", "AOO"], ["BOO", "ZOO"]]
    result = ["ICN", "AOO", "COO", "AOO", "BOO", "ZOO"]
    print(solution(tickets))
    print(result)
    tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "DOO"], ["DOO", "COO"], ["BOO", "DOO"], ["DOO", "BOO"], ["BOO", "ICN"], ["COO", "BOO"]]
    result =  ["ICN", "BOO", "DOO", "BOO", "ICN", "COO", "DOO", "COO", "BOO"]
    print(solution(tickets))
    print(result)
    tickets =  [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
    result = ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
    print(solution(tickets))
    print(result)
    tickets = [["ICN", "AOO"], ["ICN", "AOO"], ["AOO", "ICN"], ["AOO", "COO"]]
    result = ["ICN", "AOO", "ICN", "AOO", "COO"]
    print(solution(tickets))
    print(result)
    tickets = [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]
    result = ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
    print(solution(tickets))
    print(result)
    tickets = [["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]]
    result = ['ICN', 'BOO', 'DOO', 'BOO', 'ICN', 'COO', 'DOO', 'COO', 'BOO']
    print(solution(tickets))
    print(result)
    tickets = [["ICN", "BBB"],["ICN", "CCC"],["BBB", "CCC"],["CCC", "BBB"],["CCC", "ICN"]]
    result = ["ICN", "BBB", "CCC", "ICN", "CCC", "BBB"]
    print(solution(tickets))
    print(result)
    tickets = [['ICN', 'A'], ['A', 'B'], ['A', 'C'], ['C' , 'A'], ['B','D']]
    result = ['ICN', 'A', 'C', 'A', 'B','D']
    print(solution(tickets))
    print(result)