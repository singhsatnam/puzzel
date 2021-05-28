import heapq
from collections import Counter
from heapq import heappush, heappop


class Solution:
    def reorganizeString(self, S):
        max_freq = Counter(S).most_common(1)[0][1]
        print(max_freq)
        if 2 * max_freq - 1 > len(S):
            return ""
        else:
            heap = []
            for k, v in Counter(S).items():
                print(k, v)
                heappush(heap, (v * -1, k))
            print(heap)
            result = []
            while heap:
                v, k = heappop(heap)
                print(v, k)
                if not result or k != result[-1]:  # can add the top most element
                    result.append(k)
                    if v != -1:
                        heappush(heap, (v + 1, k))
                else:  # cannot add the top most element
                    v1, k1 = heappop(heap)
                    result.append(k1)
                    heappush(heap, (v, k))
                    if v1 != -1:
                        heappush(heap, (v1 + 1, k1))

            print(result)
            return "".join(result)

    def reorganizeString2(self, S):
        res, c = [], Counter(S)
        pq = [(-value, key) for key, value in c.items()]

        heapq.heapify(pq)
        print(pq)
        p_a, p_b = 0, ''
        while pq:
            a, b = heapq.heappop(pq)
            print("popped: ", a, b)
            print("remaining pq:", pq)
            res.append(b)
            print("res=", res)

            print("a=", a)
            a += 1
            print("a=", a)
            if p_a < 0:
                print(p_a, " < 0")
                heapq.heappush(pq, (p_a, p_b))
                print(pq)
            p_a, p_b = a, b
            print("pa, pb=", p_a, p_b)

        res = ''.join(res)
        if len(res) != len(S): return ""
        return res


soln = Solution()
soln.reorganizeString2("aaaabbccc")
# Time O(N log(A)) = O(N); N=len(string), A=max(freq(letters))
# Space O(A)
