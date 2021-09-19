from math import gcd, ceil, floor
def solution(w,h):
    answer = w*h
    max_a = max(w,h)
    min_a = min(w,h)
    gcd_num = gcd(w,h)
    max_prime =  max_a//gcd_num
    min_prime = min_a//gcd_num
    ## 

    if min_prime == 1: ## gcd_num == min_number인 경우
        broken_rate = max_prime//min_prime
        broken_square = broken_rate*min_a
    else: ## gcd_num과 min_number가 다른 경우
        broken_rate = max_prime/min_prime
        broken_count = 0
        for i in range(min_prime):
            if i == min_prime-1:
                start_number = floor(i* broken_rate)
                end_number = max_prime
            else:
                start_number = floor(i* broken_rate)
                end_number = ceil((i+1)*broken_rate)
            broken_count += (end_number - start_number)
        broken_square = broken_count*gcd_num
    answer -= broken_square
    return answer
'''
비율이 1:1 -> 가로로 1갈 때, 세로 1이 없어짐 대각선만 없어짐
(0,1] 1 /(1,2] 2 
비율 1:2 -> 가로로 1갈 때, 세로 2 없어짐
비율 2:3 -> 가로 2갈 때, 세로 4 =  [1.5] *2 없어짐
비율 2:5 -> 가로 2갈 때, 세로 6 = [2.5] *2
(0~2.5] 1,2,3 / (2.5~5] 3,4,5 
비율 3:5 -> 가로 3갈 때, 세로 7 != [1.67] *3
(0~1.67] 1,2 / (1.67~3.33] 2,3,4 / (3.33~5] 4,5
'''



if __name__ == "__main__":
    print(solution(3,5),8)