# def battleship(N, s, t):
#     matrix = [[0] * N for _ in range(N)]
#
#     ships = s.split(",")
#     hits = t.split(" ")
#     for i in range(len(ships)):
#         ships[i] = ships[i].split(" ")
#
#     original = set()
#     for i in range(len(ships)):
#         top_left = ships[i][0]
#         bottom_right = ships[i][1]
#         top_x = int(top_left[:-1]) - 1
#         top_y = ord(top_left[-1]) - 65
#         bottom_x = int(bottom_right[:-1]) - 1
#         bottom_y = ord(bottom_right[-1]) - 65
#         vertical = bottom_x - top_x + 1
#         horizonal = bottom_y - top_y + 1
#         for m in range(top_x, top_x + vertical):
#             for n in range(top_y, top_y + horizonal):
#                 matrix[m][n] = i + 1
#         original.add(i + 1)
#
#     hitted = set()
#     for hit in hits:
#         x = int(hit[:-1]) - 1
#         y = ord(hit[-1]) - 65
#         if matrix[x][y] != 0:
#             hitted.add(matrix[x][y])
#             matrix[x][y] = 0
#
#     updated = set()
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j] != 0:
#                 updated.add(matrix[i][j])
#
#     sunk = len(original - updated)
#     hitted_but_not_sunk = len(hitted & updated)
#
#     return sunk, hitted_but_not_sunk
#
#


#23280666306665

def battleship(n, s, t):
    # map to maintain ship with its cells
    battle_ground = {}

    ships = s.split(',')
    ships = [s.split(' ') for s in ships]

    ship_id = 0
    for ship in ships:
        cells = []
        x1, y1 = ship[0][0], ship[0][1]
        x1= int(x1) - 1
        y1 = ord(y1) - 65

        x2, y2 = ship[1][0], ship[1][1]
        x2 = int(x2) - 1
        y2 = ord(y2) - 65

        for x in range(x2 - x1 + 1):
            for y in range(y2 - y1 + 1):
                cells.append((x + x1, y + y1))

        battle_ground[ship_id] = cells
        ship_id += 1


    target = t.split(',')
    target_cells = []
    for t in target:
        x = t[0]
        y = t[1]
        x = int(x) - 1
        y = ord(y) - 65
        target_cells.append((x, y))

    sunk = 0
    hit_not_sunk = 0
    for shipid in battle_ground:
        # for a ship if all cells exist in target_cells, it got sunk
        if len(set(battle_ground[shipid]) - set(target_cells)) == 0:
            sunk += 1
        # if few cells exist in target_cells, it got hit but not sunk
        elif 0 < len(set(battle_ground[shipid]) - set(target_cells)) < len(battle_ground[shipid]):
            hit_not_sunk += 1

    return sunk, hit_not_sunk

print(battleship(12, "1A 2A,12A 12A", "12A"))
print(battleship(3, "1A 1B,2C 2C", "1B"))