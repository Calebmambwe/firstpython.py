def reverseWords(s):
    list = []
    list[:0] = s
    i = 0
    j = len(s) - 1
    while i < j:
        list[i], list[j] = list[j], list[i]
        i += 1
        j -= 1


s = "Let's take LeetCode contest"
reverseWords(s)