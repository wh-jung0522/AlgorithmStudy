def solution(gems):
    ''' 
        Spec : Max gems = 100000
        O(N^2) : time out
        
        Stratege 1 : O(N + N^2)
            Step1. find gem list
            Step2. binary search(start++, end--)
        
        Stratege 2 : 
            Step1. Gem index Dictionary
            Step2. binary search 범위 줄여나갈 것.

    '''
    gems_set = set(gems)
    gems_len = len(gems)
    min_len = gems_len
    answer = [1,gems_len]
    for start_index in range(gems_len):
        if not gems_set.issubset(gems[start_index:]):
            break
        end_index = gems_len
        box = gems_len-start_index
        while True:
            box = box//2 + 1
            if box == 0:
                break
            if gems_set.issubset(gems[start_index:end_index+1]):
                if not gems_set.issubset(gems[start_index:end_index]):
                    break
                end_index -= box
            else:
                if gems_set.issubset(gems[start_index:end_index+2]):
                    end_index += 1
                    break
                end_index += box
        if min_len > end_index-start_index+1:
            min_len = end_index-start_index+1
            answer = [start_index+1,end_index+1]
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