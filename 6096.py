class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions = sorted(potions, reverse=True)
        spells = [(i, spell) for i, spell in enumerate(spells)]
        spells = sorted(spells, key=lambda x: x[1])
        #print(spells)
        result = []
        j = 0
        for i, spell in spells:
            while j < len(potions):
                if spell * potions[j] < success:
                    result.append((i, j))
                    break
                else:
                    j += 1
            if j == len(potions):
                result.append((i, j))
        #print(result)
        return [b for a, b in sorted(result)]
        
