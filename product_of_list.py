def product_of_list(list_ints):
    product_of_list = [None] * len(list_ints)

    for i in range(len(list_ints)):
        product_of_list = list_ints[i] * list_ints[i + 1]
        # product_of_list.append(product)

    return print(product_of_list)

product_of_list([1,2,3,4])