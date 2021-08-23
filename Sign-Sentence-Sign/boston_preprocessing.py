import argparse
import csv
import pandas as pd
import numpy as np

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-csvfile", "--csvdata", required=True,
   help="train data")

ap.add_argument("-sentence_input","--sentence",required=True,
    help="input gloss sentence")



args = vars(ap.parse_args())

train = pd.read_csv(args['csvdata'], error_bad_lines=False)
inp = args['sentence']

train_gloss_sentences = train['orth'].tolist()
ved = train['frames'].tolist()
train_gloss_words = np.array([sentences.split(' ') for sentences in train_gloss_sentences])
all_words = np.unique(np.ravel(np.array(train_gloss_words)))

#inp = args['sentence'].split(' ')
inp = 'JOHN GIVE GIRL BOX'
inp = inp.split(' ')
for word in inp:
    if word not in all_words is True:
        print("there is an unexected word that is is not in training dataset")
        sys.exit()

def get_sentences_from_train(words):
  data = []
  for i in words:
    count = 0
    sentences = []
    position_of_sentence = []
    for k,j in enumerate(train_gloss_words):
        if i in j:
          count = count + 1
          #print(count)
          position_of_sentence.append(ved[k])
          sentences.append(train_gloss_sentences[k])
    data.append([i,sentences,position_of_sentence,count])
  return data
total_data_words =get_sentences_from_train(inp)
for i in range(len(inp)):
  print('_____________________________________________________________________________________')
  print('\n')
  print('required word'.ljust(40, '-'),total_data_words[i][0])
  print('found in sentence'.ljust(40, '-'),total_data_words[i][1][0])
  print('position in train dataset'.ljust(40, '-'),total_data_words[i][2][0])


def write(row):
  with open('sentenseandword.csv', 'a') as csvFile:
      writer = csv.writer(csvFile)
      writer.writerow(row)
  csvFile.close()


row  = ['word','sentence','path for sentence']
write(row)

for i in range(len(total_data_words)):
    row = [total_data_words[i][0],total_data_words[i][1][0],total_data_words[i][2][0]]
    write(row)



