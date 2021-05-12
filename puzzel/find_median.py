class Solution:

    def find_median_sorted_arrays(self, A, B):
        l = len(A) + len(B)
        print("l: ", l)
        if l % 2 == 1:
            return self.kth(A, B, l // 2)
        else:
            return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.

    def kth(self, a, b, k):
        print("new input: a:", a, " b:", b, " k:", k)

        if not a:
            return b[k]
        if not b:
            return a[k]
        ia, ib = len(a) // 2, len(b) // 2
        ma, mb = a[ia], b[ib]
        print("A[", ia, "]=", ma, " B[", ib, "]=", mb)

        # when k is bigger than the sum of a and b's median indices
        if ia + ib < k:
            print("a's and b's last are interesting as ", ia, "+", ib, " < ", k)
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.kth(a, b[ib + 1:], k - ib - 1)
            else:
                return self.kth(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            print("a's and b's first are interesting as ", ia, "+", ib, " >= ", k)
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.kth(a[:ia], b, k)
            else:
                return self.kth(a, b[:ib], k)


soln = Solution() # log(log(m+n))
print("case 1: ", soln.find_median_sorted_arrays([1, 2, 3], [4, 5, 6]))
print("\n\n")
print("case 2: ", soln.find_median_sorted_arrays([1, 2], [4, 5, 6]))
