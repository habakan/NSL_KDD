import pandas as pd


def load_column():
    with open("../Field Names.csv", 'r') as f:
        columns = [text.replace('\n', '').replace(',continuous', '').replace(',symbolic', '') for text in f.readlines()]

    return columns

def load_train():
    columns = load_column()
    columns += ["xattack", "num_acc"]

    filename = "../KDDTrain+.csv"
    df = pd.read_csv(filename, header=None)
    df.columns = columns

    return df

def load_test():
    columns = load_column()
    columns += ["xattack", "num_acc"]

    filename = "../KDDTest+.csv"
    df = pd.read_csv(filename, header=None)
    df.columns = columns

    return df

def onehotencode(df):
    categorical_var = [
            "protocol_type",
            "service",
            "flag"
    ]

    return pd.get_dummies(df, columns = categorical_var)
