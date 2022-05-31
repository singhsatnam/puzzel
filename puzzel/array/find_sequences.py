class ArrayUtil:
    def __init__(self, arr: list) -> list:
        self.arr = arr

    def find_sequence(self) -> list:
        result: list = []
        prev = self.arr[0]
        last_start = self.arr[0]
        curr = 0
        for i in range(1, len(self.arr)):
            curr_sequence = [last_start]
            curr = self.arr[i]

            if prev != curr - 1:
                curr_sequence.append(prev)
                result.append(curr_sequence)
                last_start = curr
            if i == len(self.arr) - 1:
                curr_sequence.append(curr)
                result.append(curr_sequence)

            prev = curr
        return result


arrayUtil = ArrayUtil([1, 3, 4])
print(arrayUtil.find_sequence())
