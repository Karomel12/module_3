def single_root_words (root_word, *other_words):
    same_wards = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_wards.append(i)
        if i.lower() in root_word.lower():
            same_wards.append(i)
        else:
            continue
    print(same_wards)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

