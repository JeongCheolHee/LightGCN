import numpy as np
import random

def randint_(end):
    return random.randint(0, end - 1)

def sample_negative(user_num, item_num, train_num, allPos, neg_num):
    perUserNum = train_num // user_num
    row = neg_num + 2
    S_array = np.zeros((user_num * perUserNum, row), dtype=int)

    for user in range(user_num):
        pos_item = allPos[user]

        for pair_i in range(perUserNum):
            negitem = 0
            S_array[user * perUserNum + pair_i][0] = user
            S_array[user * perUserNum + pair_i][1] = pos_item[randint_(len(pos_item))]
            for index in range(2, neg_num + 2):
                while True:
                    negitem = randint_(item_num)
                    if negitem not in pos_item:
                        break
                S_array[user * perUserNum + pair_i][index] = negitem

    return S_array

def sample_negative_ByUser(users, item_num, allPos, neg_num):
    row = neg_num + 2
    col = len(users)
    S_array = np.zeros((col, row), dtype=int)

    for user_i, user in enumerate(users):
        pos_item = allPos[user]
        negitem = 0

        S_array[user_i][0] = user
        S_array[user_i][1] = pos_item[randint_(len(pos_item))]

        for neg_i in range(2, row):
            while True:
                negitem = randint_(item_num)
                if negitem not in pos_item:
                    break
            S_array[user_i][neg_i] = negitem

    return S_array

def set_seed(seed):
    random.seed(seed)
