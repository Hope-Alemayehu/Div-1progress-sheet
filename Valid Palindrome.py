class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # it create extra memory and use built-in function
        # newstr=""

        # for c in s:
        #     if c.isalnum():
        #         newstr+=c.lower()
        
        # if newstr == newstr[::-1]:
        #     return True
        # return False

        #using two pointers techniques

        #a function to determine if a character is alphanumeric
        def alphanum(c):
            return (ord('A')<=ord(c)<=ord('Z') or
                    ord('a')<=ord(c)<=ord('z') or
                    ord('0')<=ord(c)<=ord('9'))
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not alphanum(s[l]):
                l+=1
            while l<r and not alphanum(s[r]):
                r-=1    
            if s[l].lower() != s[r].lower():
                return False

            l+=1
            r-=1
        return True    
