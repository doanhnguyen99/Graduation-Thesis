import numpy as np
import random
from numpy import argmax
import codecs
# from data_trans import read_conll_format
def read_conll_format(input_file):
    with codecs.open(input_file, 'r', 'utf8') as f:
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
        max_length_of_a_word = 0
        for line in f:
            line = line.split()
            if len(line) > 0:
                words.append(line[0].lower())
                poss.append(line[1])
                chunks.append(line[2])
                tags.append(line[3])
                max_length_of_a_word = max(max_length_of_a_word, len(line[0]))
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
    return word_list, pos_list, chunk_list, tag_list, num_sent, max_length, max_length_of_a_word
# read file
def read_char_vocab(file_path):
  char_vocab = []
  for line in open(file_path, encoding='utf8'):
    char_vocab.append(line.splitlines()[0].lower())
  return char_vocab
# run read char vocab==========begin=======================================
char_vocab_data = read_char_vocab("./VISCII_short.txt")
# char_vocab_data = read_char_vocab("char_vocab_VISCII.txt")
# print(char_vocab_data)
LEN_OF_VOCAB = len(char_vocab_data) # len of onehot vector
print('length of vocab : '+str(LEN_OF_VOCAB))
# define a mapping of chars to integers
# char_to_int = dict((char_vocab_data[i], i) for i in range(LEN_OF_VOCAB))
# int_to_char = dict((i, char_vocab_data[i]) for i in range(LEN_OF_VOCAB))
def char_to_int(char_vocab_data):
  dic = {}
  index = -1
  for char in char_vocab_data:
    try:
      dic[char]
    except:
      index = index + 1
      dic[char]=index 
  return dic
def int_to_char(char_vocab_data):
  dic = {}
  index = -1
  for char in char_vocab_data:
    try:
      dic[char]
    except:
      index = index + 1
      dic[index]=char
  return dic
char_to_int = char_to_int(char_vocab_data)
int_to_char = int_to_char(char_vocab_data)

# for key in int_to_char:
#   print(str(key)+" : "+str(int_to_char[key]))

# define input string
word_list, pos_list, chunk_list, tag_list, num_sent, max_length, max_length_of_a_word = read_conll_format('../data/add_character.txt')
print("max_length_of_a_sentence : {max_length}".format(max_length=max_length))
print("max_length_of_a_word     : {max_length_of_a_word}".format(max_length_of_a_word=max_length_of_a_word))
max_length_of_a_sentence = 25
max_length_of_a_word     = 25


#=================start====================================================
def char_encode_word_list(word_list,max_length_of_a_sentence,max_length_of_a_word):
  # len(word_list)
  word_list_encoded = np.zeros([len(word_list), max_length_of_a_sentence, max_length_of_a_word])
  for i in range(len(word_list)):
    
    sentence = word_list[i] # words is a sentence | ['i','am','an']
    sentence_encoded = np.zeros([max_length_of_a_sentence,max_length_of_a_word]) # 25*25
    for j in range(len(sentence)):  
      # word to encoded, like [12,3,4,20,0,0,0,0,0]
      word = sentence[j].lower()
      # integer_encoded = [char_to_int[char] for char in word]
      word_encoded = np.zeros(max_length_of_a_word)
      for k in range(len(word)):
        char = word[k]
        try:
          word_encoded[k]= char_to_int[char]
        except:
          print("error : " + str(char)+" "+str(word)+" "+str(len(word)))
          word_encoded[k]= char_to_int['[unk]']

      # sentence encoded
      sentence_encoded[j] = word_encoded

    word_list_encoded[i] = sentence_encoded

  print(word_list_encoded.shape)

  X = word_list_encoded
  X = X.reshape(X.shape[0]*X.shape[1],X.shape[2])
  X = X.astype(np.int64)
  fileout = open('char_encode.txt', 'a+', encoding='utf8')
  np.savetxt(fileout, X)
  fileout.close()

  return word_list_encoded

char_encode = char_encode_word_list(word_list, 25, 25)
