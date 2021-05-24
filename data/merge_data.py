import csv

input_train = []
with open('./add_and_spelling.txt', encoding='utf8') as txt_file:
    txt_reader = csv.reader(txt_file)
    for row in txt_reader:
        input_train.append(row)

with open('./add_random_character.txt', encoding='utf8') as txt_file:
    txt_reader = csv.reader(txt_file)
    for row in txt_reader:
        input_train.append(row)

with open('./delete_random_character.txt', encoding='utf8') as txt_file:
    txt_reader = csv.reader(txt_file)
    for row in txt_reader:
        input_train.append(row)

with open('./mistype_and_spelling.txt', encoding='utf8') as txt_file:
    txt_reader = csv.reader(txt_file)
    for row in txt_reader:
        input_train.append(row)

with open('./random_mistype.txt', encoding='utf8') as txt_file:
    txt_reader = csv.reader(txt_file)
    for row in txt_reader:
        input_train.append(row)

with open('./random_spelling_error.txt', encoding='utf8') as txt_file:
    txt_reader = csv.reader(txt_file)
    for row in txt_reader:
        input_train.append(row)

with open('./unikey_error.txt', encoding='utf8') as txt_file:
    txt_reader = csv.reader(txt_file)
    for row in txt_reader:
        input_train.append(row)

data_train = []
for i in input_train:
    if i == []:
        data_train.append('')
    for j in i:
        data_train.append(j)
# print(data_train)

train_dataset = open("merge_data.txt","a",encoding='utf8')
for i in (data_train):
    train_dataset.write(i)
    train_dataset.write('\n')
train_dataset.close()