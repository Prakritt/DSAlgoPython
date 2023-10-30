#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        temp_dict = {}
        for (index,ch) in enumerate(s):
            if ch in temp_dict:
                temp_dict[ch]+=1
            else:
                temp_dict[ch] = 1
        for index,ch in enumerate(s):
            if temp_dict[ch] == 1:
                return index

        return -1
    