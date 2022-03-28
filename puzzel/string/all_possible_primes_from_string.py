# https://www.geeksforgeeks.org/find-all-possible-ways-to-split-the-given-string-into-primes/
# Python 3 program to Find all the
# ways to split the given string
# into Primes.
primes = [True] * 1000001
maxn = 1000000


# Sieve of Eratosthenes
def sieve():
    primes[0] = primes[1] = 0
    i = 2

    while i * i <= maxn:
        if (primes[i]):
            for j in range(i * i,
                           maxn + 1, i):
                primes[j] = False
        i += 1


# Function Convert integer
# to binary string
def toBinary(n):
    r = ""
    while (n != 0):
        if (n % 2 == 0):
            r = "0" + r
        else:
            r = "1" + r
        n //= 2

    if (r == ""):
        return "0"
    return r


# Function print all the all the
# ways to split the given string
# into Primes.
def PrimeSplit(st):
    cnt = 0

    # To store all
    # possible strings
    ans = []
    bt = 1 << (len(st) - 1)
    n = len(st)

    # Exponetnital complexity
    # n*(2^(n-1)) for bit
    for i in range(bt):
        temp = toBinary(i) + "0"
        j = 0
        x = n - len(temp)
        while (j < x):
            temp = "0" + temp
            j += 1

        j = 0
        x = 0
        y = -1

        sp = ""
        tp = ""
        flag = 0

        while (j < n):
            sp += st[j]
            if (temp[j] == '1'):
                tp += sp + ','
                y = int(sp)

                # Pruning step
                if (not primes[y]):
                    flag = 1
                    break
                sp = ""
            j += 1

        tp += sp

        if (sp != ""):
            y = int(sp)
            if (not primes[y]):
                flag = 1

        if (not flag):
            ans.append(tp)

    if (len(ans) == 0):
        print(-1)

    print(ans)
    # for i in ans:
    #     print()


# Driver code
if __name__ == "__main__":
    st = "11373"
    sieve()
    PrimeSplit(st)

