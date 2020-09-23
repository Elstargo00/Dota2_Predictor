import pandas as pd
import numpy as np
from . import app, db
from .functions import load_Num_history 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


def logistic_regression():

    Num_history_df = load_Num_history()

    train_set, test_set = train_test_split(Num_history_df, test_size=0.2, random_state=77)

    features = ['tm_r_sc', 'pos1_r_sc', 'pos2_r_sc', 'pos3_r_sc', 'pos4_r_sc', 'pos5_r_sc', 'tm_d_sc', 'pos1_d_sc', 'pos2_d_sc', 'pos3_d_sc', 'pos4_d_sc', 'pos5_d_sc']

    train_labels = train_set['a_result']
    train_features = train_set[features]

    test_labels = test_set['a_result']
    test_features = test_set[features]

    clf = LogisticRegression()
    clf.fit(train_features, train_labels)

    pickle.dump(clf, open('app/ML_model/logistic_regression_model.pkl', 'wb'))



def decode_result(binary_prob, prob):
    if binary_prob==1:
        return 'Radiant Victory', prob[0][1]
    else:
        return 'Dire Victory', 1-prob[0][1]