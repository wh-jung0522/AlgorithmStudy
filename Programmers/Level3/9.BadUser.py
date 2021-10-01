import copy
def solution(user_id, banned_id):
    prob_set = []
    cal(user_id,banned_id,prob_set)
    temp_prob_set = set([frozenset(set_list) for set_list in prob_set])
    
    return len(temp_prob_set)


def cal(remain_user_ids,remain_banned_ids,prob_set):
    if len(remain_banned_ids)==0:
        prob_set.append(remain_user_ids)
        return
    for remain_user_id in remain_user_ids:
        if issubset_id(remain_banned_ids[0],remain_user_id):
            remain_user_ids_copy = copy.deepcopy(remain_user_ids)
            remain_banned_ids_copy = copy.deepcopy(remain_banned_ids)
            remain_user_ids_copy.remove(remain_user_id)
            remain_banned_ids_copy.remove(remain_banned_ids[0])
            cal(remain_user_ids_copy, remain_banned_ids_copy,prob_set)
    return

def issubset_id(ban_id,use_id):
    if len(ban_id) != len(use_id):
        return False
    for i, char in enumerate(ban_id):
        if char == "*":
            continue
        elif char != use_id[i]:
            return False
    return True

'''

'''

if __name__ == "__main__":
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "abc1**"]
    result = 2
    print(solution(user_id,banned_id),result)
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["*rodo", "*rodo", "******"]
    result = 2
    print(solution(user_id,banned_id),result)
    user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
    banned_id = ["fr*d*", "*rodo", "******", "******"]
    result = 3
    print(solution(user_id,banned_id),result)
