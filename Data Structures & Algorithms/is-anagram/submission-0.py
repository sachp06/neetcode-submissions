class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        seenLetters = {} #frequency counter for each letter
        
        for char in s:
            try:
                seenLetters[char] += 1
            except KeyError:
                seenLetters[char] = 1
        for char in t:
            if char not in seenLetters:
                return False
            else:
                seenLetters[char] -= 1
            if seenLetters[char] < 0:
                return False
        return True



            