def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gascount = len(gas)
        ibeststartposition = gascount
        balancegasfromstart = 0
        totalbalancegas = 0
        for i in range(gascount):
            balancegasfromstart = balancegasfromstart + gas[i] - cost[i]#2
            totalbalancegas = totalbalancegas + gas[i] - cost[i]#2
            # this is not the right starting position
            if balancegasfromstart < 0:
                ibeststartposition = gascount
                balancegasfromstart = 0
            elif ibeststartposition > i:
                ibeststartposition = i
        if totalbalancegas < 0:
            return -1
        else:
            return ibeststartposition