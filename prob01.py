import pandas as pd
import sys

def label(x):
    if x[0] < x[1]:
        return "(decreased)"
    elif x[0] > x[1]:
        return "(increased)"
    elif x[0] == x[1]:
        return "(no change)"
    else:
        return "(N/A - no previous measurement)"

if __name__ == '__main__':
    df = pd.read_table("data/prob1", header=None, names=["val"])
    df['val_lag'] = df['val'].shift(1)
    df['roll_sum'] = df['val'].rolling(window=3).sum()
    df['roll_sum_lag'] = df['roll_sum'].shift(1)
    df['label'] = df[["val", "val_lag"]].apply(label, axis=1)
    df['label2'] = df[["roll_sum", "roll_sum_lag"]].apply(label, axis=1)

    mask = df['label'] == "(increased)"
    print(df[mask]['label'].count())
    mask2 = df['label2'] == "(increased)"
    print(df[mask2]['label2'].count())
else:
        print('This test requires an input file.')






