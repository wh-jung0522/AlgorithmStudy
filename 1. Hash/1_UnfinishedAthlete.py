def solution(participant, completion):
    # Input : participant = {'a','b',...}
    #         completion = {'a',...}
    # return = 'a'
    ## slow O(n^2)
    # for ele_completion in completion:
    #     participant.remove(ele_completion)

    ## Using Hash Dictionary O(3*n)
    Hash_dict1 = make_hash_dictionary(participant)
    Hash_dict2 = make_hash_dictionary(completion)
    return get_solution(Hash_dict1,Hash_dict2)

def make_hash_dictionary(list):
    Hash_dict = {}
    for element in list:
        value = Hash_dict.get(element)
        if(value != None):
            value += 1
        else:
            value = 1
        Hash_dict[element] = value
    return Hash_dict

def get_solution(Hash_dict1, Hash_dict2):
    for (key,value1) in Hash_dict1.items():
        if((Hash_dict2.get(key) != value1) or (Hash_dict2.get(key)== None)):
            return key


if __name__ == '__main__':
    participant = ["mislav", "stanko", "mislav", "ana"]
    complement = ["stanko", "ana", "mislav"]
    sol = solution(participant,complement)
    print(sol)