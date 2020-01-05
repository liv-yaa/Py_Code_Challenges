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
        
            
    def gcdOfStrings(self, str1, str2):
    	""" For there to be a common divisor between two strings str1 and str2, the shorter string str1 would be a prefix in the longer string str2 since the divisor T is repeated mulitiple times to form the string. """
    	l1, l2 = len(str1), len(str2)

    	if l2 > l1:
			# Ensures the longer string is str1 and the shorter or equal string is s2
			return self.gcdOfStrings(str2, str1)
    	
    	# See if str1 is a prefix of str2
    	if str1[:l2] == str2:
    		if l1 == l2:
    			return str2
    		else:
    			return self.gcdOfStrings(str2, str1[l2:]) # Subtract the prefix

    	return ''
        
if __name__ == "__main__":
	s = Solution()

	# print(s.findOcurrences("alice is a good girl she is a good student", "a", "good"))
	print(s.gcdOfStrings("ABCABC", "ABC")) # "ABC"
	print(s.gcdOfStrings("ABABAB", "ABAB")) # "AB"
	print(s.gcdOfStrings("LEET", "CODE")) # ""