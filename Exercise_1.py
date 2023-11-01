# ## Problem1: Minimum Path Form String formation
# https://leetcode.com/problems/shortest-way-to-form-string/
# // Time Complexity : O(Nlogk)
# // Space Complexity : O(s)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No
class Solution:
    def shortestWay(self, source, target):
        # Initialize the lengths of the source and target strings.
        sl = len(source)
        tl = len(target)
        # count variable will keep track of the number of times 
        # we need to traverse the source string to form the target string.
        count = 0
        # Initialize pointers for the source and target strings.
        sp = 0
        hash_set = set()
        # Convert the source string into a set for O(1) look-up.
        for i in range(sl):
            hash_set.add(source[i])
        
        # Traverse through each character in the target string.
        for tp in range(tl):
            # If character in target is not present in source --> impossible
            if target[tp] not in hash_set:
                return -1
            while source[sp] != target[tp]:
                sp += 1
                #If we reach the end of the source string 
                # without finding a match, reset the source pointer and 
                # increase the count to indicate that we need to iterate over the source string again.
                if sp == sl:
                    sp = 0
                    count += 1
            # Once a match is found, move the source pointer ahead.
            sp += 1
                # If the source pointer reaches the end of the source string 
                # and we haven't processed all characters in 'target', 
                # then we need to reset 'sp' to 0 and increase the count.
            if sp == sl and tp != tl - 1:
                sp = 0
                count += 1
        return count + 1

source = "abc"
target = "abcbc"
sol = Solution()
print(sol.shortestWay(source, target))