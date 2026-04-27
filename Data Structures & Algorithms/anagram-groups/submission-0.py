class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)

        for s in strs:
            char_counter = [0]*26
            for char in s:
                char_counter[ord(char) - ord('a')]+=1
            
            key = tuple(char_counter)

            anagrams_dict[key].append(s)
        
        return list(anagrams_dict.values())