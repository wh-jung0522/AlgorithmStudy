## 1. 12345 %5
## 2. 21232425 %8
## 3. 3311224455 %10


def solution(answers):
    answer = []
    ans_1 = [1,2,3,4,5]
    ans_2 = [2,1,2,3,2,4,2,5]
    ans_3 = [3,3,1,1,2,2,4,4,5,5]
    score_1 = 0
    score_2 = 0
    score_3 = 0
    for i in range(len(answers)):
        if (answers[i] == ans_1[i%5]):
            score_1 += 1
        if (answers[i] == ans_2[i%8]):
            score_2 += 1
        if (answers[i] == ans_3[i%10]):
            score_3 += 1  
    if(score_1 > score_2):
        if (score_1 > score_3):
            answer.append(1)
        elif(score_1 == score_3):
            answer.append(1)
            answer.append(3)
        else:
            answer.append(3)
    elif(score_1 == score_2):
        if(score_1 > score_3):
            answer.append(1)
            answer.append(2)
        elif(score_1 == score_3):
            answer.append(1)
            answer.append(2)
            answer.append(3)
        else:
            answer.append(3)
    else:## score_2>score_1
        if(score_2 > score_3):
            answer.append(2)
        elif(score_2 == score_3):
            answer.append(2)
            answer.append(3)
        else:
            answer.append(3)

    return answer