class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        
        def search_list(course, prereq, visited):
            if course in visited:
                return False

            visited.add(course)

            for neighbour in adj_list.get(course, []):
                if neighbour == prereq:
                    return True

                if search_list(neighbour, prereq, visited):
                    return True

            return False
        

        for pair in prerequisites:
            course, prereq = pair[0], pair[1]
            if course == prereq or search_list(course, prereq, set()):
                return False
        

            adj_list[prereq].append(course)
        
        return True