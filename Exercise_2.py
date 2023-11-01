# ## Problem2:  Equal Row From Minimum Domino Rotations 
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# // Time Complexity : O(n)
# // Space Complexity : O(1) coz constants till 6
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No

class Solution:
    def minDominoRotations(self, tops, bottoms):
        # creating a hasahmap of all elements in tops and bottom to find candidate
        hmap = {}
        trot = brot = 0
        n = len(tops)
        cnt = 0
        # candidate is -1 till found
        candidate = -1
        # iterating over tops and bottom
        for i in range(len(tops)):
            t = tops[i]
            # adding to hmap
            hmap[t] = hmap.get(t, 0) + 1
            # checking if last entered element to hmap is candidate
            cntT = hmap[t]
            if cntT >= n:
                candidate = t
                break
            b = bottoms[i]
            # adding to hmap
            hmap[b] = hmap.get(b, 0) + 1
            # checking if last entered element to hmap is candidate
            cntB = hmap[b]
            if cntB >= n:
                candidate = b
                break
        
        # iterating over tops and bottoms again
        for i in range(n):
            # both not candidate --> not possible
            if tops[i] != candidate and bottoms[i] != candidate:
                return -1
            if tops[i] != candidate:
                trot += 1
            if bottoms[i] != candidate:
                brot += 1
        return min(trot, brot)

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
sol = Solution()
print(sol.minDominoRotations(tops, bottoms))