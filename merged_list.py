def merged_list(arr1,arr2):
    len_of_mergedlist = len(arr1) +len(arr2)

    merged_list = [None] * len_of_mergedlist

    head_of_my_list = arr1[0]
    head_of_alice_list = arr1[0]

    if head_of_my_list < head_of_alice_list:
        merged_list[0] = arr1
    else:
        merged_list[0] = arr2

    return merged_list

merged_list([1,3,5,6,8],[2,4,7,9])