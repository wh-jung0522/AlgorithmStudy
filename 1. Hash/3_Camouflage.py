def solution(clothes):
    cloth_dict = {}
    answer = 1
    for i in range(len(clothes)):
        if (cloth_dict.get(clothes[i][1])==None):
            cloth_dict[clothes[i][1]] = 1
        else:
            cloth_dict[clothes[i][1]] += 1
    for (cloth_kind, num_cloth) in cloth_dict.items():
        answer*=(num_cloth+1)
    answer-=1
    return answer

if __name__ == '__main__':
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    sol = solution(clothes)
    print(sol)