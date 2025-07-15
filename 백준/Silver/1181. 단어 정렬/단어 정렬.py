num_words = int(input())

words_list = set(input() for _ in range(num_words))

words_list = list(set(words_list))

words_list.sort(key=lambda x: (len(x), x))

for word in words_list:
    print(word)