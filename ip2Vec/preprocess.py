import numpy as np

def one_hot_encode(idx, vocab_size):
    res = [0] * vocab_size
    res[idx] = 1
    return res

class Preprocess:
    def __init__(self, flows, word_to_id, window_size):
        self.flows = flows
        self.word_to_id = word_to_id
        self.window_size = window_size
        
    def generate_training_data(self):
        X = []
        y = []
        data_list = self.flows
        
        for data in data_list:
            for i in range(len(data)):

                if i == 0:
                    type_i = 'ip_src'
                elif i == 1: 
                    type_i = 'ip_dst'
                elif i == 2: 
                    type_i = 'data_len'
                elif i == 3: 
                    type_i = 'dst_port'
                elif i == 4: 
                    type_i = 'proto'

                center_word = self.word_to_id[type_i + ' ' + str(data[i])] 

                for j in range(i - self.window_size, i + self.window_size + 1):

                    if j == 0:
                        type_j = 'ip_src'
                    elif j == 1: 
                        type_j = 'ip_dst'
                    elif j == 2: 
                        type_j = 'data_len'
                    elif j == 3: 
                        type_j = 'dst_port'
                    elif j == 4: 
                        type_j = 'proto'


    #                 if (i==1 and j==0)|(i==2 and j==0):
    #                     continue

                    if i != j and j >= 0 and j < len(data):
                        context = self.word_to_id[type_j + ' ' + str(data[j])]
                        X.append(center_word)
                        y.append(one_hot_encode(context, len(self.word_to_id)))
                        #y.append(context)
                        
        X = np.asarray(X)
        y = np.asarray(y)
        
        X = np.expand_dims(X, axis=0) 
        #y = np.expand_dims(y, axis=0) 
        
        return X, y.T
    
    