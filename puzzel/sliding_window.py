import collections


def subarraysWithKDistinct(A, K):
    return atMostK(A, K) - atMostK(A, K - 1)


def atMostK(A, K):
    count = collections.Counter()
    res = i = 0
    for j in range(len(A)):
        if count[A[j]] == 0:
            K -= 1
            print("k:", K)
        count[A[j]] += 1
        print(count)
        while K < 0:

            count[A[i]] -= 1
            if count[A[i]] == 0: K += 1
            i += 1
        res += j - i + 1
    return res

print(subarraysWithKDistinct([1,2,1,2,3], 2))

# print(subarraysWithKDistinct("12123", 2))