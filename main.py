import os





def main():
    path_file = get_path_folder()
    print("started")
    print(path_file)


def get_path_folder():
    return os.path.dirname(os.path.realpath(__file__))


if __name__ == "__main__":
    main()