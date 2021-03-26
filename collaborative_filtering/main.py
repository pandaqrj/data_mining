from data import critics


def sim_distance(person1, person2):
    from math import sqrt
    si = [] #交集
    for item in critics[person1]:
        if item in critics[person2]:
            si.append(item) #加入交集

    if len(si) == 0: return 0 #交集为空则相似度为0

    #计算欧几里得距离
    sum_of_squares = sum(
        [ pow(critics[person1][item] - critics[person2][item], 2) for item in critics[person1] if item in critics[person2] ]
    )
    return 1/(1+sum_of_squares)

print(sim_distance('Claudia Puig', 'Jack Matthews'))