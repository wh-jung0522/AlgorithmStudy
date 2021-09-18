def solution(lottos, win_nums):
    min_count = 0
    max_count = 0
    min_ranking = 7
    max_ranking = 7
    for lotto in lottos:
        if lotto == 0:
            max_count += 1
    for win_num in win_nums:
        if win_num in lottos:
            min_count += 1
    max_count += min_count
    min_ranking -= min_count
    max_ranking -= max_count
    if max_ranking > 6:
        max_ranking = 6
    if min_ranking > 6:
        min_ranking = 6
    answer = []
    answer.append(max_ranking)
    answer.append(min_ranking)
    return answer

if __name__ == "__main__":
    print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]),[3, 5])