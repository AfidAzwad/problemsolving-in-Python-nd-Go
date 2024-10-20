def canFinish(numCourses, prerequisites):
    preMap = { i:[] for i in range(numCourses)}

    for course, pre_req in prerequisites:
        preMap[course].append(pre_req)

    visitSet = set()

    def dfs(course):
        if course in visitSet:
            return False
        if preMap[course] == []:
            return True
        visitSet.add(course)
        for pre_req in preMap[course]:
            if not dfs(pre_req): return False
        visitSet.remove(course)
        preMap[course] = []
        return True

    for course in range(numCourses):
        if not dfs(course): return False

    return True

# prerequisites = [[1,0]]
# numCourses = 2
prerequisites = [[1,0],[0,1]]
numCourses = 2
print(canFinish(numCourses,prerequisites))

# Time Complexity: O(n+p)
# Space Complexity: O(n)

# Think courses as vertices or nodes of a graph and prerequisite is an edge.

# approach : DFS in Graph [ is when there is no prerequisite then dfs returns True and after checking all ]
# prerequisite list will be empty so we can track if we can do all the courses or not at the end.

# edge case : if there is a cycle found then it is impossible to complete the courses and return False
