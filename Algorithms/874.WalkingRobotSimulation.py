class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacles_set = {tuple(obstacle) for obstacle in obstacles}
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir_index = 0
        pos = (0, 0)
        result = 0
        for command in commands:
            if command == -2:
                dir_index = (dir_index - 1) % 4
            elif command == -1:
                dir_index = (dir_index + 1) % 4
            else:
                direction = directions[dir_index]
                for i in range(command):
                    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                    if new_pos in obstacles_set:
                        break
                    pos = new_pos
                result = max(result, pos[0] ** 2 + pos[1] ** 2)
        return result
