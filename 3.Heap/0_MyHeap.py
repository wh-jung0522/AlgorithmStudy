# TODO : Make Minimun Heap (not exat min heap)
#        Compare heapq (exact min heap)
#
import heapq

class myHeap:
    def __init__(self,list = []):
        self.len = len(list)
        self.heap = self.sort(list)
        return
    
    def push(self,heap,element):
        ## bubble - up (not exact min)
        # Step1. append at k (self.len)
        # Step2. Compare with A[(k-1)//2]
        # Step3. while(A[(k-1)//2] > A[k])
        #        switch i.e Temp = A[(k-1)//2]
        #                   A[(k-1)//2] = A[k]
        #                   A[k] = Temp
        #        update k i.e k = (k-1)//2
        k = len(heap)
        heap.append(element)
        while(heap[int((k-1)/2)] > heap[k]):## > : min heap, < : max heap
            # switch
            temp = heap[int((k-1)/2)]
            heap[int((k-1)/2)] = heap[k]
            heap[k] = temp
            # update k
            k = int((k-1)/2)
            if(k<0):
                break
        return

    def pop(self,heap: list):
        # Step1. pop A[0]
        minimum = heap.pop(0)
        # Step2. pop A[last]
        n = len(heap)
        maximum = heap.pop(n-1)
        # Step3. push at 0
        heap.insert(0,maximum)
        # Step4. sort
        k = 0
        while(k<n-1):
            #switch
            leftchildindex = 2*k+1
            rightchildindex = 2*k+2
            temp = heap[k]
            if(leftchildindex> n-1):
                break
            leftchild = heap[leftchildindex]
            if(rightchildindex>n-1):
                heap[k] = leftchild
                heap[leftchildindex] = temp
                k = leftchildindex
                break
            rightchild = heap[rightchildindex]
            if(leftchild < rightchild):
                heap[k] = leftchild
                heap[leftchildindex] = temp
                k = leftchildindex
            else:
                heap[k] = rightchild
                heap[rightchildindex] = temp
                k = rightchildindex

        return minimum
    def sort(self,list):
        # Step1. n = len(list)
        #       sortedheap = []
        #       for i in range(n):
        #             self.push(sortedheap,list[i])
        sortedheap = []
        for i in range(self.len):
            self.push(sortedheap,list[i])
        return sortedheap

if __name__ == '__main__':
    mylist = [7,5,4,8,6,56,78,11,2,1,64,9,10]
    stdheap = mylist
    myheap = myHeap(mylist)
    print(myheap.heap)
    min = myheap.pop(myheap.heap)
    print(min,myheap.heap)
    # heapq.heapify(stdheap)
    # print(stdheap)
