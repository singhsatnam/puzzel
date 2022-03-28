def _parse_string(s):
    # building essentially a list of useful groups of |*...*|,
    # so for example *|*|***|*|* becomes [(1,3),(3,7),(7,9)]
    a = []
    prev = -1
    for i in range(len(s)):
        if s[i] == '|':
            if prev >= 0:
                a.append((prev, i))
            prev = i

    return a


def solution(s, starts, ends):
    # we only parsing the string once
    a = _parse_string(s)
    ans = []
    for i in range(len(starts)):
        start, end = starts[i] - 1, ends[i] - 1
        cnt = 0
        # for every interval, check
        # if we can include it or not
        for e in a:
            i_start, i_end = e
            if i_start >= start and i_end <= end:
                # if this compartment is fully inside
                # our given interval, then include it
                cnt += i_end - i_start - 1
            elif start > i_end:
                # some optimization, to break early
                break
        ans.append(cnt)
    return ans


print(solution('|**|*|*', [1, 1], [5, 6]))
