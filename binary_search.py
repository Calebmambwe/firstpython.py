def binary_search(target, lst):
    floor_index = -1
    ceiling_index = len(lst)

    while floor_index + 1 < ceiling_index:
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

        guess_value = lst[guess_index]
        if guess_value == target:
            return True

        if guess_value > target:
            ceiling_index = guess_index
        else:
            floor_index = guess_index

    return False

#driver
binary_search(12, [1,3,4,5,6,12,3,4,4,5])