# def reverse_array(Str_n):
#     first = 0
#     last = len(Str_n) - 1
#     rev_list = []
#     while first <= last:
#         rev_list.append(Str_n[last])
#         # print(rev_list)
#         # first += 1
#         last -= 1
#
#     return print(''.join(rev_list))
#
# message = [ 'c', 'a', 'k', 'e', ' ','p', 'o', 'u', 'n', 'd', ' ','s', 't', 'e', 'a', 'l' ]
#
# reverse_array("This is the day")

def reverse_words(message):
    reverse_characters(message, 0, len(message) - 1)

    current_word_start_index = 0

    for i in range(len(message) + 1 ):
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            current_word_start_index = i + 1 



def reverse_characters(message, left_index, right_index ):

    while left_index < right_index:
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index += 1
        right_index -= 1

    return message


