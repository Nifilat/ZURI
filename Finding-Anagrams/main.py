# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if (len(word) == len(anagram)):
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)

        if(sorted_word == sorted_anagram):
            return True
        else:
            return False

    else:
        return False
    # [assignment] Add your code here


print(find_anagram('below', 'elbow'))
