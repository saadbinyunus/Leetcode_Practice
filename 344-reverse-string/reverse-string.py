class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # we will use 2 pointers approach , s is the name of list(array) of the strings
        left = 0            #1st letter in list
        right = len(s)-1    #Last Letter in list

        # we must swap the 1st and last then increment left and decrement right then swap again till we reach the mid point
        # mid point is when left_index is larger than right_index so use while loop
        while left < right:
            #now we swap, first save the left element in var x to replace right later
            x = s[left]
            s[left] = s[right]
            s[right] = x
            #increment left
            left+=1
            #decrement right
            right-=1