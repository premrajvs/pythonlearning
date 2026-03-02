""" There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true """

from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # find max distance
        maxd = 0
        for numPassengersi, fromi, toi in trips:
            if toi > maxd:
                maxd = toi
        
        locations = [0]*maxd
        #print(locations)
        for numPassengersi, fromi, toi in trips:
            if numPassengersi > capacity:
                return False
            locations[fromi-1] = locations[fromi-1] + numPassengersi
            if toi <= maxd:
                #print(toi)
                locations[toi-1] = locations[toi-1] - numPassengersi
                #print(locations)

        for i in range(1,len(locations)):
            locations[i] = locations[i] + locations[i-1]
            if locations[i]>capacity:
                return False
        return True

if __name__ == "__main__":
    c1 = Solution()
    c1.carPooling([[2,1,5],[3,3,7]],4)
