def split_words(input_string):
    words = []
    current_word_start_index = 0
    current_word_length = 0

    for i, char in enumerate(input_string):
        if char.isalpha():
            if current_word_length == 0:
                current_word_start_index = i
            current_word_length += 1
        else:
            word = input_string[current_word_start_index:current_word_start_index + current_word_length]
            words.append(word)
            current_word_length = 0
    return words



def add_words_to_dictionary(word):
    words_to_counts = {}

    if word in words_to_counts:
        words_to_counts[word] += 1
    else:
        words_to_counts[word] = 1


split_words('After beating the eggs, Dana read the next step:')
