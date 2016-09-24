import pandas as pd
import numpy as np

attributes = pd.read_csv('assignment2.attributes.csv', header=0, index_col=['doc'])

ratings = pd.read_csv('assignment2.ratings.csv', header=0, index_col=['doc'])

profiles = pd.DataFrame(np.zeros((len(ratings.columns), len(attributes.columns))), columns=attributes.columns, index=ratings.columns)

for user in ratings.columns:
    print attributes.apply(lambda x: x*ratings[user], axis=0)
    profiles.ix[user] = attributes.apply(lambda x: x*ratings[user], axis=0).sum()
