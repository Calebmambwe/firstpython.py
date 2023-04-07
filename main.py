def two_sum(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == k:
                return True
    return False


if __name__ == "__main__":
    list = [2, 4, 1, 6, 8, 6]
    k = 7
    data = two_sum(list, k)
    print(data)