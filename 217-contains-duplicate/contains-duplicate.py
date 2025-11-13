class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Creating a Hashset to store non-duplicates as we iterate the array
        hashset1 = set()

        #Iterating the array
        for n in nums:
            #For every element in array we check if it exists in the Hashset, if it does then the program returns True and exits
            if n in hashset1:
                return True   
        #If not in Hashset then we add that element to Hashset and move on
            hashset1.add(n)
        #If every element is added then it returns False as there are no duplicates
        return False
