"""
PROBLEM   : Longest Common Prefix
DIFFICULTY: easy
PATTERN   : string comparison
TRIGGER   : common prefix, array of strings, trim
INTUITION : Use the first string as the running prefix. For each subsequent string, trim the
            prefix character by character until it matches the start of that string.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        longest = strs[0]
        new_longest = ""
        i = 0

        if len(strs) <= 1:
            return strs[0]
        
        while i < len(strs) - 1:
            print(i)
            for j in range(1, len(min(longest, strs[i+1])) + 1):
                print(new_longest)
                print(f"longest[:{j}] = {longest[:j]} | strs[{i+1}][:{j}] = {strs[i+1][:j]}")
                if longest[:j] == strs[i+1][:j]:
                    new_longest = longest[:j]
                    
                    print("Longest:",new_longest)  
                    continue
                new_longest = longest[:j-1]
                break
            i += 1
        
        return new_longest
    

strs = ["aaa","aa","aaa"]

result = Solution.longestCommonPrefix(object, strs)

print(result)