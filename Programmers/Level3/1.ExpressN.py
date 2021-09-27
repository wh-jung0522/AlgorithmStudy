def solution(N, number):
    answer = -1
    if N == number:
        return 1
    set_list = [set() for i in range(8)]
    for i,n_set in enumerate(set_list, start=1):
        n_set.add(int(str(N)*i)) ## NNNNN add

    for i in range(1,8):
        for j in range(i):
            for num1 in set_list[j]: ## j == 0 -- 1번 쓴거
                for num2 in set_list[i-j-1]:
                    set_list[i].add(num1+num2)
                    set_list[i].add(num1-num2)
                    set_list[i].add(num1*num2)
                    if (num2 != 0):
                        set_list[i].add(num1//num2)
        if number in set_list[i]:
            answer = i+1
            break
    return answer
'''
    e.g) N = 5
    1set -> N
    2set -> NN , 1set(+-/*)1set
    3set -> NNN , 1set(+-/*)2set, 2set(+-/*)1set
    ...
    kset -> NNN....NN , union(1()k-1, 2()k-2, ... ,k-1()1)
'''




if __name__ =="__main__":
    print(solution(5,12),4)
    print(solution(2,11),3)