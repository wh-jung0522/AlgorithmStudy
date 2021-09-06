def binary_search(input_list:list, target:int, start_index:int, end_index:int):
    if start_index == end_index:
        return start_index
    half_index = (start_index + end_index)//2
    if input_list[half_index] > target:
        end_index = half_index
    elif input_list[half_index] < target:
        start_index = half_index
    else:
        start_index= half_index
        end_index= half_index
    return binary_search(input_list,target,start_index,end_index)

if __name__ == "__main__":
    input_list = [0,2,4,6,8,10,12,14,16,18]
    target = 10
    print(binary_search(input_list,target,0,9))