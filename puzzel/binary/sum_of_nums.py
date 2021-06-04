class Solution:
    def getSum(self, a: int, b: int) -> int:
        print("A:", a, " in bin:", bin(a), "       b:", b, " in bin:",  bin(b))
        mask = 0xffffffff
        print(bin(mask))
        while b & mask > 0:
            print("b:", b, " in bin:", bin(b))
            c = (a & b) << 1
            print("c:", c," in bin:", bin(c))
            print(bin(a), "^ ", bin(b))
            a = a ^ b
            print("a:",a, " in bin:", bin(a))
            b = c

        return (a & mask) if b > 0 else a


soln = Solution()
print(soln.getSum(-2, 3))
# print(bin(-2))
# print(bin(2))
# print(bin(-3))
# print(bin(3))
