def some_function(lst):
    d = {}
    max_ = float('-inf')
    for i in range(len(lst)):
        word = lst[i]
        words = word.split()
        d[words[1]] = num_words(lst[i])
        max_ = max(max_, d[words[1]])
    return get_key(max_, d)


def get_key(val, d):
    for key, value in d.items():
        if val == value:
            return key
    return "key doesn't exist"


def num_words(lst):
    words = lst.split()
    counter = 0
    i = 0
    while i < len(words):
        counter += 1
        i += 1
    return counter - 2

some_function(["[10:00] <John> This is it", "[11:00] <Ben> This it"])