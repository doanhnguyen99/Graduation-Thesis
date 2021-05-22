import csv
import re
import string
from collections import Counter
import numpy as np
import random

def random_add_character(word):
    rand_ascii = np.random.randint(97, 123)
    rand_char = chr(rand_ascii)
    index = np.random.randint(0, len(word))
    new_word = word[:index] + rand_char + word[index:]
    return new_word

def generate_error(sentence):
    for i in range(2):
        pick_index = random.randint(0, len(sentence) - 1)
        # print(sentence[pick_index])
        while sentence[pick_index].isdigit():
            pick_index = random.randint(0, len(sentence) - 1)
        sentence[pick_index] = random_add_character(sentence[pick_index])
    return sentence

input_train = []
with open('./data_train_cau_giay.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        input_train.append(row[0].lower())


# tách dạng split
get_text_data = []
for i in input_train:
    get_text_data.append(i.split())

def check_number_contain(s):
    check = False if next((chr for chr in s if chr.isdigit()), None) else True
    return check

# xxx = ['103', 'phố', 'phùng', 'chí', 'kiên', 'nghĩa', 'đô', 'cầu', 'giấy', 'hà', 'nội']
# for i in xxx:
#     if check_number_contain(i):
#         print(i)

data_text = []
for i in get_text_data:
    temp = []
    for j in i:
        if check_number_contain(j):
            temp.append(j)
    data_text.append(temp)

# print(data_text)

# tạo tập train
sentence_source = []
sentence_destination = []
for i in data_text:
    sentence_source.append(i.copy())

source = []
for i in sentence_source:
    source.append(i.copy())
    sentence_destination.append(generate_error(i))

# for i in range(len(sentence_destination)):
#     print(source[i])
#     print(sentence_destination[i])
#     break

# train_dataset.close()

# Lấy data để test
# data_test = []
# for i in sentence_destination:
#     temp = ""
#     for j in range(len(i)):
#         temp += i[j] + " "
#     data_test.append(temp)

# train_dataset = open("new_train.txt","a",encoding='utf8')
# for i in data_test:
#     train_dataset.write(str(i))
#     train_dataset.write('\n')

# train_dataset.close()

# for i in data_test:
#     print(i)

# Lấy data để train
train_dataset = open("add_random_character.txt","a",encoding='utf8')
for i in range(len(sentence_destination)):
    for j in range(len(sentence_destination[i])):
        train_dataset.write(str(sentence_destination[i][j]))
        train_dataset.write(' ')
        train_dataset.write('0')
        train_dataset.write(' ')
        train_dataset.write('0')
        train_dataset.write(' ')
        train_dataset.write(str(source[i][j]))
        train_dataset.write('\n')
    train_dataset.write('\n')
train_dataset.close()