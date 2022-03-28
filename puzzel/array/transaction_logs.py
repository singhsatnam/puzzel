import collections


def process(logs, threshold):
    if not logs:
        return [None]

    risky_users = []

    user_transaction_count_map = collections.defaultdict(int)
    for cur_log in logs:
        # row = ''.join(cur_log)
        print("cur_log: ", cur_log)
        sender_receiver_amount_list = [int(ele) for ele in cur_log.split(" ")]
        print("sender_receiver_amount_list:", sender_receiver_amount_list)
        if sender_receiver_amount_list[0] != sender_receiver_amount_list[1]:
            # The case where the role of the two users in the transaction logs is different
            user_transaction_count_map[sender_receiver_amount_list[1]] += 1
            user_transaction_count_map[sender_receiver_amount_list[0]] += 1
        else:
            # The case where one user plays both the roles and the continuation of the
            user_transaction_count_map[sender_receiver_amount_list[0]] += 1

    for user, transaction_count in user_transaction_count_map.items():
        if transaction_count >= threshold:
            risky_users.append(user)
    return sorted(risky_users)


print(process(["1 2 50", "1 7 70", "1 3 20", "2 2 17"], 2))
