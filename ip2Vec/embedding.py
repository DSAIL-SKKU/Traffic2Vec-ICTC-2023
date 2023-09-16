import pandas as pd
import numpy as np
import argparse

def process_data(data, dir):
    # Read the main data file
    df = pd.read_csv(dir + data + '_10wnd_40data_new.csv')
    
    # Select relevant columns
    df = df[['traffic(t-10)', 'traffic(t-9)', 'traffic(t-8)', 'traffic(t-7)', 'traffic(t-6)',
             'traffic(t-5)', 'traffic(t-4)', 'traffic(t-3)', 'traffic(t-2)', 'traffic(t-1)', 'traffic(t)']]
    
    # Read the word embedding data
    wrd_emb = pd.read_csv(dir + data + '_emb.csv')
    
    # Filter and extract word embeddings related to 'data_len'
    index = 0
    words_ = wrd_emb['word'].values.tolist()
    for i in range(len(words_)):
        word = words_[i].split(' ')[0]
        if word == 'data_len':
            index = i
            break
    words = wrd_emb['word'].values.tolist()[index:]
    del wrd_emb['word']
    
    dl_dict = {}
    for i, word in enumerate(words):
        dl_dict[float(word.split(' ')[1])] = wrd_emb.loc[index + i].values.tolist()

    result = []
    data_list = df.values.tolist()
    
    for s in data_list:
        temp = []
        for d in s:
            temp.append(dl_dict[d])
        result.append(temp)
        
    print(np.array(result).shape)
    # Save the processed data as a numpy array
    np.save(dir + data + '_10wnd_40data_new_emb_.csv', np.array(result))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process data using word embeddings')
    parser.add_argument('--data', type=str, help='Specify the bulk argument')
    parser.add_argument('--dir', type=str, help='Specify the bulk argument')
    args = parser.parse_args()

    process_data(args.data, args.dir)
