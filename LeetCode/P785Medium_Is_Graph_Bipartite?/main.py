from typing import List
# Problem: https://leetcode.com/problems/is-graph-bipartite/


class Solution:
    def isBipartite2(self, graph: List[List[int]]) -> bool:
        '''O(V+E) runtime, O(V) space solution

        Complexity Analysis:
        - The algorithm traverses visits every node at least once and traverses
        the nodes edges, making the time complexity O(V+E)
        - The algorithm stores a color for every node giving it a space
        complexity of O(V)

        Solution Explanation:
        The solution iterates through each vertex in the graph, running a dfs
        if the vertex hasn't been seen yet. We expect that between every
        recursive dfs call, the color should switch between -1 and 1. So for
        every vertex, we run a dfs on all neighbors to check that the neighbors
        of the current node are the opposite color from the current color
        (`-color`). We use all to easily check that all dfs calls return True,
        meaning that the graph is bipartite, or if any returns false,
        nonbipartite.
        '''
        colored = {}

        def dfs(color, node):
            if node in colored:
                # If a node has been seen before, we check that the color is what we expect
                return color == colored[node]
            else:
                # If a node hasn't been seen yet, we "color" it
                colored[node] = color

                # continue dfs on all neighbors
                # we change the color between 1 and -1 because we expect neighbors to be in opposite subgroup
                return all(dfs(-color, nb) for nb in graph[node])
        # Run our dfs on every node if not yet explored
        return all(node in colored or dfs(1, node) for node in range(len(graph)))

    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}

        q = []

        for i in range(len(graph)):
            # for every node in graph

            if i not in color:
                # if not yet explored, set its color
                color[i] = 1
                q.append(i)

                # process queue
                while q:
                    # anything in the queue is already guaranteed to be colored because we only add to queue after coloring the node.
                    node = q.pop(0)

                    # explore its neighbors
                    for neighbor in graph[node]:
                        if neighbor in color:
                            # check that color is opposite of curr node
                            if color[node] != -color[neighbor]:
                                return False
                        else:
                            # node not colored. Let's color it and add it to queue to look at next.
                            color[neighbor] = -color[node]
                            q.append(neighbor)

        # got through all nodes successfully without finding a color mismatch.
        # graph is bipartite
        return True
