class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        m = str(x)
        l = len(m)
        one = m[:l//2][::-1]
        two = m[l//2:]
        if (l%2!=0):
            two = m[(l//2)+1:]

        if one==two:
            return True
        else:
            return False
