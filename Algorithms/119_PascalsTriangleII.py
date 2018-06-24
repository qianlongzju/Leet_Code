class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        row = [1, 1]
        for i in range(2, rowIndex+1):
            old_row = row[:]
            row = [1]
            for j in range(1, i):
                row.append(old_row[j-1] + old_row[j])
            row.append(1)
        return row
