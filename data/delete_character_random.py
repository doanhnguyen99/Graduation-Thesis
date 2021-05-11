import numpy as np
import csv
import re
import string
from collections import Counter
import numpy as np
import random

def split(word):
  return [(word[:i], word[i:]) for i in range(len(word) + 1)]

def delete(word):
  return [l + r[1:] for l,r in split(word) if r]

def pick_word_from_fake(list_word):
    index_chose = random.randint(0, len(list_word) - 1)
    return list_word[index_chose]

def check_number_contain(s):
    check = False if next((chr for chr in s if chr.isdigit()), None) else True
    return check

input_train = []
with open('./data_train_cau_giay.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        input_train.append(row[0].lower())

get_data = []
for i in input_train:
    get_data.append(i)

# tách dạng split
split_data = []
for i in input_train:
    split_data.append(i.split())


data_text = []
for i in split_data:
    temp = []
    for j in i:
        if check_number_contain(j):
            temp.append(j)
    data_text.append(temp)

concat_text_array = []
for i in data_text:
    concat_data = ""
    for j in i:
        concat_data = concat_data + j + " "
    concat_text_array.append(concat_data)

sentense_corpus = []
for i in concat_text_array:
    sentense_corpus.append(i.split())

# print(sentense_corpus)

sentence_source = []
sentence_destination = []

# tạo câu sai và đúng để train
for i in sentense_corpus:
    source = i.copy()
    sentence_source.append(source)
    index_chose = random.randint(0, len(i) - 1)
    while len(i[index_chose]) < 3:
        index_chose = random.randint(0, len(i) - 1)
    word_pick = i[index_chose]
    i[index_chose] = pick_word_from_fake(delete(word_pick))
    sentence_destination.append(i)


# đọc dữ liệu ra dạng câu để cho vào tập test
# data_test = []
# for i in sentence_destination:
#     temp = ""
#     for j in range(len(i)):
#         temp += i[j] + " "
#     data_test.append(temp)

# print(data_test)

# Read file
# Lấy data để test
# train_dataset = open("test_mistype.txt","a",encoding='utf8')
# for i in data_test:
#     train_dataset.write(str(i))
#     train_dataset.write('\n')
# train_dataset.close()

# lấy data để train
train_dataset = open("delete_random_character.txt","a",encoding='utf8')
for i in range(len(sentence_destination)):
    for j in range(len(sentence_destination[i])):
        train_dataset.write(str(sentence_destination[i][j]))
        train_dataset.write(' ')
        train_dataset.write('0')
        train_dataset.write(' ')
        train_dataset.write('0')
        train_dataset.write(' ')
        train_dataset.write(str(sentence_source[i][j]))
        train_dataset.write('\n')
    train_dataset.write('\n')
train_dataset.close()