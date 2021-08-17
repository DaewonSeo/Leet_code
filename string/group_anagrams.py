class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        sorted_strs = [''.join(sorted(s)) for s in strs]
        result = []
        for word in set(sorted_strs):
            word_index = []
            for i, d in enumerate(sorted_strs):
                if word == d:
                    word_index.append(strs[i])
            result.append(word_index)

        return result


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))

