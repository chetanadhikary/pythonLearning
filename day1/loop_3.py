
words_split = str_words.lower().split()
dict_count = {}
for word in words_split:
    dict_count[word] = dict_count.get(word,0) +1
print(dict_count)
