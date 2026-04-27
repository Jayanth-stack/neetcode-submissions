class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)

        for strings in strs:
            char_counter = [0] * 26
            for char in strings:
                char_counter[ord(char) - ord('a')] +=1
            
            key = tuple(char_counter)

            group_anagrams[key].append(strings)
        
        return list(group_anagrams.values())

