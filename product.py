def products(nums):
    # Generate prefix products
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)

    # Generate suffix products
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return print(result)

products([1, 2, 3, 4, 5])

# def product(nums):
#
#     prod = [None] * 128
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             prod = nums[i] * nums[j]
#     return print(prod)
#
#
# product([1, 2, 3, 4, 5])

# def product(nums):
#     # prefix products
#     prefix_product = []
#
#     for num in nums:
#         if prefix_product:
#             prefix_product.append(prefix_product[-1] * num)
#         else:
#             prefix_product.append(num)
#
#     # Generate sufix product
#     suffix_product = []
#     for num in reversed(nums):
#         if suffix_product:
#             suffix_product.append(suffix_product[-1] * num)
#     suffix_product = list(reversed(suffix_product))
#     # generate result
#
#     result = []
#     for i in range(len(nums)):
#         if i == 0:
#             result.append(suffix_product[i + 1])
#         elif i == len(nums) - 1:
#             result.append(prefix_product[i - 1])
#         else:
#             result.append(prefix_product[i - 1] * suffix_product[i + 1])
#     return result
#
#
# product([1, 2, 3, 4, 5])



