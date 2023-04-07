def print_mid_point(items):

    midpoint = len(items) // 2
    index = 0
    for item in items:
        while index < midpoint:
            print(item)
            index += 1

    for time in range(100):
        print(time)

#driver
print_mid_point(["Thissjkahxihuio"])

