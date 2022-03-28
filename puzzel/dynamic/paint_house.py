def print_arr(arr):
    print(arr)
    # for ele in color:
    #     print(ele) 
color = [[1,2,3],[1,2,3],[3,3,1]]
print_arr(color)
print()
def min_cost(color) -> int:
    for i in range(1, len(color)):
        
        color[i][0] += min(color[i - 1][1], color[i - 1][2])
        color[i][1] += min(color[i - 1][0], color[i - 1][2])
        color[i][2] += min(color[i - 1][0], color[i - 1][1])
    n = len(color) - 1
    print_arr(color)
    print(min(min(color[n][0], color[n][1]), color[n][2]))
    return min(min(color[n][0], color[n][1]), color[n][2])

print(min_cost(color))