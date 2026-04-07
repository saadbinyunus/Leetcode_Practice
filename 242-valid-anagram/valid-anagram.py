class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Hashmap Frequency (key:value) -> (character:frequency)
        
        #Frequency Hashmap
        freq_map1 = {}
        freq_map2 = {}

        #iterate string then add character to hashmap with default frequency 1. 
        #Check if it character already exists in map if so then increase count.
        for char1 in s:
            if char1 in freq_map1:
                freq_map1[char1] += 1
            else:
                freq_map1[char1] = 1

        for char2 in t:
            if char2 in freq_map2:
                freq_map2[char2] += 1
            else:
                freq_map2[char2] = 1

        #Now compare frequencies of both hashtables
        #if equal then valid anagram otherwise false
        return freq_map1 == freq_map2
