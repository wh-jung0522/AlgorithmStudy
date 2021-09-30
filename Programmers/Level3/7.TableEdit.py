def solution(n, k, cmd):
    answer_list = [i for i in range(n)]
    now_index = k
    delete_stack = []
    for onecmd in cmd:
        if onecmd[0] == "D": ## Down
            for _ in range(int(onecmd[2:])):
                now_index += 1
                while now_index in delete_stack:
                    now_index += 1
        elif onecmd[0] == "U": ## Up
            for _ in range(int(onecmd[2:])):
                now_index -= 1
                while now_index in delete_stack:
                    now_index -= 1
        elif onecmd[0] == "C": ## remove
            isend = False
            answer_list.remove(now_index)
            delete_stack.append(now_index)
            while now_index in delete_stack:
                now_index += 1
                if now_index == n:
                    break
            if now_index == n: ## 마지막인 경우
                now_index -= 1
                while now_index in delete_stack:
                    now_index -= 1
        else: ## undo
            answer_list.append(delete_stack.pop())
    answer = ''
    for i in range(n):
        if i in answer_list:
            answer += "O"
        else:
            answer += "X"
    return answer
'''
n : 행 갯수
k : 선택 index

필요한 데이터
answer = "O"*n
현재 가르키고있는 index
삭제한 데이터 (index)가 있는 list (stack)

'''





if __name__ == "__main__":
    # n = 8
    # k = 2
    # cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
    # result = "OOOOXOOO"
    # print(solution(n,k,cmd),result)
    n = 8
    k = 2
    cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
    result = "OOXOXOOO"
    print(solution(n,k,cmd),result)