class Solution:
    def isValid(self, s: str) -> bool:
        #lifo
        stack = []
        for x in s:

            if x=="[" or x=="(" or x=="{":
                stack.append(x)
            
            elif x=="]":
                if stack!=[] and stack.pop()=="[":
                    continue
                else:
                    return False
            elif x=="}":
                if stack!=[] and stack.pop()=="{":
                    continue
                else:
                    return False
            elif x==")":
                if stack!=[] and stack.pop()=="(":
                    continue
                else:
                    return False
        if stack==[]:
            return True
        else:
            return False