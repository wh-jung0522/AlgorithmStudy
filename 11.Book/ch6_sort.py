''' Sort Algorithm '''
import time

class mysort():
    def __init__(self, array:list):
        self.array = array

    def selection_sort(self):
        sorted_list = self.array.copy()
        start_time = time.perf_counter()
        for i in range(len(sorted_list)):
            min_index = i
            min_num = sorted_list[i]
            for j in range(i+1,len(sorted_list)):
                if min_num > sorted_list[j]:
                    min_index = j
                    min_num = sorted_list[j]
            ##swap
            sorted_list[i] ,sorted_list[min_index] = sorted_list[min_index] ,sorted_list[i]
        return sorted_list, time.perf_counter()-start_time

    def insertion_sort(self):
        sorted_list = self.array.copy()
        start_time = time.perf_counter()
        for i in range(len(sorted_list)):
            for j in range(i,0,-1):
                if sorted_list[j] < sorted_list[j-1]:
                    sorted_list[j], sorted_list[j-1] = sorted_list[j-1] ,sorted_list[j]
        return sorted_list, time.perf_counter()-start_time
    
    def quick_sort(self):
        sorted_list = self.array.copy()
        start_time = time.perf_counter()
        sorted_list = self.recur_quick_sort(sorted_list)
        return sorted_list, time.perf_counter()-start_time

    def recur_quick_sort(self,input_list): ## pythonic..
        if len(input_list) <= 1:
            return input_list
        pivot = input_list[0]
        tail = input_list[1:]
        left_list = [x for x in tail if x <= pivot]
        right_list = [x for x in tail if x > pivot]
        return self.recur_quick_sort(left_list) + [pivot] + self.recur_quick_sort(right_list)
        
    
    def in_lib_sort_1(self):
        sorted_list = self.array.copy()
        start_time = time.perf_counter()
        return sorted(sorted_list), time.perf_counter()-start_time

    def in_lib_sort_2(self):
        sorted_list = self.array.copy()
        sorted_list.sort()
        start_time = time.perf_counter()
        return sorted_list, time.perf_counter()-start_time

if __name__ == "__main__":
    input_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    sort_class = mysort(input_list)
    print("selection sort : ",sort_class.selection_sort())
    print("insertion sort : ",sort_class.insertion_sort())
    print("quick sort : ",sort_class.quick_sort())
    print("lib sorted : ",sort_class.in_lib_sort_1())
    print("lib sort : ",sort_class.in_lib_sort_2())