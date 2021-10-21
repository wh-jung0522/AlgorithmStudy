def solution(n):
    answer = start2end(1,3,n)
    return answer


'''
TODO : start to end point with n

'''
def start2end(start,end,n):
    if n == 1:
        return [[start,end]]
    point_list = [1,2,3]
    point_list.remove(start)
    point_list.remove(end)
    buffer = point_list[0]
    answer = []
    answer.extend(start2end(start,buffer,n-1))
    answer.append([start,end])
    answer.extend(start2end(buffer,end,n-1))
    return answer



if __name__== "__main__":
    '''
    n=1 from 1 to 3
    1 -> 3

    n=2 from 1 to 3 
    (n=1 from 1 to 2)1->2 || 1->3 || (n=1 from 2 to 3)2->3

    n=3
    (n=2 from 1 to 2) 1->3, 1->2, 3->2 || 1->3 ||(n=2 from 2 to 3) 2->1, 2->3, 1->3

    n=4
    (n=3 from 1 to 2) 1->2, 1->3, 2->3, 1->2, 3->1, 3->2, 1->2 || 1->3 (가장 밑에있는 거 옮기기) ||| & (n=3 from 2 to 3)
    
    '''
    # print(solution(2))
    # print([ [1,2], [1,3], [2,3] ])
    print(solution(3))
