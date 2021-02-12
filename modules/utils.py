import os
import argparse

def get_file_names(folderpath, out="/home/jovyan/python_handins_bs190/testfiles/output.txt"):
    files = os.listdir(folderpath)
    with open(out, "w") as f_obj:
        f_obj.write(str(files))


def get_all_file_names(folderpath, out="/home/jovyan/python_handins_bs190/testfiles/output.txt"):
    with open(out, "w") as f_obj:
        for root, dirs, files in os.walk(folderpath):
            f_obj.write(str(files))


def print_line_one(file_names):
    for file in file_names:
        for root, dirs, files in os.walk("."):
            if file in files:
                with open(file, "r") as f_obj:
                    print(f_obj.readline())
                


def print_emails(file_names):
    for file in file_names:
        for root, dirs, files in os.walk("."):
            if file in files:
                with open(file, "r") as f_obj:
                    data = f_obj.readlines()
                for line in data:
                    if line.__contains__("@"):
                        print(line)


def write_headlines(md_files, out="/home/jovyan/python_handins_bs190/testfiles/output.txt"):
        for file in md_files:
            for root, dirs, files in os.walk("."):
                if file in files:
                    with open(file, "r") as f_obj:
                        data = f_obj.readlines()
                    for line in data:
                        if line.startswith("#"):
                             with open(out, "w") as f_obj_2:
                                f_obj_2.write(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A program that can write file names and folder names to text files, and print specific parts of files such as lines containing emails.")
    parser.add_argument("-gp", "--getpath", help="Path to folder you want to get the names of files from.")
    parser.add_argument("-gap", "--getallpath", help="Path to the folder you want to get the names of all files and subdirectories from.")
    parser.add_argument("-pl", "--printline", help="Names of the files you want to print the first lines of.")
    parser.add_argument("-pe", "--printemail", help="Names of the files you want to print any lines containing emails from.")
    parser.add_argument("-wh", "--writeheadlines", help="Names of the markdown files you want to print any headlines from.")

    args = parser.parse_args()

    if args.getpath:
        get_file_names(args.getpath)
    elif args.getallpath:
        get_all_file_names(args.getallpath)
    elif args.printline:
        print_line_one(args.printline)
    elif args.printemail:
        print_emails(args.printemail)
    elif args.writeheadlines:
        write_headlines(args.writeheadlines)