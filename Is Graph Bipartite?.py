class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        color = [0] * n  # Initialize colors for nodes
        
        def dfs(node, c):
            color[node] = c
            for neighbor in graph[node]:
                if color[neighbor] == c:
                    return False  # Conflict in coloring
                if color[neighbor] == 0 and not dfs(neighbor, -c):
                    return False  # Recurse with opposite color
                
            return True
        
        for node in range(n):
            if color[node] == 0:  # If node is not colored
                if not dfs(node, 1):  # Start DFS from the node with color 1
                    return False  # If conflict in coloring occurs
        
        return True

