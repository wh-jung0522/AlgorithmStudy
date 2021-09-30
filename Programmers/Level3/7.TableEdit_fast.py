def solution(n, k, cmd):
    route_list = [[i-1,i+1] for i in range(n)]
    route_list[n-1][1] = -1
    now_index = k
    delete_stack = []
    for onecmd in cmd:
        if onecmd[0] == "D": ## Down
            for _ in range(int(onecmd[2:])):
                now_index = route_list[now_index][1]
                '''
                routing algorihtm
                '''
        elif onecmd[0] == "U": ## Up
            for _ in range(int(onecmd[2:])):
                now_index = route_list[now_index][0]
                '''
                routing algorihtm
                '''
        elif onecmd[0] == "C": ## remove
            before_index = route_list[now_index][0]
            next_index = route_list[now_index][1]
            if before_index != -1:
                route_list[before_index][1] = next_index
            if next_index != -1:
                route_list[next_index][0] = before_index
            delete_stack.append(now_index)
            if route_list[now_index][1] != -1:
                now_index = route_list[now_index][1]
            else:
                now_index = route_list[now_index][0]
            '''
                routing algorihtm
                if now_next == -1:
                    now_index = now_before
            '''
        else: ## undo
            undo_index = delete_stack.pop()
            before_index = route_list[undo_index][0]
            next_index = route_list[undo_index][1]
            if before_index != -1:
                route_list[before_index][1] = undo_index
            if next_index != -1:
                route_list[next_index][0] = undo_index

    answer = ''

    next_O_index = 0
    while next_O_index in delete_stack:
        next_O_index += 1
    ## | ~~ |First O
    for _ in range(next_O_index):
        answer+="X"
    ## |OX~~|O...
    while next_O_index != -1:
        answer+="O" ## next_O_index
        for _ in range(route_list[next_O_index][1]-next_O_index-1):
            answer+="X"
        next_O_index = route_list[next_O_index][1]
    ## Last O| ~~ |
    ans_len = len(answer)
    if ans_len != n:
        for _ in range(n-ans_len):
            answer+= "X"

    return answer

if __name__ == "__main__":
    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    result = "OOXOXOOO"
    print(solution(n,k,cmd),result)