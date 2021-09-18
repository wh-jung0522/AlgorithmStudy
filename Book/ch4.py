def ch4_1():
    position = (1,1)
    dright = (0,1)
    dleft = (0,-1)
    dup = (-1,0)
    ddown = (1,0)
    N = int(input("Space : "))
    Plan_list = input("Plans : ").split(" ")
    for move in Plan_list:
        if move == "R":
            dmove = dright
        elif move == "L":
            dmove = dleft
        elif move == "U":
            dmove = dup
        else:
            dmove = ddown
        temp_position = (position[0]+dmove[0],position[1]+dmove[1] )
        if (temp_position[0]<1 or temp_position[1]<1 or temp_position[0]>5 or temp_position[1]>5):
            continue
        else:
            position = temp_position
    return position

def ch4_2():
    N, M = list(map(int,input("N M : ").split(" ")))
    x,y,head = list(map(int,input("x y head : ").split(" ")))
    position = [x,y]
    dup = [0,-1]
    ddown = [0,1]
    dright = [1,0]
    dleft = [-1,0]
    map_array = []
    for n in range(N):
        map_array.append(list(map(int,input().split(" "))))

    rotation = 0
    map_array[position[1]][position[0]] = 1
    count = 1
    while (True):
        if head == 0:
            dmove = dup
        elif head == 1:
            dmove = dright
        elif head == 2:
            dmove = ddown
        else:
            dmove = dleft
        temp_position = [position[0]+dmove[0],position[1]+dmove[1]]
        if map_array[temp_position[1]][temp_position[0]] == 1:
            rotation += 1
            if rotation >3:
                break
            head += 1
            head %= 4
        else:
            position = temp_position
            map_array[position[1]][position[0]] = 1
            rotation = 0
            count += 1
    return count


if __name__ == "__main__":
    test_case = int(input("Test Case : "))
    if test_case == 1:
        print(ch4_1())
    elif test_case == 2:
        print(ch4_2())
    else:
        ch4_1()