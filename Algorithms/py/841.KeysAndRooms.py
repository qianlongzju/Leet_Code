class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        q, visited = [0], {0}
        while q:
            room = q.pop(0)
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    q.append(key)
        return len(visited) == len(rooms)
