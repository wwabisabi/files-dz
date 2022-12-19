import os
from pprint import pprint
from typing import List

FILE_LOG_DIR = 'text files'
ROOT_PATH = os.getcwd()
path = os.path.join(ROOT_PATH, FILE_LOG_DIR)
files_l = []  # список названий файлов
for file in os.listdir(path):
    files_l.append(file)
files_d = {}  # словарь из названия,содержания и кол-ва строк в файлах
for file in files_l:
    info = []  # содержание файлов
    with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
        for i in f:
            count_lines = len(info)+1
            info.append(i)
        files_d[file] = count_lines, info

sorted_list = sorted(files_d.values())
info1 = []
for i in sorted_list:
    for j in sorted_list:
        info1.append(j[1])
    break
#
txt1 = "".join(info1[0])
txt2 = "".join(info1[1]) + '\n'
txt3 = "".join(info1[2])
#print(txt1, txt2, txt3, sep='\n')

with open('result.txt', 'a', encoding='utf-8') as new_f:
    for i in txt1:
        new_f.write(f'{i}')
    for i in txt2:
        new_f.write(f'{i}')
    for i in txt3:
        new_f.write(f'{i}')

