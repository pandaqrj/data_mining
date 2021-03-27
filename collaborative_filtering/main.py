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
    return 1/(1+sum_of_squares)

# print(sim_distance('Mick LaSalle', 'Toby')) # 0.31

def sim_pearson(person1, person2):
    """皮尔斯相关度评价"""
    from math import sqrt

    si = [] # 交集
    for item in critics[person1]:
        if item in critics[person2]:
            si.append(item) # 加入交集

    if len(si)==0: return 0
    n=len(si)

    # 评分求和
    sum1=sum([critics[person1][it] for it in si])
    sum2=sum([critics[person2][it] for it in si])
    
    # 评分平方和
    sum1Sq=sum([pow(critics[person1][it],2) for it in si])
    sum2Sq=sum([pow(critics[person2][it],2) for it in si])	
    
    # 评分乘积和
    pSum=sum([critics[person1][it]*critics[person2][it] for it in si])
    
    # 皮尔斯相关系数计算
    # 当相关系数为0时，X和Y两变量无关系。
    # 当X的值增大（减小），Y值增大（减小），两个变量为正相关，相关系数在0.00与1.00之间。
    # 当X的值增大（减小），Y值减小（增大），两个变量为负相关，相关系数在-1.00与0.00之间。
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    # 返回绝对值
    return abs(num/den)

# print(sim_pearson('Lisa Rose', 'Gene Seymour')) # 0.39605901719066977