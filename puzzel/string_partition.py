from typing import List


def partition_labels(S: str) -> List[int]:
    res = []
    last_occur = {}
    for i in range(len(S)):
        last_occur[S[i]] = i
    print("last occur: ", last_occur)
    last = 0
    start = 0
    for i in range(len(S)):
        print("i=", i, " ele=", S[i])
        last = max(last, last_occur[S[i]])
        print("last=", last)
        if last == i:
            print(last, "==", i)
            add_this = last - start + 1
            res.append(add_this)
            start = last + 1

    return res


partition = partition_labels("ababcbacadefegdehijhklij")
print(partition)
