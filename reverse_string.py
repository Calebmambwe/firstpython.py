def reverse_array(Str_n):
    first = 0
    last = len(Str_n) - 1

    while first <= last:
        rev_list = Str_n[last]
        last -= 1

    return print(rev_list)


reverse_array("Things")
