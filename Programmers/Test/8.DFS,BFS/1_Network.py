## TODO : Root Node의 갯수를 구하라
## Input : computers[i] = i번째 컴퓨터가 연결되어있는 컴퓨터 index list []
''' 
    Step1. parent list 구현
    Step2. root list 구현
    Step3. root 갯수 확인
'''

def solution(n, computers):
    parent_list = [i for i in range(0,n+1)]
    parent_list = make_union(parent_list,computers)
    root_list = []
    for i in range(0,n+1):
        if i == 0:
            continue
        temp_root = find_root(parent_list[i],parent_list)
        if not temp_root in root_list:
            root_list.append(temp_root)

    return len(root_list)

def make_union(parent_list,computers_union):
    for i in range(len(computers_union)):
        for j in range(i+1,len(computers_union)):
            if computers_union[i][j] == 1:
                ## find root_node of i, j
                root1 = find_root(i+1,parent_list)
                root2 = find_root(j+1,parent_list)
                if root1 < root2:
                    parent_list[root2] = root1
                else:
                    parent_list[root1] = root2
    return parent_list

def find_root(node_index, parent_list:list):
    if node_index != parent_list[node_index]:
        parent_list[node_index] = find_root(parent_list[node_index],parent_list)
    return parent_list[node_index]

if __name__ == "__main__":
    print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]),2)
    print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]),1)