def groupAnagrams(strs):
    annagrams_counter = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in annagrams_counter.keys():
            annagrams_counter[sorted_word] = [word]
        else:
            annagrams_counter[sorted_word].append(word)
    result = []
    for v in annagrams_counter.values():
        result.append(v)
    return result

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# done
