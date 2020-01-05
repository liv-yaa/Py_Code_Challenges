# leetcodePracJan2020.py

class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        s = text.split(" ")    
        return [s[i + 2] for i in range(len(s) - 2) if s[i] == first and s[i + 1] == second]
        
            
        
        
if __name__ == "__main__":
	s = Solution()

	print(s.findOcurrences("alice is a good girl she is a good student", "a", "good"))
