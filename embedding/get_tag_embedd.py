import numpy as np
import requests
import codecs
import _pickle as pickle
import time

def read_conll_format(input_file):
    with codecs.open(input_file, 'r', encoding='utf8') as f:
        word_list = [] 
        chunk_list = []
        pos_list = []
        tag_list = []
        words = []
        chunks = []
        poss = []
        tags = []
        num_sent = 0
        max_length = 0
        for line in f:
            line = line.split()
            if len(line) > 0:
                words.append(map_number_and_punct(line[0].lower()))
                poss.append(line[1])
                chunks.append(line[2])
                tags.append(line[3])
            else:
                word_list.append(words)
                pos_list.append(poss)
                chunk_list.append(chunks)
                tag_list.append(tags)
                sent_length = len(words)
                words = []
                chunks = []
                poss = []
                tags = []
                num_sent += 1
                max_length = max(max_length, sent_length)
    return word_list, pos_list, chunk_list, tag_list, num_sent, max_length

def map_number_and_punct(word):
    if any(char.isdigit() for char in word):
        word = u'<number>'
    elif word in [u',', u'<', u'.', u'>', u'/', u'?', u'..', u'...', u'....', u':', u';', u'"', u"'", u'[', u'{', u']',
                  u'}', u'|', u'\\', u'`', u'~', u'!', u'@', u'#', u'$', u'%', u'^', u'&', u'*', u'(', u')', u'-', u'+',
                  u'=']:
        word = u'<punct>'
    return word
#============================get tag_list=====================================
word_list, pos_list, chunk_list, tag_list, num_sent, max_length = read_conll_format('../get char embedd/data_train/version_1.txt')
#============================create dic of tag================================
def dict_of_tags(tag_list):
    dic = {'pad': 0}
    index = 0
    for tags in tag_list:
        for tag in tags:
            try:
                dic[tag]
            except:
                index = index + 1
                dic[tag]= index
    return dic, len(dic)

# print(tag_list)
dic_of_tag, len_of_dic_tag = dict_of_tags(tag_list)
print(dic_of_tag)
print(len_of_dic_tag)
#===========================encode tag_list by dic_of_tags================
def encode_tag_list_by_dic_of_tags(tag_list, dic, len_of_a_sentence):
    encodeTag_of_many_sentence = []
    for tags_of_a_sentence in tag_list:
        # print(tags_of_a_sentence)
        encode_of_a_sentence = np.zeros(len_of_a_sentence)
        for i in range(len(tags_of_a_sentence)):
            tag = tags_of_a_sentence[i]
            encode_of_a_sentence[i] = dic[tag]
        encodeTag_of_many_sentence.append(encode_of_a_sentence)
    return np.array(encodeTag_of_many_sentence)

tag_list_encode = encode_tag_list_by_dic_of_tags(tag_list,dic_of_tag, 25)
print(tag_list_encode.shape)
# print(tag_list_encode[0])
#==========================create one hot vector from tag_encode==========
def create_onehot(sens_encodes, tag_dim, num_word_in_sentence):
    X = np.zeros([len(sens_encodes), num_word_in_sentence, tag_dim])
    for i in range(len(sens_encodes)):# duyet tung cau
        for j in range(len(sens_encodes[i])):# duyet tung tu trong cau
            index = sens_encodes[i][j].astype(np.int64)
            X[i, j, index] = 1

    X = X.reshape(X.shape[0]*X.shape[1], X.shape[2])
    fileout = open('tag_embedd.txt', 'a+', encoding='utf8')
    np.savetxt(fileout, X)
    fileout.close()
    return X

tag_onehot = create_onehot(tag_list_encode, tag_dim = len_of_dic_tag, num_word_in_sentence = 25)
print(tag_onehot.shape)
# print(tag_onehot[0])