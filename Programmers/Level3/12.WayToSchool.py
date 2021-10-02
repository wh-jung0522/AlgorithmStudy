def solution(m, n, puddles):
    way_array = [[0]*(m+n) for i in range(m+n)]
    way_array[0][0] = 1
    ## puddle = [i+1][j+1]
    for k in range(1,m+n):
        way_array, puddles = update_nth(k,way_array, puddles)
    answer = way_array[m-1][n-1]
    return answer


def update_nth(n,way_array,puddles):
    rem_puddle = [-1,-1]
    for i in range(n+1):
        if i == 0:
            way_array[i][n-i] = way_array[i][n-i-1]
        elif i == n:
            way_array[i][n-i] = way_array[i-1][n-i]
        else:
            way_array[i][n-i] = way_array[i][n-i-1] + way_array[i-1][n-i]
        for puddle in puddles:
            if puddle[0]-1 == i and puddle[1]-1 == n-i:
                way_array[i][n-i] = 0
                rem_puddle = puddle
                break
        if rem_puddle in puddles:
            puddles.remove(puddle)
    return way_array, puddles

if __name__ == "__main__":
    m = 4
    n = 3
    puddles = [[2,2]]
    result = 4
    print(solution(m,n,puddles),result)