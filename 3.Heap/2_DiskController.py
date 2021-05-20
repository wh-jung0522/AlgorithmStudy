from operator import itemgetter
def makeDictFromArray(jobArray):
	dictionary = {element[0] : element[1] for element in jobArray}
	return dictionary
def solution(jobs):
	main_dictionary = makeDictFromArray(jobs)
	main_heap = jobs
	main_heap.sort(key=itemgetter(0))
	sub_heap = []
	start_time = 0
	total_time = 0
	total_num = len(jobs)
	main_end_signal = 0

	while(main_end_signal != 1):
		if (len(main_heap) == 0):
			main_end_signal = 1
		else:
			request_time = main_heap[0][0]
		while((main_end_signal == 0) and (start_time > request_time)):
			##TODO : Make Subheap [value, index] and update
			sub_heap.append([main_heap[0][0],main_heap[0][1]+start_time-main_heap[0][0]])
			main_heap.pop(0)
			if(len(main_heap)==0):
				break
			request_time = main_heap[0][0]
		if(len(sub_heap)>0):
			##TODO : Subheap Routine
			## request time 이 중복되는 경우 예외처리 필요 sub_heap[0]이 아님.
			sub_heap.sort(key=itemgetter(1))
			## Using element
			## 같은 경우
			pop_index = 0
			i = 0
			request_time, spend_time = sub_heap[0]
			sub_heap_len = len(sub_heap)
			while(True):
				if (i >= sub_heap_len):
					break
				if(request_time == sub_heap[i][0]):
					if(spend_time > sub_heap[i][1]):
						spend_time = sub_heap[i][1]
						pop_index = i
				else:
					break
				i+=1

			sub_heap.pop(pop_index)
			## Update sub_heap
			## request time 이 중복되는 경우 예외처리 필요
			process_time = main_dictionary.get(request_time)
			for i in range(len(sub_heap)):
				sub_heap[i][1] += process_time
		elif (main_end_signal == 0):
			##TODO : Mainheap Routine
			## request time 이 중복되는 경우 예외처리 필요 main_heap[0]이 아님.
			start_time, process_time = main_heap[0]
			main_heap_len = len(main_heap)
			pop_index = 0
			i = 0
			while(True):
				if (i >= main_heap_len):
					break
				if(start_time == main_heap[i][0]):
					if(process_time > main_heap[i][1]):
						process_time = main_heap[i][1]
						pop_index = i
				else:
					break
				i += 1
			start_time, process_time = main_heap.pop(pop_index)
			spend_time = process_time
			request_time = start_time
		else:
			break

		start_time += process_time
		total_time += spend_time

	return int(total_time/total_num)