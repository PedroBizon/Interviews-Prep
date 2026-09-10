# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placeable_flowers = 0

        # Dealing with Edge Cases:
        if len(flowerbed)==1:
            if flowerbed[0] == 0:
                placeable_flowers = 1
            else:
                placeable_flowers = 0

            return placeable_flowers >= n
        
        elif len(flowerbed) == 2:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                placeable_flowers = 1
            else:
                placeable_flowers = 0

            return placeable_flowers >= n
        
        # General cases -> len(flowerbed) >= 3
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 1:
                flowerbed[i-1] = 2
                flowerbed[i+1] = 2

        if flowerbed[0] == 0:
            flowerbed[0] = 1
            placeable_flowers += 1

        flowerbed[1] = 1

        if flowerbed[-1] == 0:
                flowerbed[-1] = 1
                placeable_flowers += 1

        flowerbed[-2] = 1

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0:
                flowerbed[i-1] = 1
                flowerbed[i+1] = 1

                placeable_flowers += 1

        if placeable_flowers >= n:
            return True

        else: 
            return False
        
# This solution goes through the array 2 times on every execution.
# The first time, it marks the places where flowers can't be placed
# The second time, it "plants" the plants, updating the counter and marking more places as unfit for planting
# So, the complexity is O(2n), wich is O(n)