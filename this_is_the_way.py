import os


def this_is_the_way(directory_path):
    files_that_start_with_deep = []

    for files in os.listdir(directory_path):
        if files.startswith("deep"):
            files_that_start_with_deep.append(files)

    return files_that_start_with_deep


if __name__ == "__main__":
    this_is_the_way("C:\\yam_mesika_ex\\Notebooks-master\\Notebooks-master\\week05\\images")
