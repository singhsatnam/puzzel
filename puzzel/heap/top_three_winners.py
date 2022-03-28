results="""\
Christania Williams      11.80
Marie-Josee Ta Lou       10.86
Elaine Thompson          10.71
Tori Bowie               10.83
Shelly-Ann Fraser-Pryce  10.86
English Gardner          10.94
Michelle-Lee Ahye        10.92
Dafne Schippers          10.90
"""

import heapq

results_list = results.splitlines()
print(type(results_list))
# print(results_list[0].split(sep="", ))
# res = heapq.nlargest(3, results_list, key=lambda x: x.split())

# print(type(res))

arr = [3, 1, 7, 6, 2, 9, 4, 8, 5]
[print(x) for x in arr]
# arr_h = heapq.heapify(arr)
print()
[print(x) for x in arr]
# print(arr_h)
print([heapq.heappop(arr) for x in range(0, len(arr))])