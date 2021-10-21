import copy
def solution(n):
    answer = 0
    ## n//2까지는 2배, n//2 +1 까지하기.
    loop_index = n//2
    for x_pos in range(loop_index):
        visit_array = [[False]*n for _ in range(n)]
        answer += 2*validcount(x_pos,0,n,visit_array)
    if n%2 ==1:
        visit_array = [[False]*n for _ in range(n)]
        answer += validcount(loop_index, 0,n,visit_array)
    return answer

def validcount(x_pos,y_pos,remain_queen,visit_array):
    visit_array = make_visit(x_pos,y_pos,visit_array)
    remain_queen -= 1
    if remain_queen == 0:
        return 1
    if y_pos+1 == len(visit_array):
        return 0
    next_visit_count = 0
    for i in range(len(visit_array)):
        if visit_array[y_pos+1][i] == False:
            next_visit_array = copy.deepcopy(visit_array)
            next_visit_count += validcount(i,y_pos+1,remain_queen,next_visit_array)
    return next_visit_count


def make_visit(x_pos,y_pos,visit_array):
    n=len(visit_array)
    visit_array[y_pos][x_pos] = True
    for i in range(len(visit_array)):
        visit_array[y_pos][i] = True
        visit_array[i][x_pos] = True
        if x_pos-i >= 0:
            if y_pos-i >= 0:
                visit_array[y_pos-i][x_pos-i] = True
            if y_pos+i < n:
                visit_array[y_pos+i][x_pos-i] = True
        if x_pos+i < n:
            if y_pos-i >= 0:
                visit_array[y_pos-i][x_pos+i] = True
            if y_pos+i < n:
                visit_array[y_pos+i][x_pos+i] = True
    return visit_array

    '''
        (0,1) == (0,:) ,(:,1) | (1,0), | (1,2), (2,3)
        가로 : n-1, 세로 : n-1 | 좌 대각 | 우 대각 visit처리, 그다음 non visit 추가 ... 한 row를 반복하면 갯수 나옴.
    '''
if __name__ == "__main__":
    # print(solution(1)) # 1
    # print(solution(2)) # 0
    # print(solution(3)) # 0
    # print(solution(4)) # 2
    # print(solution(5)) # 10
    # print(solution(6)) # 4
    print(solution(7)) # 40
    print(solution(8))
    print(solution(9))
    print(solution(10))
    print(solution(11))
    print(solution(12))