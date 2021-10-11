from collections import deque
INF = int(1e9)
def solution(board):
    '''
    Strategy : DP, BFS
    head : -1,0,1,2,3
    -1 : start point
    0 : right
    1 : down
    2 : left
    3 : up
    '''
    dx_list = [1,0,-1,0]
    dy_list = [0,1,0,-1]
    
    board_len = len(board)
    cost_arr = [[[INF for _ in range(4)]for _ in range(board_len)] for _ in range(board_len)]
    cost_arr[0][0] = [0,0,0,0] ## right, down, left, up cost
    queue = deque([(0,0,-1,0)]) # x,y,head,cost 
    while queue:
        x_pos,y_pos,head,cost = queue.popleft()
        for next_head, dx in enumerate(dx_list):
            dy = dy_list[next_head]
            next_x_pos = x_pos + dx
            next_y_pos = y_pos + dy
            if isvalid(next_x_pos, next_y_pos,board):
                if head == -1: ## Start
                    cost_arr[next_x_pos][next_y_pos][next_head] = cost + 100
                    queue.append((next_x_pos,next_y_pos, next_head, cost+100))
                ## 같은 head 비교
                elif head == next_head:
                    if cost + 100 < cost_arr[next_x_pos][next_y_pos][next_head]:
                        cost_arr[next_x_pos][next_y_pos][next_head] = cost+100
                        queue.append((next_x_pos,next_y_pos,next_head, cost+100))
                ## 다른 head 비교
                else:
                    if cost + 600 < cost_arr[next_x_pos][next_y_pos][next_head]:
                        cost_arr[next_x_pos][next_y_pos][next_head] = cost + 600
                        queue.append((next_x_pos,next_y_pos,next_head, cost + 600))
    min_cost = INF
    for head in range(4):
        min_cost = min(min_cost,cost_arr[board_len-1][board_len-1][head])
    return min_cost

def isvalid(next_x_pos,next_y_pos,board):
    board_len = len(board)
    if 0 <= next_x_pos < board_len and 0 <= next_y_pos < board_len:
        if board[next_x_pos][next_y_pos] == 1:
            return False
        return True
    return False

if __name__ == "__main__":
    board = [[0,0,0],[0,0,0],[0,0,0]]
    result = 900
    print(solution(board),result)
    board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
    result = 3800
    print(solution(board),result)
    board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
    result = 2100
    print(solution(board),result)
    board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]
    result = 3200
    print(solution(board),result)
    board =     [[0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 1, 1, 0, 0]]
    result = 3000
    print(solution(board),result)
