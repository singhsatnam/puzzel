def recursive_dfs(graph, source, path=[]):
    print("source: ", source, "// path:", path)
    if source not in path:
        path.append(source)
        print("appended path: ", path)
        if source not in graph:
            print("source not in graph :", source, ". returning path: ", path)
            # leaf node, backtrack
            return path
        for neighbour in graph[source]:
            print("for neighbour: ", neighbour)
            path = recursive_dfs(graph, neighbour, path)
            print("loop path: ", path)
    return path


def dfs_non_recursive(graph, source):
    if source is None or source not in graph:
        return "Invalid input"

    path = []
    stack = [source]
    while (len(stack) != 0):
        s = stack.pop()
        if s not in path:
            path.append(s)
        if s not in graph:
            # leaf node
            continue
        for neighbor in graph[s]:
            stack.append(neighbor)
    return " ".join(path)


# graph = {"A": ["B", "C", "D"],
#          "B": ["E"],
#          "C": ["F", "G"],
#          "D": ["H"],
#          "E": ["I"],
#          "F": ["J"]
#          }

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(graph)

path = recursive_dfs(graph, "A")
print("Traversal path: ", path)
