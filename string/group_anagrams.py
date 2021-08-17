import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 처음 풀이
        # sorted_strs = [''.join(sorted(s)) for s in strs]
        # result = []
        # for word in set(sorted_strs):
        #     word_index = []
        #     for i, d in enumerate(sorted_strs):
        #         if word == d:
        #             word_index.append(strs[i])
        #     result.append(word_index)
        #
        # return result

        # defaultdict를 활용한 방식
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))

