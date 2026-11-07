class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReq = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            preReq[course].append(pre)

        visiting = set()  # on the current DFS path
        doable = set()    # proven finishable

        def dfs(c):
            if c in visiting:   
                return False
            if c in doable:     
                return True

            visiting.add(c)
            for p in preReq[c]:
                if dfs(p)==False:
                    return False
            visiting.remove(c)

            doable.add(c)
            return True

        for c in range(numCourses):
            if dfs(c)==False:
                return False
        return True