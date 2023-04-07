def reverse_array(array):
    i = 0
    leng = len(array)
    while i < leng:
        # print(array[i])
        print(len(array[i]))
        leng -= 1

        # for j in range(len(array)):
        #     array[i], array[j] = array[j], array[i]
        #     print(array[j])
    return array


reverse_array(['a','b','c'])