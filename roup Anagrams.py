class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram = {}

        for word in strs:
            key = tuple(sorted(word))

            if key in anagram:
                anagram[key].append(word)
            else:
                anagram[key] = [word]

        return list(anagram.values())
