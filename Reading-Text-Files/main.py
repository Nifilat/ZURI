# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import re


def read_file_content(filename):
    f = open(filename, "r")
    read = f.read()
    f.close()

    return read


print(read_file_content("story.txt"))


# [assignment] Add your code here


def count_words():
    txt = read_file_content("./story.txt")
    lowercase = txt.lower()
    text_count = {}

    split_txt = re.split('[?.,\n\t&! ]', lowercase)

    for word in split_txt:
        if word in text_count:
            text_count[word] += 1
        else:
            text_count[word] = 1

    return text_count


print(count_words())


# [assignment] Add your code here
