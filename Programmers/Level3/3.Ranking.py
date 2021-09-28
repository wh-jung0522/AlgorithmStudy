def solution(n, results):
    answer = 0
    ## player game_array
    game_array = [[0]*(n) for i in range(n)]
    for win,lose in results:
        game_array[win-1][lose-1] = 1
        game_array[lose-1][win-1] = -1

    # win-lose graph update with floyd k,j,i
    for k in range(n):
        for j in range(n):
            for i in range(n):
                if game_array[i][j] == 0:
                    if game_array[i][k] == 1 and game_array[k][j] == 1: ## i > k > j
                        game_array[i][j] = 1
                    elif game_array[i][k] == -1 and game_array[k][j] == -1: ## j > k > i
                        game_array[i][j] = -1
    ''' 
        ijk -> 1,2 -> (1,4),(4,2) : 1 
        ijk 반례 -> 1,3 -> 아직 순서가 안돌아서 (1,5) == 0 
        kji -> k를 거쳐가는 모든 경우를 확인할 수 있음
    '''
    # don't know : 1 -> self
    for i in range(n):
        count = 0
        for j in range(n):
            if game_array[i][j] == 0:
                count+=1
            if count == 2:
                break
        if count == 1:
            answer += 1
    return answer

if __name__ == "__main__":
    print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]),5)