def solution(board, moves):
    answer = 0
    stack = []
    for move in moves:
        board, pop_value = board_update(board,move)
        if pop_value == 0:
            continue
        stack, isPop = stack_update(stack,pop_value)
        if isPop:
            answer += 2
    return answer
''' 
시각화 
[[0,0,0,0,0],
 [0,0,1,0,3],
 [0,2,5,0,1],
 [4,2,4,4,2],
 [3,5,1,3,1]]

작동
[1,5,3,5,1,2,1,4]

Step 1. move 마다 pop, board update

Stpe 2. stack에 pop 한 요소 update
'''

def board_update(board, move):
    pop_index = move-1
    pop_value = 0
    i = 0
    max_index = len(board)
    while True:
        if board[i][pop_index] != 0:
            pop_value = board[i][pop_index]
            board[i][pop_index] = 0
            break
        i += 1
        if i >= max_index:
            break
    return board, pop_value

def stack_update(stack,pop_value):
    isPop = False
    if len(stack) != 0 and stack[-1] == pop_value:
        stack.pop()
        isPop = True
    else:
        stack.append(pop_value)
    return stack, isPop


if __name__ == "__main__":
    print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]),4)
