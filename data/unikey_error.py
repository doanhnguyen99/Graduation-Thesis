import numpy as np
import csv
import re
import string
from collections import Counter
import numpy as np
import random

input_train = []
with open('./data_train_cau_giay.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        input_train.append(row[0].lower())

def check_number_contain(s):
    check = False if next((chr for chr in s if chr.isdigit()), None) else True
    return check

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

sentense_corpus = []
for i in data_text:
    concat_data = ""
    for j in i:
        concat_data = concat_data + j + " "
    sentense_corpus.append(concat_data)
# print(sentense_corpus)

source_digit = ['ạ', 'ả', 'ã', 'à', 'á', 'â', 'ậ', 'ẩ', 'ẫ', 'ầ', 'ấ', 'ă', 'ặ', 'ẳ', 'ẵ', 'ằ', 'ắ',
                'ọ', 'ỏ', 'õ', 'ò', 'ó', 'ô', 'ộ', 'ổ', 'ỗ', 'ồ', 'ố', 'ơ', 'ợ', 'ở', 'ỡ', 'ờ', 'ớ',
                'ẹ', 'ẻ', 'ẽ', 'è', 'é', 'ê', 'ệ', 'ể', 'ễ', 'ề', 'ế',
                'ụ', 'ủ', 'ũ', 'ù', 'ú', 'ư', 'ự', 'ử', 'ữ', 'ừ', 'ứ',
                'ị', 'ỉ', 'ĩ', 'ì', 'í',
                'ỵ', 'ỷ', 'ỹ', 'ỳ', 'ý',
                'đ']

replace_digit = ['aj', 'ar', 'ax', 'af', 'as', 'aa', 'aaj', 'aar', 'aax', 'aaf', 'aas', 'aw', 'awj', 'awr', 'awx', 'awf', 'aws',
                'oj', 'or', 'ox', 'of', 'os', 'oo', 'ooj', 'oor', 'oox', 'oof', 'oos', 'ow', 'owj', 'owr', 'owx', 'owf', 'ows',
                'ej', 'er', 'ex', 'ef', 'es', 'ee', 'eej', 'eer', 'eex', 'eef', 'ees',
                'uj', 'ur', 'ux', 'uf', 'us', 'uw', 'uwj', 'uwr', 'uwx', 'uwf', 'uws',
                'ij', 'ir', 'ix', 'if', 'is',
                'yj', 'yr', 'yx', 'yf', 'ys',
                'dd']

def check_special_character(digit):
    check = True
    if ord(digit) > 96 and ord(digit) < 122:
        check = False
    elif digit == '-' or digit == ',' or  digit == ',' or  digit == '&' or digit == ' ' or digit == '/':
        check = False
    elif ord(digit) > 47 and ord(digit) < 58:
        check = False
    return check

def replace_digit_to_unikey(digit):
    for i in range(len(source_digit)):
        if digit == source_digit[i]:
            digit = replace_digit[i]
            pass
    return digit

# for i in text_test:
#     if check_special_character(i):
#         print(replace_git_to_unikey(i))

def fake_sentense(text_test):
    data_source = text_test
    count = 0
    for i in range(len(text_test)):
        if check_special_character(text_test[i]) == True:
            text_test = text_test.replace(text_test[i], replace_digit_to_unikey(text_test[i]))
            # print(text_test)
            count = count + 1
        elif count == 2:
            break
    return text_test

# text_test = '144 xuân thủy Cầu Giấy Hà Nội'
# print(fake_sentense(text_test))

total = []
for i in sentense_corpus:
    data_source = i
    sentense_set = []
    sentense_set.append(data_source)
    sentense_set.append(fake_sentense(i))
    total.append(sentense_set)

# print(total)

total_data = []
for i in total:
    data = []
    for j in i:
        data.append(j.split())
    total_data.append(data)
 
# print(total_data)

# output file
#tạo tập test
# data_test = []
# for i in total_data:
#     temp = ""
#     for j, value in enumerate(i[0]):
#         temp += i[1][j] + " "
#     data_test.append(temp)

# dùng data để test
# train_dataset = open("unikey_error_test.txt","a",encoding='utf8')
# for i in data_test:
#     train_dataset.write(str(i))
#     train_dataset.write('\n')
# train_dataset.close()

# data_test = []
# for i in sentence_destination:
#     temp = ""
#     for j in range(len(i)):
#         temp += i[j] + " "
#     data_test.append(temp)



train_dataset = open("unikey_error.txt", "a", encoding='utf8')
for i in total_data:
    for j, val in enumerate(i[0]):
        train_dataset.write(str(i[1][j]))
        train_dataset.write(' ')
        train_dataset.write('0')
        train_dataset.write(' ')
        train_dataset.write('0')
        train_dataset.write(' ')
        train_dataset.write(str(val))
        train_dataset.write('\n')
    train_dataset.write('\n')
train_dataset.close()