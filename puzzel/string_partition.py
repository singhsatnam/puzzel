from typing import List


def partition_labels(S: str) -> List[int]:
    res = []
    last_occur = {}
    for i in range(len(S)):
        last_occur[S[i]] = i
    last = 0
    start = 0
    for i in range(len(S)):
        last = max(last, last_occur[S[i]])
        print(last)
        if last == i:
            add_this = last - start + 1
            res.append(add_this)
            start = last + 1

    return res


partition = partition_labels("ababcbacadefegdehijhklij")
print(partition)