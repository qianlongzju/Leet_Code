class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        q = [(sr, sc)]
        old_color = image[sr][sc]
        visited = []
        while q:
            r, c = q.pop(0)
            visited.append((r, c))
            image[r][c] = newColor
            for r_diff, c_diff in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                new_r, new_c = r + r_diff, c + c_diff
                #print new_r, new_c
                if (new_r >= 0 and new_r < len(image)) and (new_c >= 0 and new_c < len(image[0])) and image[new_r][new_c] == old_color:
                    if (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
            
        return image
