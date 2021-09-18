class MySort:
    def __init__(self,_list:list) -> None:
        self.sorted = _list
        self.len = len(self.sorted)
        pass
    def selectionSort(self):
        listLen = self.len
        for index in range(listLen):
            minValue = self.sorted[index]
            minIndex = index
            for i in range(index,listLen): 
                if(minValue > self.sorted[i]):
                    minIndex = i
                    minValue = self.sorted[i]
            self.sorted.pop(minIndex)
            self.sorted.insert(0,minValue)
        return
    def insertSort(self):
        listLen = self.len
        for keyIndex in range(1,listLen):
            keyValue = self.sorted[keyIndex]
            for insertIndex in range(0,keyIndex):
                if(self.sorted[insertIndex]>keyValue):
                    self.sorted.pop(keyIndex)
                    self.sorted.insert(insertIndex,keyValue)
                    break
        return
    def bubbleSort(self):
        listLen = self.len
        for cycleIndex in range(1,listLen-1):
            for startIndex in range(0,listLen-cycleIndex):
                if(self.sorted[startIndex]>self.sorted[startIndex+1]):
                    temp = self.sorted[startIndex]
                    self.sorted[startIndex] = self.sorted[startIndex+1]
                    self.sorted[startIndex+1] = temp
        return
    def mergeSort(self):

        return
        
    def mergeSortSplit(_list:list):
        return _list[:len(_list)//2], _list[len(_list)//2:]

    def mergeSortMerge(_list1:list,_list2:list):
        mergedList = []
        list1len = len(_list1)
        list2len = len(_list2)
        list1Index = 0
        list2Index = 0
        while(True):
            if((list1Index==(list1len-1))and(list2Index ==(list2len-1))):
                break
            if(_list1[list1Index]<_list2[list2Index]):
                element = _list1[list1Index]
                mergedList.append(element)
                list1Index+=1
            else:
                element = _list2[list2Index]
                mergedList.append(element)
                list2Index+=1
        return mergedList

    def quickSort(self):
        return