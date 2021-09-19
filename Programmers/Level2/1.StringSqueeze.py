def solution(s):
    answer = len(s) ## 최대 길이
    for length in range(1,len(s)//2+1):
        answer = min(answer,squeeze_len(s,length))
    return answer
'''
Step 1. length 의 절반까지 
Step 2. Stack에 있는거 빼서 processing, 0:l-1, l:2l-1 , ... min 길이 측정

'''
def squeeze_len(s,length):
    squeezed_length = len(s)
    temp_count = 0
    temp_word = ''
    word_num = len(s)//length
    for i in range(word_num):
        word = s[i*length:(i+1)*length]
        if temp_word == word:
            squeezed_length-=len(word)
            temp_count+=1
            ## 2개 이상인 경우만 숫자 추가
            if temp_count == 2:
                squeezed_length += 1
            ## 10개 이상인 경우 한 자리 추가
            elif temp_count == 10:
                squeezed_length += 1
            ## 100개 이상인 경우 한 자리 추가 ~ 500이므로 4자리 숫자는 안나옴
            elif temp_count == 100:
                squeezed_length += 1
        else:
            temp_word = word
            temp_count = 1
    return squeezed_length

if __name__ == "__main__":
    print(solution("aaaaaaaaaaaaaaabbbbbbbbbbc"),7)