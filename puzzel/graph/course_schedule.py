from typing import List


class CourseSchedule:
    def build_adjacency_list(self, n, edgesList):
        adj_list = [[] for _ in range(n)]
        for c1, c2 in edgesList:
            adj_list[c2].append(c1)
        return adj_list

    def can_finish_stack(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build Adjacency list from Edges list
        adjList = self.build_adjacency_list(numCourses, prerequisites)
        visited = set()

        def hasCycle(v, stack):
            if v in visited:
                if v in stack:
                    # This vertex is being processed and it means we have a cycle.
                    return True
                # This vertex is processed so we pass
                return False

            # mark this vertex as visited
            visited.add(v)
            # add it to the current stack
            stack.append(v)

            for i in adjList[v]:
                if hasCycle(i, stack):
                    return True

            # once processed, we pop it out of the stack
            stack.pop()
            return False

        # we traverse each vertex using DFS, if we find a cycle, stop and return
        for v in range(numCourses):
            if hasCycle(v, []):
                return False

        return True

    def topoBFS(self, numNodes, edgesList):
        # Note: for consistency with other solutions above, we keep building
        # an adjacency list here. We can also merge this step with the next step.
        adjList = self.build_adjacency_list(numNodes, edgesList)

        # 1. A list stores No. of incoming edges of each vertex
        inDegrees = [0] * numNodes
        for v1, v2 in edgesList:
            # v2v1 form a directed edge
            inDegrees[v1] += 1

        # 2. a queue of all vertices with no incoming edge
        # at least one such node must exist in a non-empty acyclic graph
        # vertices in this queue have the same order as the eventual topological
        # sort
        queue = []
        for v in range(numNodes):
            if inDegrees[v] == 0:
                queue.append(v)

        # initialize count of visited vertices
        count = 0
        # an empty list that will contain the final topological order
        topoOrder = []

        while queue:
            # a. pop a vertex from front of queue
            # depending on the order that vertices are removed from queue,
            # a different solution is created
            v = queue.pop(0)
            # b. append it to topoOrder
            topoOrder.append(v)

            # increase count by 1
            count += 1

            # for each descendant of current vertex, reduce its in-degree by 1
            for des in adjList[v]:
                inDegrees[des] -= 1
                # if in-degree becomes 0, add it to queue
                if inDegrees[des] == 0:
                    queue.append(des)

        if count != numNodes:
            return None  # graph has at least one cycle
        else:
            return topoOrder

    def can_finish_queue(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return True if self.topoBFS(numCourses, prerequisites) else False
