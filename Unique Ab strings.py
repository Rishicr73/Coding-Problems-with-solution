#LINK : https://binarysearch.com/problems/Unique-Ab-Strings

#CODE:
class Solution:
    def solve(self, s):
        return (2**(s.count('a')))
      #IF SET HAS 'N' ELEMENTS ,THEN THE NUMBER OF SUBSET OF THE GIVEN SET IS 2**N 
      #Here a can be change but b can,t so here N == count of a.
