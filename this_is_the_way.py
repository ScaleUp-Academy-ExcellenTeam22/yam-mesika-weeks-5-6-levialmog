import os


def this_is_the_way():
    res_lst = []
    path = input("Enter path to directory: ")

    for files in os.listdir(path):
        if files.startswith('deep'):
            res_lst.append(files)

    return res_lst


this_is_the_way()

