def linear_search(lst, target):
    ''' Returns the position of the index of the target if found, else returns None'''
    for i in range(len(lst)):
        if lst[i] == target:
            return i
        return None


def verify(index):
    if index is not None:
        print(index)
    else:
        print("Your Target index was not found ")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 6)
verify(result)

