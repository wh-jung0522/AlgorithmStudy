def solution(tickets):
    answer = []
    return answer
'''
사용 기술 : Topology 위상 정렬
Step 1. loop Edge:
            -> Graph = []*Start_node+1
            -> Start_node.append(End_node)
Step 2. queue에 ICN 추가

Step 3. While queue
        now node = queue pop, result에 append
        loop:
            Graph[now_node]에 있는 값 하나씩 뺌.
            빼고나니 0이면 queue에 추가


''' 


if __name__ == "__main__":
    print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]),["ICN", "JFK", "HND", "IAD"])
    print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]),
    ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])