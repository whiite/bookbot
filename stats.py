def word_count(content):
    return len(content.split())


def char_count(content):
    chars = {}

    for char in content.lower():
        if char not in chars:
            chars[char] = 0
        chars[char] += 1

    return chars


def __sort_on(dict):
    return dict["num"]


def content_chars(content):
    char_list = []

    chars = char_count(content)
    for char in chars:
        char_list.append({"char": char, "num": chars[char]})

    char_list.sort(reverse=True, key=__sort_on)
    return char_list
