import itertools


def cup_of_join(*lists, separator='-'):
    list_of_lists = []

    if not lists:
        return list_of_lists

    [one_list.append(separator) for one_list in lists]
    list_of_lists = list(itertools.chain(*lists))
    list_of_lists.pop()

    return list_of_lists


if __name__ == "__main__":
    print(cup_of_join([1, 2], [2, 3], [3, 4], separator='*'))
