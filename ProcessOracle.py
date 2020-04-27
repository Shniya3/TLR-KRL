# coding:utf-8

import os

import ProcessSourceCode

def process_oracle():
    sourcecode_list = ProcessSourceCode.get_sourcecode_list()

    content = ""
    foRead = open(input_oracle_file, "r", encoding="UTF-8")
    for line in foRead:
        line = line.replace("\n", "")
        line = line.strip()
        link_list = line.split(" ")

        usecase = link_list[0]

        link_unique_list = []
        for item in link_list[1:]:
            if item not in link_unique_list and item in sourcecode_list:
                link_unique_list.append(item)

        for sourcecode in link_unique_list:
            content += usecase + " " + sourcecode + "\n"
        # content += "\n"

    foWrite = open(output_oracle_line_file, "w", encoding="UTF-8")
    foWrite.write(content)
    foWrite.close()


def get_oracle_list():
    oracle_list = []
    foRead = open(input_oracle_line_file, "r", encoding="UTF-8")
    for line in foRead:
        line_array = line.split(" ")
        usecase = line_array[0].strip()
        sourcecode = line_array[1].strip()
        link = [usecase, sourcecode]
        oracle_list.append(link)
    # print("oracle_list[300] =", oracle_list[300])
    return oracle_list

def get_sourcecode_u():
    oracle_list = get_oracle_list()
    sourcecode_list = ProcessSourceCode.get_sourcecode_list()
    oracle_sourcecode_list = []
    for link in oracle_list:
        usecase = link[0]
        sourcecode = link[1]
        if sourcecode not in oracle_sourcecode_list:
            oracle_sourcecode_list.append(sourcecode)
    # print("oracle_sourcecode_list =", len(oracle_sourcecode_list), oracle_sourcecode_list)
    sourcecode_u_list = []
    for sourcecode in sourcecode_list:
        if sourcecode not in oracle_sourcecode_list:
            sourcecode_u_list.append(sourcecode)
    # print("sourcecode_u_list =", len(sourcecode_u_list), sourcecode_u_list)

input_usecase_directory = "../../input/eTour/UC1/"
input_sourcecode_directory = "../../input/eTour/CC1/"

input_oracle_line_file = "../../input/eTOUR/oracle/oracle line.txt"
input_oracle_file = "../../input/eTOUR/oracle/oracle.txt"
output_oracle_line_file = "../../output/eTour/oracle/oracle line.txt"



if __name__ == '__main__':
    # process_oracle()
    # get_oracle_list()
    get_sourcecode_u()
