import collections


def get_association_major(l):
    visited = []
    d = collections.defaultdict(list)
    print("dict: ", d)
    print("received: ", l)

    def dfs(item, output):
        print("dfs item: ", item, "/ output: ", output)
        if item not in visited:
            print("dfs item: ", item, "/ visited: ", visited)
            visited.append(item)
            output.append(item)
            for neighbor in d[item]:
                dfs(neighbor, output)

    if len(l) < 2:
        return l

    for item in l:
        if len(item) == 1:
            d[item[0]] = []
        else:
            d[item[0]].append(item[1])
            d[item[1]].append(item[0])

    print("d is ", d)

    res = []
    for item in d:
        if item not in visited:
            print("item: ", item, "/ visited: ", visited)
            output = []
            dfs(item, output)
            output.sort()
            print("output=", output)
            if len(res) == 0 or len(output) > len(res):
                res = output
            elif len(output) == len(res):
                res = min(res, output)

    return res


print(get_association_major([['A', 'B'], ['D', 'E'], ['C', 'D']]) == ['C', 'D', 'E'])
# print(func([['A', 'B'], ['C', 'D'], ['F', 'E']]) == ['A', 'B'])
# print(func([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E']]) == ['C', 'D', 'E', 'F'])
# print(func([['A', 'B'], ['C', 'D'], ['D', 'E'], ['F', 'E'], ['A', 'C']]) == ['A', 'B', 'C', 'D', 'E', 'F'])
# print(func([['A', 'B'], ['F', 'E'], ['G', 'K'], ['C', 'D'], ['D', 'E'],
#             ['X', 'G'], ['X', 'N'], ['K', 'L'], ['L', 'M'], ['F', 'E'],
#             ['A', 'C'], ]) == ['A', 'B', 'C', 'D', 'E', 'F'])
# print(func([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]) == ['item3', 'item4', 'item5'])
# print(func([['item1', 'item2'], ['item2', 'item5'], ['item3']]) == ['item1', 'item2', 'item5'])
# print(func([['item1', 'item2'], ['item2', 'item3'], ['item4', 'item5'], ['item5', 'item6']]) == ['item1', 'item2',
#                                                                                                  'item3'])
# print(func([["item1", "item2"], ["item1", "item3"], ["item2", "item7"], ["item3", "item7"], ["item5", "item6"],
#             ["item3", "item7"]]) == ['item1', 'item2', 'item3', 'item7'])
#
# print(func([['item1', 'item2'], ['item1', 'item4'], ['item3', 'item4'], ['item4', 'item5']]))
#
# print(func([["item3", "item4"], ["item1", "item2"], ["item5", "item6"], ["item4", "item5"], ["item2", "item7"],
#             ["item7", "item8"]]))
#
# print(func([["item1", "item2"], ["item3", "item4"], ["item5", "item6"], ["item4", "item5"]]))