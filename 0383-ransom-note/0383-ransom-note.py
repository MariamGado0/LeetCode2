from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in set(ransomNote):
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        return True


      #  magazine_count = Counter(magazine)

      #  for ch in ransomNote:
       #     if magazine_count[ch] > 0:
        #        magazine_count[ch] -= 1
         #   else:
          #      return False
        #return True
        