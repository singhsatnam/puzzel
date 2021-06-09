def isRobotBounded(instructions: str) -> bool:
    curr_pos = [0, 0]
    curr_dir = "N"
    directions = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}

    # Calculate the final vector of how the robot travels after executing all instructions once - it consists of a change in position plus a change in direction.
    for char in instructions:
        if char == "G":
            curr_pos[0] += directions[curr_dir][0]
            curr_pos[1] += directions[curr_dir][1]
        elif (curr_dir == "N" and char == "L") or (curr_dir == "S" and char == "R"):
            curr_dir = "W"
        elif (curr_dir == "W" and char == "L") or (curr_dir == "E" and char == "R"):
            curr_dir = "S"
        elif (curr_dir == "S" and char == "L") or (curr_dir == "N" and char == "R"):
            curr_dir = "E"
        elif (curr_dir == "E" and char == "L") or (curr_dir == "W" and char == "R"):
            curr_dir = "N"

    # The robot stays in the circle iff (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.``
    return curr_dir != "N" or curr_pos == [0, 0]


print(isRobotBounded("GGLLGG"))
