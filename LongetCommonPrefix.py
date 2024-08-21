class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        max_prefix = ''

        if not strs:
            return max_prefix

        min_string = min(strs, key = len)    

        for i in range(0, len(min_string)):
            if all([s.startswith(min_string[:i+1]) for s in strs]):
                max_prefix = min_string[:i+1]
            else:
                break

        return max_prefix            
        
