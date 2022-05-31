# improvement - treat the array as a one dim array and use one binary search
class Search2DMatrix:
    def __init__(self, arr:list[list[int]]):
        self.arr = arr

    def contains(self, target: int) -> bool:
        row = 0
        col = 0

        num_row = len(self.arr)
        num_col = len(self.arr[0])

        low = 0
        high = num_row - 1
        while(low < high):
            mid = (low + high) // 2
            print("mid: ", mid)
            if self.arr[mid][num_col - 1] == target:
                return True
            elif self.arr[mid][num_col - 1] < target:
                low = mid
            else:
                high = mid

        our_row = high
        low = 0
        high = num_col - 1
        while(low < high):
            mid = (low + high) // 2
            if self.arr[our_row][mid] == target:
                print(our_row, mid)
                return True
            elif self.arr[our_row][mid] < target:
                low = mid
            else:
                high = mid

        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
assert(Search2DMatrix(matrix).contains(target) == True)
