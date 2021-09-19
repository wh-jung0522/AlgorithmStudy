from collections import deque
def solution(record):
    nick_name_dict = {}
    queue = deque([])
    for one_record in record:
        nick_name_dict, queue = process_one(one_record,nick_name_dict,queue)
    answer = []
    answer = append_to_result(answer,nick_name_dict,queue)
    return answer

'''
UID - NickName dictionary <- for change
UID - Enter Leave Queue 
'''
def process_one(one_record:str,nick_name_dict:dict,queue:deque):
    if one_record[0] == "L": ## Leave
        cmd, uid = one_record.split(" ")
        queue.append((uid,cmd))
    elif one_record[0] == "E": ## Enter, Change
        cmd,uid,nick_name = one_record.split(" ")
        nick_name_dict[uid] = nick_name
        queue.append((uid,cmd))
    else: ## Change
        cmd,uid,nick_name = one_record.split(" ")
        nick_name_dict[uid] = nick_name
    return nick_name_dict, queue

def append_to_result(answer:list,nick_name_dict:dict,queue:deque):
    string_dict = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다."}
    while queue:
        uid, cmd = queue.popleft()
        answer.append(nick_name_dict.get(uid)+string_dict.get(cmd))
    return answer

if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]),["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])