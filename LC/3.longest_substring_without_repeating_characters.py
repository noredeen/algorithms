class Solution:

    # Left edge does the "seeking"
    def len_longest_substr(self, s: str) -> int:
        left = 0
        max_length = 0
        while left+max_length < len(s):
            chars = set()
            i = left
            temp_length = 1
            right = left+temp_length
            while i < right and right <= len(s) and s[i] not in chars:
                chars.add(s[i])
                right += 1
                i += 1

            max_length = max(max_length, right-left-1)
            left += 1

        return max_length

    # Right edge does the "seeking". When right hits dupe, left catches
    # up to the first occ of the dupe (undoing the counts), restart seeking from there
    # O(2n) = O(n) time. Worst case, every char will be viewed twice
    # TODO: Space ???
    def more_organized(self, s: str) -> int:
        left = right = 0
        max_len = 0
        chars = [0] * 128

        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            max_len = max(max_len, right-left+1)
            right += 1

        return max_len

    # if s[j] has a dup in [i..j] at j', then we can move to [j'..j]
    def optimized(self, s: str) -> int:
        max_len = 0
        mp = {}

        i = 0
        for j in range(len(s)):
            if s[j] in mp:
                # sometimes mp[s[j]] is behind i, so we keep i in that case
                i = max(mp[s[j]], i)

            max_len = max(max_len, j-i+1)
            mp[s[j]] = j + 1

        return max_len


print(Solution().more_organized("pwwkew"))
print(Solution().more_organized("abcabcbb"))
print(Solution().more_organized("bbbbb"))
print(Solution().more_organized("b"))
