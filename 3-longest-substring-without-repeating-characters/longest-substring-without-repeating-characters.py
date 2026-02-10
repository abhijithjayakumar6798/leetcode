class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        seen={}
        max_len=0
        for right,ch in enumerate(s):
            if ch in seen and seen[ch]>=left:
                left=seen[ch]+1
            seen[ch]=right
            max_len=max(max_len,right-left+1)
        return max_len