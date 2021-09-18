def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_stack = bridge_length*[0]
    for i in range(len(truck_weights)):
        step_time = 0
        bridge_stack, step_time = process_truck_inout_bridge(bridge_stack,weight,truck_weights[i],step_time)
        answer+=step_time
    answer+=bridge_length
    return answer

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_stack = bridge_length*[0]
    for i in range(len(truck_weights)):
        step_time = 0
        bridge_stack, step_time = process_truck_inout_bridge(bridge_stack,weight,truck_weights[i],step_time)
        answer+=step_time
    answer+=bridge_length
    return answer

def process_truck_inout_bridge(bridge_stack,weight_limit,truck_weight,step_time):
    brige_sum = sum(bridge_stack[1:])##Time Delay occur
    if((brige_sum+truck_weight)<=weight_limit):
        bridge_stack.pop(0)
        bridge_stack.append(truck_weight)
        step_time+=1
    else:
        while(brige_sum>(weight_limit-truck_weight)):
            bridge_stack.pop(0)
            brige_sum -= bridge_stack[0]
            bridge_stack.append(0)
            step_time += 1
        bridge_stack.pop(0)
        bridge_stack.append(truck_weight)
        step_time += 1
    return bridge_stack, step_time


    ## 재귀함수가 길어지면 runtime error
    # else:
    #     bridge_stack.pop(0)
    #     bridge_stack.append(0)
    #     step_time += 1
    #     return process_truck_inout_bridge(bridge_stack,weight_limit,truck_weight,step_time)

if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7, 4, 5, 6]
    sol = solution(bridge_length, weight, truck_weights)
    print(sol)