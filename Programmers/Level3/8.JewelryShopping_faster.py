def solution(gems):
    ''' 
        Spec : Max gems = 100000
        O(N^2) : time out
        
        Stratege 1 : 
            Step1. Gem index Dictionary
            Step2. binary search 범위 줄여나갈 것.
        Stratege 2 : 
            Two Pointer Algorithm
            주의 : issubset -> O(N) 따라서, dictionary와 비교해야함.

    '''
    gems_set = set(gems)
    gems_len = len(gems)
    answer = [1,gems_len]
    start = 0
    end = 0
    min_len = gems_len
    while end < gems_len:
        if gems_set.issubset(gems[start:end+1]):
            if end-start+1 < min_len:
                min_len = end-start+1
                answer = [start+1,end+1]
            start += 1
        else:
            end += 1
    return answer
    

if __name__ == "__main__":
    gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    result = [3, 7]
    print(solution(gems),result)
    gems = ["AA", "AB", "AC", "AA", "AC"]
    result = [1, 3]
    print(solution(gems),result)
    gems = ["XYZ", "XYZ", "XYZ"]
    result = [1, 1]
    print(solution(gems),result)
    gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
    result = [1, 5]
    print(solution(gems),result)
    gems = ["A", "B" ,"B", "C", "A", "B", "C", "A","B","C"]
    result = [3, 5]
    print(solution(gems),result)