class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        VOWEL = 'aeiou'
        res = 0
    
        for word in words[left:right+1]:
            if (word[0] in VOWEL) and (word[-1] in VOWEL):
                res += 1

        return res