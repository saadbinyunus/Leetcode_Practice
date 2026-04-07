class Solution:
    def isValid(self, s: str) -> bool:
        # HashMap & Stack

        # Create a HashMap where the key:value is same as (closing:opening) parenthesis to match
        #This is just a "Cheat Sheet." When the code sees a ')', it looks at the cheat sheet, sees that the matching partner is 
        # '(', and then checks if that partner is currently sitting on top of the stack.
        hashmap = { ")" : "(" , "}" : "{" , "]" : "[" }
        #Stack to keep track of parenthesis
        #When you see an opening bracket (, [, or {, you push it onto the stack.
        #When you see a closing bracket ), ], or }, you look at the top of the stack.
        stack = []

        for char in s:
            #Check if character is a closing bracket
            if char in hashmap:
                #If the top matches your closing bracket, you pop it off and keep going.
                #If it doesn't match, or the stack is empty, the string is invalid
                if not stack or stack.pop() != hashmap[char]:
                    return False
            #If its character is an opening bracket then just push to stack
            else:
                stack.append(char)

        # CRITICAL: Only True if the stack is empty!
        return not stack