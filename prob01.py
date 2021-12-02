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
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        df = pd.read_table("data/prob1", header=None, names=["val"])
        df['val_lag'] = df['val'].shift(1)
        df['label'] = df[["val", "val_lag"]].apply(label, axis=1)
        mask = df['label'] == "(increased)"
        print(df[mask]['label'].count())
    else:
        print('This test requires an input file.')






