import pandas as pd
import numpy as np

attributes = pd.read_csv('assignment2.attributes.csv', header=0, index_col=['doc'])

ratings = pd.read_csv('assignment2.ratings.csv', header=0, index_col=['doc'])

profiles = pd.DataFrame(np.zeros((len(ratings.columns), len(attributes.columns))), columns=attributes.columns, index=ratings.columns)

for user in ratings.columns:
    profiles.ix[user] = attributes.apply(lambda x: x*ratings[user], axis=0).sum()

weights = 1 / attributes.T.sum().pow(0.5)

weighted_attributes = attributes * 1.0

for doc in weights.index:
    weighted_attributes.ix[doc] *= weights.ix[doc]

weighted_profiles = pd.DataFrame(np.zeros((len(ratings.columns), len(attributes.columns))), columns=attributes.columns, index=ratings.columns)

for user in ratings.columns:
    weighted_profiles.ix[user] = weighted_attributes.apply(lambda x: x*ratings[user], axis=0).sum()

predictions = pd.DataFrame(np.zeros((len(attributes.index), len(ratings.columns))), columns=ratings.columns, index=attributes.index)

for user in ratings.columns:
    for doc in weighted_attributes.index:
        predictions.ix[doc][user] = (weighted_attributes.ix[doc]*weighted_profiles.ix[user]).sum()

print predictions['User 1'].sort_values(ascending=False)
