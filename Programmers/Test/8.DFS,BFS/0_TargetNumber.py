from collections import deque
count = 0
def solution(numbers, target):
    deq_numbers = deque(numbers) ## to optimize
    recurrency_solution(deq_numbers,target)
    return count

def recurrency_solution(numbers : deque, target):
    global count
    if len(numbers) == 0:
        if target == 0:
            count += 1
        return count
    else:
        now_number = numbers.popleft()
        temp_numbers1 = numbers.copy()
        temp_numbers2 = numbers.copy()
        recurrency_solution(temp_numbers1,target-now_number)
        recurrency_solution(temp_numbers2,target+now_number)

if __name__ == "__main__":
    print(solution([1,1,1,1,1],3),5)