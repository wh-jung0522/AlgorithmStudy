def solution(prices):
    list_len = len(prices)
    answer = []
    for i in range(list_len):
        ith_value = prices[i]
        is_insert = 0
        for needle in range(list_len-i-1):
            needle_value = prices[i+1+needle]
            if(ith_value>needle_value):
                answer.append(needle+1)
                is_insert=1
                break
        if(is_insert==0):
            answer.append(list_len -i-1)

    return answer

if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    sol = solution(prices)
    print(sol)