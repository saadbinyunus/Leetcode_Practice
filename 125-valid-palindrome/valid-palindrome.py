class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Whenever both pointers point to valid characters, we compare them in lowercase form.
        #If at any point they differ, the string is not a palindrome.
        #TWO POINTERS
        left = 0
        right = len(s)-1

        while left < right:

            #We move both pointers inward, skipping any characters that are not letters or digits.
            while left < right and not s[left].isalnum():
                left  += 1

            while left < right and not s[right].isalnum():
                right -= 1    
            
            if s[left].lower() != s[right].lower():
                return False
            
            else:
                left  += 1
                right -= 1

        return True