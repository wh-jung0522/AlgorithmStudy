import copy
def solution(key, lock):
    if ismatched(lock):
        return True
    key_len = len(key)
    lock_len = len(lock)
    key_90 = rotated(key)
    key_180 = rotated(key_90)
    key_270 = rotated(key_180)
    for i in range(-key_len, lock_len):
        for j in range(-key_len, lock_len):
            ## 0 degree
            lock_match = match(i,j,key,lock)
            if ismatched(lock_match):
                return True
            ## 90 degree
            lock_match = match(i,j,key_90,lock)
            if ismatched(lock_match):
                return True
            ## 180 degree
            lock_match = match(i,j,key_180,lock)
            if ismatched(lock_match):
                return True
            ## 270 degree
            lock_match = match(i,j,key_270,lock)
            if ismatched(lock_match):
                return True
    return False
'''
Step1. key 모양 4개로 만들기 
    1인 부분을 좌측 상단에 배치 X 안해도 되는게 그냥 -key_len ~ lock_len+key_len 까지 옮겨가면 됨.

Step2. 자물쇠의 0 부분을 열쇠의 1에 맞춰보기 (행, 열 더해서) 
'''
def ismatched(lock_match):
    lock_match_len = len(lock_match)
    for i in range(lock_match_len):
        for j in range(lock_match_len):
            if lock_match[i][j] == 0 or lock_match[i][j] == 2:
                return False
    return True

def match(key_start_i,key_start_j,key,lock):
    key_len = len(key)
    lock_len = len(lock)
    lock_match = copy.deepcopy(lock)
    for i in range(key_len):
        for j in range(key_len):
            lock_i = i + key_start_i
            lock_j = j + key_start_j
            if 0 <= lock_i < lock_len and 0 <= lock_j < lock_len:
                lock_match[lock_i][lock_j] += key[i][j]
    return lock_match

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]


if __name__ == "__main__":
    print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]),True)