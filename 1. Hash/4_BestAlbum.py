def solution(genres, plays):

    ## 1. favorite genre -> dictionary ,number
    ## 2. favorite two album per genre -> two dictionary order:genre, order:plays.
    order_dict, info_dict = make_info(genres, plays) # {"classic":[0,1,2,...]}
    ## find genre order
    ## info_dict = sorted(info_dict.items(),key=(lambda x:x[1]),reverse=True)
    answer = sumandlist2dict(order_dict, info_dict)
    return answer

def make_info(genres, plays):
    order_dic = {}
    info_dic = {}
    for i in range(len(genres)):
        if (info_dic.get(genres[i])==None):
            info_dic[genres[i]] = [plays[i]]
            order_dic[genres[i]] = [i]
        else:
            order_dic[genres[i]].append(i)
            info_dic[genres[i]].append(plays[i])

    return order_dic, info_dic

def sumandlist2dict(order_dic, info_dic):
    sum_dict = {}
    order_dict = {}
    return_list = []
    for key,value in order_dic.items():
        sum, return_order = sumandlist(info_dic.get(key),value)
        sum_dict[key] = sum
        order_dict[key] = return_order

    sum_dict = sorted(sum_dict.items(),key=(lambda x:x[1]),reverse=True)
    for key,value in sum_dict:
        return_list.extend(order_dict.get(key))
    return return_list

def sumandlist(plays_list,ordered_list):
    sum = 0
    best_order = []## playlist order
    return_order = []
    for i in range(len(plays_list)):
        sum+=plays_list[i]
        if(len(best_order)==0):
            best_order.append(i)
        elif(plays_list[best_order[0]]<plays_list[i]):
            best_order.insert(0,i)
        elif(len(best_order)==1):
            best_order.append(i)
        elif(plays_list[best_order[1]]<plays_list[i]):
            best_order[1] = i
    return_order.append(ordered_list[best_order[0]])
    return_order.append(ordered_list[best_order[1]])
    return sum, return_order


if __name__ == '__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    sol = solution(genres, plays)
    print(sol)