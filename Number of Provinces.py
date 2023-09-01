class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        def dfs(node):
            visited[node] = True
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        
        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)
        
        return provinces
