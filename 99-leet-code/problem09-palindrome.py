class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        m = len(s) // 2
        for i in range(0, m):
            if s[i] != s[-(i+1)]:
                return False
        return True


s = Solution()
print(s.isPalindrome(-121))
