import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from time import timedelta

def main():
    pass

def processData():
    url = "Train.csv";
    train = pd.read_csv(url);
    url = "Test.csv";
    test = pd.read_csv(url);
    print(train.shape, test.shape);
    print(train.sample(5), test.sample(5)); 
    #combining the dataset with a source column to record where each observation belong
    train['source'] = 'train';
    test['source'] = 'test';

    data = pd.concat([train, test],ignore_index=True, sort=False);
    print (train.shape, test.shape, data.shape);



if __name__ == "__main__":
    start_time = time.time()
    main()
    d = timedelta(seconds=(time.time()-start_time))
    print("\n*** total run time (): " , d,"***\n")

