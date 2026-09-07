class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for x in s:
            if x.isalnum():
                word+=x.lower()
        i = 0
        j = len(word)-1
        print(word)
        print(i,j)
        while i!=j and i<len(word) and j>=0:
            print(i,j)
            if word[i]!=word[j]:
                return False
            i+=1
            j-=1
        return True