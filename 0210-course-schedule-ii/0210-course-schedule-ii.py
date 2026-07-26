class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict (list)
        order = []
        for a,b in prerequisites: 
            g[a].append(b)

        UNVISITED, VISITING,VISITED = 0,1,2
        states = [UNVISITED] * numCourses

        def dfs(node):
            state = states[node]
            if state == VISITING:
                return False
            if state == VISITED:
                return True 

            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False
            states[node] = VISITED
            order.append(node)
            return True


        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order

        
        