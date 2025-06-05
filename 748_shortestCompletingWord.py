from typing import List

def shortestCompletingWord(licensePlate: str, words: List[str]) -> str:
    counter = {}
    for i in licensePlate:
        if i.isalpha():
            i = i.lower()
            counter[i] = counter.get(i, 0) + 1
    result = None
    for word in words:
        new_counter = {}
        for char in word:
            if char in counter.keys():
                new_counter[char] = new_counter.get(char, 0) + 1
        if all(new_counter.get(char, 0) >= count for char , count in counter.items()):
            if result is None or len(word) < len(result):
                result = word
    return result








print(shortestCompletingWord(
    licensePlate = "1s3 PSt",
    words = ["step","steps","stripe","stepple"])
)

