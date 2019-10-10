import re


def clean_data_wpp(name_file):
    data_file = open(name_file, 'r')
    file_clean = open('clean_file.txt', 'w')
    regex_info_message = r"\[.*?\].{3,4}\d{2}.\d{2}.\d{4,5}.\d{4}.:*"
    file_read = data_file.read()

    lines = file_read.splitlines()

    for line in lines:
        line = line.strip()
        if line:
            result = re.sub(regex_info_message, "", line)
            file_clean.write(result + '\n')

    file_clean.close()
    data_file.close()
