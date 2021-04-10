def solution(phone_book):
    ## If One -tepnumber is Another Header -> false
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)):
        if (i == (len(phone_book)-1)):
            return True
        else:
            if (phone_book[i] == phone_book[i+1][:len(phone_book[i])]):
                return False
    return True

##채점 결과
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0
# def solution(phone_book):
#     ## If One -tepnumber is Another Header -> false
#     hash_dict, ndic = make_dictionary(phone_book)
#     return compare_element(hash_dict, ndic)
#
# def make_dictionary(list):
#     hash_dict = {}
#     i = 0
#     for value in list:
#         hash_dict[i] = value
#         i+=1
#     return hash_dict , i
#
# def compare_element(hash_dict, ndic):
#     for (key, value) in hash_dict.items():
#         for i_key in range(key+1,ndic): ## O(n^2) -> ?
#             target_value = hash_dict.get(i_key)
#             if ((len(target_value) >= len(value))&(target_value[:len(value)]==value) ):
#                 return False
#             elif((len(target_value) < len(value))&(target_value==value[:len(target_value)])):
#                 return False
#     return True
if __name__ == '__main__':
    phone_book = ["345","12","123","1235","567","88"]
    sol = solution(phone_book)
    print(sol)




