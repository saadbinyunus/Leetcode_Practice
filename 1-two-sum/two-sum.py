class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Hashmap
        # What we can do is we can take each element in the array then subtract it from the target
        # Check the hashmap if the remainder value exists then its true

        hashmap = {}

        for idx,n in enumerate(nums): # keeps value and index
            
            remainder = target - n

            if remainder in hashmap: #check if remainder in hashmap
                return [hashmap[remainder],idx] # if found returns index of elements in original array

            else:
                hashmap[n] = idx #add the value and its index (in original array) into hashmap for next iteration check

