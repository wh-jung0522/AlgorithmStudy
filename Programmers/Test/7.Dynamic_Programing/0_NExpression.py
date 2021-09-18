def solution(N, number):
    ''' 
    0. 고려사항 N*N, N+N, N-N
    1. 1을 만드는 방법 : N/N
    2. 11을 만드는 방법 : NN/N

    State 수 : 
    '''
    count = 0


    if (count>8):
        return -1
    return count



if __name__ == "__main__":
    print(solution(5,12) , 4)