def palandrome(the_str):
    unpair_characters = set()

    for char in the_str:
        if char in unpair_characters:
            unpair_characters.remove(char)
        else:
            unpair_characters.add(char)

    return len(unpair_characters) <= 1

