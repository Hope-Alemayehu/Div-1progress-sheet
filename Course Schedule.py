class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Create a dictionary preMap to represent prerequisites for each course
        preMap = {i: [] for i in range(numCourses)}

        # Populate the preMap with prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Create a set to keep track of visited courses during DFS
        visitSet = set()

        # Define a recursive function to perform depth-first search (DFS)
        def dfs(crs):
            # If the course is already visited in the current traversal, return False (indicating a cycle)
            if crs in visitSet:
                return False
            # If there are no prerequisites for this course, return True (no cycle)
            if preMap[crs] == []:
                return True

            # Add the course to the visited set to mark it as visited
            visitSet.add(crs)

            # Recursively visit each prerequisite course
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False  # If a cycle is detected, return False

            # Remove the course from the visited set and mark it as completed
            visitSet.remove(crs)
            preMap[crs] = []  # Mark this course as having no prerequisites

            return True  # Return True indicating this course can be completed

        # Iterate through each course and check if it can be completed without a cycle
        for crs in range(numCourses):
            if not dfs(crs):
                return False  # If a cycle is detected, return False

        return True  # If no cycles are detected for all courses, return True
