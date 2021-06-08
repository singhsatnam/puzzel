import collections


class Node:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def cloneGraph_bfs(self, node: 'Node') -> 'Node':
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:  # neighbor is not visited
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    def cloneGraph_iter_dfs(self, node):
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        stack = [node]
        while stack:
            node = stack.pop()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    stack.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy

    def cloneGraph_dfs_recursive(self, node):
        if not node:
            return
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy}
        self.dfs(node, dic)
        return nodeCopy

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])

# class Solution(object):
#         '''
#         https://leetcode.com/problems/clone-graph/
#         '''
#     def cloneGraph1(self, node):  # DFS iteratively
#         if not node:
#             return node
#         m = {node: Node(node.val)}
#         stack = [node]
#         while stack:
#             n = stack.pop()
#             for neigh in n.neighbors:
#                 if neigh not in m:
#                     stack.append(neigh)
#                     m[neigh] = Node(neigh.val)
#                 m[n].neighbors.append(m[neigh])
#         return m[node]
#
#     def cloneGraph2(self, node):  # BFS
#         if not node:
#             return node
#         m = {node: Node(node.val)}
#         deque = collections.deque([node])
#         while deque:
#             n = deque.popleft()
#             for neigh in n.neighbors:
#                 if neigh not in m:
#                     deque.append(neigh)
#                     m[neigh] = Node(neigh.val)
#                 m[n].neighbors.append(m[neigh])
#         return m[node]
#
#     def cloneGraph(self, node):  # DFS recursively
#         if not node:
#             return node
#         m = {node: Node(node.val)}
#         self.dfs(node, m)
#         return m[node]
#
#     def dfs(self, node, m):
#         for neigh in node.neighbors:
#             if neigh not in m:
#                 m[neigh] = Node(neigh.val)
#                 self.dfs(neigh, m)
#             m[node].neighbors.append(m[neigh])
