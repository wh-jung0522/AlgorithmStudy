from collections import deque
global N,M
def ch5_1():
    global N,M
    N, M = list(map(int,input("N M : ").split(" ")))
    map_array = []
    for n in range(N):
        map_array.append(list(map(int,input().split(" "))))
    '''Search '''
    count = 0
    for n in range(N):
        for m in range(M):
            if map_array[n][m] == 0:
                count += 1
                DFS(n,m,map_array)
    return count
def DFS(x,y,map_array):
    ## out of range 처리 map_array[=<N][=<M]
    if x < 0 or x >= N or y < 0 or y >= M:
        return
    if map_array[x][y] == 0:
        map_array[x][y] = 1
    else:
        return
    DFS(x+1,y,map_array)
    DFS(x-1,y,map_array)
    DFS(x,y+1,map_array)
    DFS(x,y-1,map_array)


def ch5_2(x,y):
    X, Y = list(map(int,input("N M : ").split(" ")))
    queue = deque()
    queue.append((x,y))
    map_array = []
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    for n in range(X):
        map_array.append(list(map(int,input().split(" "))))
    while True:
        x,y = queue.popleft()
        if x == X-1 and y == Y-1:
            break
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if (next_x < 0) or (next_x > (X-1)) or (next_y < 0) or (next_y > (Y-1)):
                continue
            if map_array[next_x][next_y] == 1:
                map_array[next_x][next_y] = map_array[x][y]+1
                x = next_x
                y = next_y
                queue.append((x,y))
            elif map_array[next_x][next_y] == 0:
                continue
    return map_array[X-1][Y-1]

if __name__ == "__main__":
    test_case = int(input("Test Case : "))
    if test_case == 1:
        print(ch5_1())
    elif test_case == 2:
        print(ch5_2(0,0))
    else:
        ch5_1()