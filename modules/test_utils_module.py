from modules import utils

def test_get_file_names(folderpath):
    utils.get_file_names(folderpath)

def test_get_all_file_names(folderpath):
    utils.get_all_file_names(folderpath)

def test_print_line_one(file_names):
    utils.print_line_one(file_names)

def test_print_emails(file_names):
    utils.print_emails(file_names)

def test_write_headlines(md_files):
    utils.write_headlines(md_files)
