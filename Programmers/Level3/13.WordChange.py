def solution(begin, target, words):
    ''' 
        make graph (dictionary)
        dictionary 탐색 with BFS (stack)
    '''
    start_word_list = []
    graph = {}
    for word1 in words:
        if isSimilar(begin,word1):
            start_word_list.append(word1)
        graph[word1] = []
        for word2 in words:
            if isSimilar(word1,word2):
                graph[word1].append(word2)
    if target in start_word_list:
        return 1

    mincount = int(1e9)
    for start_word in start_word_list:
        stack = [start_word]
        mincount = min(mincount,change(start_word, graph, stack, target))
    if mincount == int(1e9):
        mincount = 0
    return mincount

def change(prev_word, graph, stack, target):
    mincount = int(1e9)
    if len(stack) >= len(graph):
        return int(1e9)
    next_word_list = graph[prev_word]
    if target in next_word_list:
        return len(stack) + 1
    for next_word in next_word_list:
        if next_word in stack:
            continue
        else:
            stack.append(next_word)
            mincount = min(mincount, change(next_word,graph,stack,target))
    return mincount
            


def isSimilar(word1, word2):
    diff_count = 0 
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_count+=1
    if diff_count != 1:
        return False
    return True





if __name__ == "__main__":
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    result = 4
    print(solution(begin, target, words),result)
    words = ["hot", "dot", "dog", "lot", "log"]
    result = 0
    print(solution(begin, target, words),result)
    begin = "hit"
    target = "hot"
    words = ["hit", "hot", "lot"] 
    result = 1
    print(solution(begin, target, words),result)
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]), 4)
    print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]), 0)
    print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]), 1)
    print(solution("1234567000", "1234567899", [
        "1234567800", "1234567890", "1234567899"]), 3)
    print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]), 4)