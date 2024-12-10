def single_root_words(root_word, *other_words):
    same_words = []
    root_w = root_word.lower()

    for word in other_words:
        other_w = word.lower()
        txt = other_w.find(root_word)
        if txt > -1:
            same_words.append(word)

    for word in other_words:
        other_w = word.lower()
        txt = root_w.find(other_w)
        if txt > -1:
            same_words.append(word)

    print(same_words)
    return same_words

same = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
