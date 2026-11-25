class Solution:
    def isPalindrome(self, s: str) -> bool:
        refined_str = (''.join(e for e in s if e.isalnum())).lower()
        reverse_str = refined_str[::-1]
        
        return refined_str == reverse_str