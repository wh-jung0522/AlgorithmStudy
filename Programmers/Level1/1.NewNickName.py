import re
def solution(new_id:str):
    ## Step 1. 대문자 -> 소문자
    answer = new_id
    answer = answer.lower()
    ## Step 2. 특수문자 제외하고 뺌.
    answer = re.sub(r"[^a-z0-9-_.]","",answer)
    ## Step 3. 온점 2개 -> 하나로 만듦
    while True:
        next_anwer = answer.replace("..",".")
        if next_anwer == answer:
            break
        else:
            answer = next_anwer
    ## Step 4. 시작,끝 온점 삭제
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] =='.':
        answer = answer[:-1]
    ## Step 5. 
    if len(answer) == 0:
        answer = 'a'
    ## Step 6. 15개까지 , 마지막 온점 삭제
    if len(answer) > 15:
        answer = answer[:15]
    if len(answer) != 0 and answer[-1] =='.':
        answer = answer[:-1]
    ## Step 7. 글자수가 두개 이하인 경우 마지막 문자 추가
    while len(answer) <= 2:
        answer += answer[-1]
    return answer


if __name__ == "__main__":
    print(solution("=.="),"aaa")