REMOVE = 0
ADD = 1
def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x,y,frame_type,build_type  = frame
        if build_type == ADD:
            answer.append((x,y,frame_type))
            if not isvalid(answer):
                answer.remove((x,y,frame_type))
        else:
            answer.remove((x,y,frame_type))
            if not isvalid(answer):
                answer.append((x,y,frame_type))
    answer = [list(i) for i in answer]
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer
vertical = 0
horizon = 1
def isvalid(answer):
    for x_pos,y_pos,frame_type in answer:
        if frame_type == vertical:
            if y_pos == 0 or (x_pos-1,y_pos,horizon) in answer or (x_pos,y_pos,horizon) in answer or (x_pos,y_pos-1,vertical) in answer:
                continue
            else:
                return False
        if frame_type == horizon:
            if (x_pos,y_pos-1,vertical) in answer or (x_pos+1,y_pos-1,vertical) in answer or ((x_pos-1,y_pos,horizon) in answer and (x_pos+1,y_pos,horizon) in answer):
                continue
            else:
                return False
    return True

if __name__ == '__main__':
    n = 5
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
    result = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
    print(solution(n,build_frame))
    print(result)