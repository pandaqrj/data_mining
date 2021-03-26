from data import critics


def sim_distance(person1, person2):
    """欧几里得距离评价"""
    si = [] # 交集
    for item in critics[person1]:
        if item in critics[person2]:
            si.append(item) # 加入交集

    if len(si) == 0: return 0 # 交集为空则相似度为0

    # 计算欧几里得距离的平方
    sum_of_squares = sum(
        [ pow(critics[person1][item] - critics[person2][item], 2) for item in critics[person1] if item in critics[person2] ]
    )

    # 返回一个0-1保留两位小数的数字，数字越大代表相似度越高
    return round(1/(1+sum_of_squares), 2)

# print(sim_distance('Mick LaSalle', 'Toby')) # 0.31