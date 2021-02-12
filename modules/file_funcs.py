import argparse

def print_file_content(file):
    with open(file) as f_obj:
        content = f_obj.readlines()
        print(content)

# Before rewrite
def write_list_to_file(output_file, lst):
    with open(output_file, "w") as f_obj:
        for element in lst:
            f_obj.write(str(element))
            f_obj.write( "\n")

#Rewritten
def write_list_to_file_two(output_file, *strings):
    with open(output_file, "w") as f_obj:
        for string in strings:
            f_obj.write(string + "\n")


def read_csv(input_file):
    list = []
    with open(input_file) as f_obj:
        content = f_obj.readlines()

        for line in content:
            list.append(line)


    return list

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A program that can read CSV files (to console and to a list) and write strings or a list to a text file.")
    parser.add_argument("csv_path", help="Path to the CSV file you want the program to read.")
    parser.add_argument("-f", "--file", help="Name of file you want to write to.")

    args = parser.parse_args()
    print("CSV Path: ", args.csv_path)
    print("File: ", args.file)

    if not (args.file):
        print_file_content(args.csv_path)
    else:
        list = read_csv(args.csv_path)
        write_list_to_file(args.file, list)

    