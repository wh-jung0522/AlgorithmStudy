def solution(n, edge):
    for i in range(n):
        if i == 0:
            next_dist, next_dict = graphsort(edge)
            if len(next_dict) == 0:
                break
        else:
            if len(next_dict) == 0:
                break
            next_dist, next_dict = next(next_dist,next_dict)

    return len(next_dist)


def next(before_distance_list:list,dictionary:dict):
    next_distance_list = []
    next_dictionary = dictionary.copy()
    for before_distance_node in before_distance_list: 
        for node, link_node_list in next_dictionary.items():
            if before_distance_node in link_node_list:
                next_dictionary[node].remove(before_distance_node)
            else:
                next_distance_list+=next_dictionary[node]
        if len(next_dictionary) ==0:
            break
        else:
            del next_dictionary[before_distance_node]   
    next_distance_list = list(set(next_distance_list))
    return next_distance_list, next_dictionary


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
    print(solution(11, [[1, 2], [1, 3], [2, 4], [2, 5], [3, 5], [3, 6], [4, 8], [4, 9], [5, 9], [5, 10], [6, 10], [6, 11]]), 4)
    # print(solution(4, [[1, 2], [2, 3], [3, 4]]), 1)
    # print(solution(2, [[1, 2]]), 1)
    # print(solution(5, [[4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]), 2)
    # print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4], [3, 4]]), 1)
    # print(solution(4, [[1, 4], [1, 3], [2, 3], [2, 1]]), 3)
    # print(solution(4, [[3, 4], [1, 3], [2, 3], [2, 1]]), 1)
    # print(solution(4, [[4, 3], [1, 3], [2, 3]]), 2)