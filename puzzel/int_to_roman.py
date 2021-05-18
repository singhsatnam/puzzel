def intToRoman(self, num: int) -> str:
    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    combs = [[0], [0, 0], [0, 0, 0], [0, 1], [1], [1, 0], [1, 0, 0], [1, 0, 0, 0], [0, 2]]
    ret = ""
    itr = 0
    while num > 0:
        tmp = num % 10
        num = num // 10
        tmplet = ""
        if tmp > 0:
            for l in combs[tmp - 1]:
                tmplet += romans[l + itr]
            ret = tmplet + ret

        itr += 2

    return ret

