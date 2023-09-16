import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import argparse
import pandas as pd
import numpy as np
import tensorflow as tf
from model import ip2vec
from preprocess import Preprocess

def train_ip2vec(input_file, word2id_file, data, dir):
    # Read bulk_word2id.csv
    df = pd.read_csv(word2id_file)
    word2id = dict(df.values.tolist())

    # Read bulk_concat.csv
    df = input_file[['ip_src', 'ip_dst', 'data_len', 'dst_port', 'proto']]
    X_train, y_train = Preprocess(df.values.tolist(), word2id, 1).generate_training_data()
    parameters = ip2vec().skipgram_model_training(X_train, y_train, len(word2id), 1, 0.05, 100)

    wrd_emb = pd.DataFrame(parameters['WRD_EMB'])
    wrd_emb['word'] = word2id.keys()
    wrd_emb.to_csv(dir + data + '_emb.csv', index=False)
    pd.DataFrame(parameters.items()).to_csv(dir + data + '_parameters.csv', index=False)

def word_to_id(input_file):

    concat = pd.read_csv(input_file)
    concat.drop_duplicates(['time', 'ip_dst'], inplace=True)
    temp = concat.groupby(['time', 'ip_src', 'ip_dst', 'dst_port', 'proto'], as_index=False).count()[['time', 'ip_src', 'ip_dst', 'dst_port', 'proto', 'data_len']]

    final_df = pd.merge(concat[['time', 'ip_src', 'ip_dst', 'dst_port', 'proto']], temp)
    
    drop = final_df.drop_duplicates()

    drop = drop[['ip_src', 'ip_dst', 'data_len', 'dst_port', 'proto']].reset_index(drop=True)

    return drop

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process CSV file for Ip2Vec analysis")
    parser.add_argument("--data", type=str, help="Path to the bulk_concat.csv file")
    parser.add_argument("--dir", type=str, help="Path to the output CSV file (parameters.csv)")
    args = parser.parse_args()
    
    input = args.dir + args.data + '_concat.csv'
    word2id = args.dir + args.data + '_word2id.csv'
    
    word2id_drop = word_to_id(input)
    train_ip2vec(word2id_drop, word2id, args.data, args.dir)
    