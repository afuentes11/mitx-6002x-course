import os
import argparse

def init_parser():
    parser = argparse.ArgumentParser(description='Creates the general folder structure for each reading.')
    parser.add_argument('--lecture', '-l', dest='lecture', type=str, help='reading number')
    parser.add_argument('--exercises', '-e', dest='exercises', type=str, default="1", help='number of exercises')
    parser.add_argument('--no-utils', dest='is_create_util_folder', action='store_false', help='Do not include utils folder')
    args = parser.parse_args()
    return args


def add_basic_files_to_folder(path, files=["__init__.py", "main.py", "README.md"]):
    for f in files:
        create_file(path, f)


def create_file(path, file):
    with open(f"{path}/{file}", "w") as f:
        if file == "main.py":
            f.write("")
            f.write("def main():\n")
            f.write("    pass\n\n")
            f.write("")
            f.write("")
            f.write("if __name__ == \"__main__\":\n")
            f.write("    main()\n")
        else:
            f.write("")


def main():
    
    args = init_parser()

    lecture = args.lecture
    exercises = args.exercises
    is_create_util_folder = args.is_create_util_folder

    if os.path.exists(f"lecture{lecture}"):
        print("Folder already exists")

    else:
        os.mkdir(f"lecture{lecture}")
        create_file(f"lecture{lecture}", "README.md")
        
        for i in range(1, int(exercises)+1):
            os.mkdir(f"lecture{lecture}/exercise{i}")
            add_basic_files_to_folder(f"lecture{lecture}/exercise{i}")

        if is_create_util_folder:
            os.mkdir(f"lecture{lecture}/utils")
            add_basic_files_to_folder(f"lecture{lecture}/utils", ["__init__.py", "utils.py"])
        
        print("Folder created")

if __name__ == "__main__":
    main()