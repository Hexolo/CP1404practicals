def word_count(text):
    count = {}
    words = text.split()

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    return count


text = input("Text: ")
word_to_count = word_count(text)
for word, count in word_to_count.items():
    print(word, ":", count)
