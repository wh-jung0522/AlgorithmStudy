def solution(stones, k):
    '''
        연속된 0번째부터 k개 중 max list 만들어서 작은 숫자를 찾으면 됨.
    '''
    len_stone = len(stones)
    max_list = [0]*(len_stone-k+1)
    for i in range(len_stone-k+1):
        target_stones = stones[i:i+k]
        max_list[i] = max(target_stones)
    answer = min(max_list)
    return answer