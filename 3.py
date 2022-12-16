import os
from typing import List

FILE_LOG_DIR = 'text files'
ROOT_PATH = os.getcwd()
path = os.path.join(ROOT_PATH, FILE_LOG_DIR)
files_l = []  # список названи файлов
for file in os.listdir(path):
    files_l.append(file)
files_d = {}  # словарь из названия,содержания и кол-ва строк в файлах
info = []  # содержание файлов
for file in files_l:
    with open(os.path.join(path, file), 'r', encoding='utf-8') as f:
        count_lines = 0
        for i in f:
            count_lines += 1
            info.append(i)
            files_d[file] = [count_lines, info]
print(files_d)

# values_dict = {}
#
# for k, v in files_d.items():
#     print(k,v)
#
# print(values_dict)
#with open('result.txt', 'a') as res_file:
    #for key, value in files_d.items():
        #print(key, value[0], ''.join(value[1]), sep='\n')