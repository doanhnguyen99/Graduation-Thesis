import numpy as np
import csv
import re
import string
from collections import Counter
import numpy as np
import random

def random_mistype(word):
    keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    index = np.random.randint(0, len(word))
    mistyped_char = word[index]
    incorrect_char = 'a'
    for row in keyboard:
        if mistyped_char in row:
            key_location = row.index(mistyped_char)
            if key_location == len(row)-1:
                incorrect_char = row[key_location-1]
            else:
                incorrect_char = row[key_location+1]
    new_word = word[:index] + incorrect_char + word[index+1:]    
    return new_word

def random_add_character(word): #6
    rand_ascii = np.random.randint(97, 123)
    rand_char = chr(rand_ascii)
    index = np.random.randint(0, len(word))
    new_word = word[:index] + rand_char + word[index:]
    return new_word

def delete_random_character(word): #3
    index = np.random.randint(0, len(word))
    new_word = word[:index] + word[index+1:]
    return new_word

def random_spelling_error(word):
    new_word = word
    if word.startswith('tr'):
        new_word = word.replace('tr', 'ch', 1)
    elif word.startswith('ch'):
        new_word = word.replace('ch', 'tr', 1)
    elif word.startswith('s'):
        new_word = word.replace('s', 'x', 1)
    elif word.startswith('x'):
        new_word = word.replace('x', 's', 1)
    elif word.startswith('l'):
        new_word = word.replace('l', 'n', 1)
    elif word.startswith('n') and not word.startswith('nh') and not word.startswith('ng'):
        new_word = word.replace('n', 'l', 1)
    elif word.startswith('d'):
        new_word = word.replace('d', np.random.choice(['r', 'gi']), 1)
    elif word.startswith('r'):
        new_word = word.replace('r', np.random.choice(['d', 'gi']), 1)
    elif word.startswith('gi'):
        new_word = word.replace('gi', np.random.choice(['r', 'd']), 1)
    return new_word

def check_number_contain(s):
    check = False if next((chr for chr in s if chr.isdigit()), None) else True
    return check

def generate_error(sentence):
    pick_index_1 = random.randint(0, len(sentence) - 1)
    pick_index_2 = random.randint(0, len(sentence) - 1)
        # print(sentence[pick_index])
    while sentence[pick_index_1].isdigit() and sentence[pick_index_2].isdigit() and pick_index_1 != pick_index_2:
        pick_index_1 = random.randint(0, len(sentence) - 1)
        pick_index_2 = random.randint(0, len(sentence) - 1)
    sentence[pick_index_1] = random_spelling_error(sentence[pick_index_1])
    sentence[pick_index_2] = random_add_character(sentence[pick_index_2])
    return sentence



input_train = []
with open('./data_train_cau_giay.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        input_train.append(row[0].lower())

get_data = []
for i in input_train:
    get_data.append(i)

# t??ch d???ng split
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

sentence_source = []
sentence_destination = []
for i in concat_text_array:
    sentence_source.append(i.split().copy())

source = []
for i in sentence_source:
    source.append(i.copy())
    sentence_destination.append(generate_error(i))

# for i in range(len(sentence_source)):
#     print(source[i])
#     print(sentence_destination[i])
#     break

train_dataset = open("add_and_spelling.txt","a",encoding='utf8')
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