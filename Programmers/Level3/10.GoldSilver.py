def solution(a, b, g, s, w, t):
    '''
    a : 운반해야하는 금
    b : 운반해야하는 은
    g : 도시별로 갖고있는 금
    s : 도시별로 갖고있는 은
    w : 도시의 트럭이 한번에 운반할 수 있는 양
    t : 도시의 트럭이 걸리는 편도 시간

    Obj : min sum( max(ti*(2*ni -1 )) )
        a =< g1*(t1*(2*n1-1)) + g2*(t2*(2*n2-1))
        b =< s1*(t1*(2*n1-1)) + s2*(t2*(2*n2-1))
        g1+s1 =< w1
        g2+s2 =< w2

    Stratege : Binary Search with Time index
    '''
    ## Step 1. Init MAX Time 
    ## 전체 도시 * 광물을 한번에 운반할 수 있는 양 * 광물을 한번에 운반하는데 걸리는 편도 시간 * 2(왕복)  * 2(금,은)
    MAX_TIME = (int(1e9) * (int(1e5) * 2))*2 
    answer = MAX_TIME
    start = 0
    end = MAX_TIME
    total_city = len(g)
    while (start<=end):
        mid = (start+end)//2 ## start : 499, end : 500 -> mid = 499
        max_gold_carry = 0
        max_silver_carry = 0
        max_total_carry = 0
        for i in range(total_city):
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]
            now_move_count = mid//(now_time*2)
            if (mid % (now_time*2) >= now_time): ## 추가적인 편도 가능할 경우
                now_move_count += 1
            ## 도시 하나당 MAXIMUM 을 전부 더하는데, GOLD랑 SILVER weight count 를 중복해서 사용해도되는건지
            ## -> 가능함 : total carry 값도 고려하기 때문에
            ## 도시가 갖고있는 광물과 최대로 보낼 수 있는 광물중 작은 값을 carry에 더함.
            
            ## gold 
            max_gold_carry += min(now_gold, now_move_count * now_weight)
            # silver
            max_silver_carry += min(now_silver,now_move_count * now_weight)
            # total
            max_total_carry += min(now_gold + now_silver, now_move_count * now_weight)
        if max_gold_carry >= a and max_silver_carry >=b and max_total_carry>=(a+b):
            end = mid -1
            answer = min (answer,mid)
        else:
            start = mid +1

    return answer

if __name__ == "__main__":
    a= 10
    b= 10
    g=[100]
    s=[100]
    w=[7]
    t=[10]
    result = 50 
    print(solution(a,b,g,s,w,t),result)
    a= 90
    b= 500
    g=[70,70,0]
    s=[0,0,500]
    w=[100,100,2]
    t=[4,8,1]
    result = 499 
    print(solution(a,b,g,s,w,t),result)