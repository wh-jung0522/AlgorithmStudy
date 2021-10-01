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
    gem_stack = []
    gem_dictionary = {}
    for index, gem in enumerate(gems):
        if gem_dictionary.get(gem) == None:
            gem_dictionary[gem] = [index+1]
            gem_stack.append(gem)
        else:
            gem_dictionary[gem].append(index+1)
    
    len_gems = len(gems)
    answer = [1,len_gems]
    min_len = len_gems
    for i in range(len_gems):
        temp_start, temp_end = find_result(gem_dictionary,gems,gem_stack,i+1,len_gems)
        if temp_start == -1:
            break
        if min_len > (temp_end - temp_start +1):
            answer = [temp_start,temp_end]
            min_len = temp_end - temp_start +1
    return answer


def find_result(gem_dictionary, gems, gem_stack, start_index, end_index):
    gem_stack_copy = gem_stack.copy()
    isupdate = False
    for i in range(start_index,end_index+1):
        if gems[i-1] in gem_stack_copy:
            for gem, gem_list in gem_dictionary.items():
                if i in gem_list:
                    gem_stack_copy.remove(gem)
        if len(gem_stack_copy) == 0:
            isupdate = True
            break
    if isupdate:
        return start_index, i
    else:
        return -1,-1

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