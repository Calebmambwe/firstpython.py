def merge_sort(list_to_sort):
    if len(list_to_sort) < 2:
        return list_to_sort

    mid_index = len(list_to_sort) // 2
    left = list_to_sort[:mid_index]
    right = list_to_sort[mid_index:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    sorted_list = []
    current_index_left = 0
    current_index_right = 0

    while len(sorted_list) < len(left) + len(right):
        if ((current_index_left < len(left)) and
                (current_index_right == len(right) or
                 sorted_left[current_index_left] < sorted_right[current_index_right])):
            sorted_list.append(sorted_left[current_index_left])
            current_index_left += 1
        else:
            sorted_list.append(sorted_right[current_index_right])
            current_index_right += 1

    return sorted_list

print(merge_sort([1, 3, 4, 5, 6, 12, 3, 4, 4, 5]))

