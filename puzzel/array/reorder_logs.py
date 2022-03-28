from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        https://leetcode.com/problems/reorder-data-in-log-files/solution/
        '''

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1,)

        return sorted(logs, key=get_key)

