import heapq as hp
def solution(operations):
    ## TODO
    # Step1. 명령어 Get
    # Step2. Parsing
    # Step3-1 "I num" -> heap.push(num)
    # Step3-2 "D index" -> heap.pop(0 or -1)
    heap_list = []
    answer = []
    for command_op in operations:
        heap_list = process_command(heap_list,command_op)

    heap_list_len = len(heap_list)
    if (heap_list_len == 0):
        answer.append(0)
        answer.append(0)
    elif(heap_list_len == 1):
        answer.append(heap_list[0])
        answer.append(heap_list[0])
    else:
        heap_list_temp = [-1 * x for x in heap_list]
        heap_list_temp.sort()
        answer.append(-1*hp.heappop(heap_list_temp))
        heap_list = [-1 * x for x in heap_list_temp]
        heap_list.sort()
        answer.append(hp.heappop(heap_list))

    return answer

def process_command(heap_list,command_op):
    command, index = command_op.split(" ")
    index = int(index)
    if(command == 'I'):
        hp.heappush(heap_list,index)
    elif(command == 'D'):
        if (len(heap_list) == 0):
            pass
        elif (index == 1):## delete max from heap
            heap_list_temp = [-1*x for x in heap_list]
            heap_list_temp.sort()
            hp.heappop(heap_list_temp)
            heap_list = [-1*x for x in heap_list_temp]
            heap_list.sort()
        elif (index == -1): ## delete min from heap
            hp.heappop(heap_list)

    return heap_list


if __name__ == '__main__':
    print(solution(["I 16","D 1"]) , [0,0])
    print(solution(["I 7","I 5","I -5","D -1"]) , [7, 5])