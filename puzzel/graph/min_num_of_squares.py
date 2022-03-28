# A number can always be represented as a sum of squares of other numbers. Note that 1 is a square and we can always
# break a number as (1*1 + 1*1 + 1*1 + …). Given a number n, find the minimum number of squares that sum to X.
# Python3 program for the above approach
import sys

class BruteForce():
    def calc(self, num):
        # Loop from 1 to n forming all combinations of squares of numbers. Take the numbers which sum up to target.
        # Return the size of the smallest list.
        return

class ArraySoln():
    # Subtract the biggest square possible, then run the function for the remaining number.
    res = sys.maxsize
    def calc(self, num):
        if num == 0:
            return
        for i in range(1, num):
            if i*i <= num:
                res = min(res, 1 + self.calc(num - i**i))
            else:
                break

        return res
        return





class BFSSolution():
    # Function to count minimum
    # squares that sum to n
    def numSquares(self, n):
        visited = [0] * (n + 1)
        q = []
        ans = sys.maxsize
        q.append([n, 0])
        visited[n] = 1
        print(visited)
        print(q)
        while len(q) > 0:
            print(q)
            p = q[0]
            q.pop(0)

            if p[0] == 0:
                ans = min(ans, p[1])
            i = 1
            while i * i <= p[0]:

                # If we are standing at some node
                # then next node it can jump to will
                # be current node-
                # (some square less than or equal n)
                path = p[0] - i * i

                # Check if it is valid and
                # not visited yet
                if path >= 0 and (visited[path] == 0 or path == 0):
                    visited[path] = 1
                    q.append([path, p[1] + 1])

                i += 1
        return ans


bfss = ArraySoln()
print(bfss.calc(12))
