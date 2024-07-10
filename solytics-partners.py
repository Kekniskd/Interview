a = [1, 3, 7, 5, 9, 3, 5]


def find_sencond_larget(array: list) -> int:
    largest = float('-inf')
    second_largest = float('-inf')
    for num in array:
        if num > second_largest:
            second_largest = num
        if num > largest:
            second_largest = largest
            largest = num
    return second_largest


def contains_duplicates(array: list) -> bool:
    dub = {}
    for num in array:
        if num in dub:
            return False
        else:
            dub[num] = True
    return True
