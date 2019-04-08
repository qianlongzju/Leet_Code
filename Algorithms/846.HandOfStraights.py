class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        n = len(hand)
        if n % W != 0:
            return False
        hand.sort()
        while hand:
            s = hand.pop(0)
            for i in range(1, W):
                if s+i in hand:
                    hand.remove(s+i)
                else:
                    return False
        return True
