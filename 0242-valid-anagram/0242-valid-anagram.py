from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
        
        
        
        
        #if len(s) != len(t):
         #   return False
    
        #for ch in set(s):
         #   if s.count(ch) != t.count(ch):
          #      return False
        #return True
      
           