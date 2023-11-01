word_list = ["apple", "banana", "cherry", "dates", "elderberry", "green", "greenRedOrangeYellowBlue"]


def return_second(list: list) -> str:

    scLarget = 0
    largest = len(word_list[0])
    for item in list:
        if len(item) > scLarget:
            if len(item) < largest:
                scLarget = len(item)
            elif len(item) > largest:
                largest = len(item)
    return scLarget



print(return_second(word_list))


