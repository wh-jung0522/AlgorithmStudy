def solution(n, edge):
    for i in range(n):
        if i == 0:
            next_dist, next_dict = graphsort(edge)
        else:
            if len(next_dict) == 0:
                break
            temp_sol = len(next_dist)
            next_dist, next_dict = next(next_dist,next_dict)
            if len(next_dist) == 0:
                return temp_sol
    return len(next_dist)


def next(before_distance_list:list,dictionary:dict):
    next_distance_list = []
    for node, branchs in dictionary.items():
        for branch in branchs:
            if branch in before_distance_list:
                dictionary[node].remove(branch)
        if len(dictionary[node])==0:
            next_distance_list.append(node)
    for before_distance_node in before_distance_list:
        if (dictionary.get(before_distance_node) != None):
            next_distance_list += dictionary[before_distance_node]
            del dictionary[before_distance_node]
    for next_node in next_distance_list:
        if dictionary.get(next_node) != None:
            if len(dictionary[next_node]) == 0:
                del dictionary[next_node]
    next_distance_list = list(set(next_distance_list))    
    return next_distance_list, dictionary


def graphsort(graph:list):
    ret_dictionary = {}
    for small_list in graph:
        small_list.sort()
        if ret_dictionary.get(small_list[0]) == None:
            ret_dictionary[small_list[0]] = []
        ret_dictionary[small_list[0]].append(small_list[1])
    ret_first_dist = ret_dictionary[1]
    del ret_dictionary[1]
    return ret_first_dist, ret_dictionary



if __name__ == "__main__":
    # print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]),3)
    # print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
    # print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
    # print(solution(2, [[1, 2]]), 1)
    # print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
    # print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
    print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
    print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
    # print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)