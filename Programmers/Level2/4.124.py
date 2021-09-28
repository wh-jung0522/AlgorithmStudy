def solution(n):
    answer = rule(n)
    answer = answer.replace("3","4")
    return answer
'''
    1,2,3, 4, 5, 6, 7, 8, 9,10,11,12, 13, 14, 15, 16, 17  ---10진법
    1,2,3,11,12,13,21,22,23,31,32,33, 111,112,113,121,
    1,2,4,11,12,14,21,22,24,41,42,44, 111,112,114,121,122


    Step 1. 3진법 변경 
'''

def rule(n:int):
    q = n//3 # 1
    r = n%3 # 0
    add_string = str(r)
    if r == 0 and q > 0:
        add_string = str(3)
        q -= 1
    if q < 4:
        if q == 0:
            return add_string
        else:
            return str(q) + add_string

    return rule(q)+add_string

if __name__ == "__main__":
    print(solution(17),122)