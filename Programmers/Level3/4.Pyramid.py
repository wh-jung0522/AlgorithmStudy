def solution(enroll, referral, seller, amount):
    parent_dict = {}
    selling_dict = {}
    selling_dict['center'] = 0
    for i in range(len(enroll)):
        parent = referral[i]
        if referral[i] == '-':
            parent = 'center'
        parent_dict[enroll[i]] = parent
        selling_dict[enroll[i]] = 0

    for i in range(len(seller)):
        next_seller = seller[i]
        next_amount = amount[i]*100
        while True:
            sell_amount = next_amount - next_amount//10
            next_amount -= sell_amount
            selling_dict[next_seller] += sell_amount
            next_seller = parent_dict[next_seller]
            if next_seller == 'center':
                selling_dict[next_seller] += next_amount
                break
            if next_amount == 0:
                break

    answer = []
    for sellerman in enroll:
        answer.append(selling_dict[sellerman])
    return answer


if __name__=="__main__":
    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]


    result = [360, 958, 108, 0, 450, 18, 180, 1080]

    print(solution(enroll, referral, seller, amount),result)