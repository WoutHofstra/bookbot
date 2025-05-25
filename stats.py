
def get_num_words(book_text):

    split_text = book_text.split()
    num_words = len(split_text)

    return num_words

def get_num_chars(book_text):
    num_chars = {}

    lower_cases = book_text.lower()
    for i in lower_cases:
        if i in num_chars:
            num_chars[i] += 1
        else:
            num_chars[i] = 1

    return num_chars

def sort_on(num_chars):
    return num_chars["num"]

def sorting_chars(num_chars):

    char_list = []


    for char in num_chars:
        count = num_chars[char]
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)

    return char_list
