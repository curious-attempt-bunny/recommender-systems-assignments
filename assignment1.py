import pandas as pd
import numpy as np

df = pd.read_csv('assignment1.csv', header=0, index_col=['User'])

# 318: Shawshank Redemption, The (1994)                      3.600000
# 260: Star Wars: Episode IV - A New Hope (1977)             3.266667
# 541: Blade Runner (1982)                                   3.222222
# 1265: Groundhog Day (1993)                                 3.166667
# 593: Silence of the Lambs, The (1991)                      3.062500
df.mean().order(ascending=False)

# 318: Shawshank Redemption, The (1994)                      0.700000
# 260: Star Wars: Episode IV - A New Hope (1977)             0.533333
# 3578: Gladiator (2000)                                     0.500000
# 541: Blade Runner (1982)                                   0.444444
# 593: Silence of the Lambs, The (1991)                      0.437500
(df[ df >= 4 ].count() / df.count()).order(ascending=False)

# 1: Toy Story (1995)                                        17
# 593: Silence of the Lambs, The (1991)                      16
# 260: Star Wars: Episode IV - A New Hope (1977)             15
# 1210: Star Wars: Episode VI - Return of the Jedi (1983)    14
# 780: Independence Day (ID4) (1996)                         13
df.count().order(ascending=False)

# 1: Toy Story (1995)                                        0.933333
# 1210: Star Wars: Episode VI - Return of the Jedi (1983)    0.866667
# 593: Silence of the Lambs, The (1991)                      0.800000
# 780: Independence Day (ID4) (1996)                         0.733333
# 2916: Total Recall (1990)                                  0.666667
reference = '260: Star Wars: Episode IV - A New Hope (1977)'
def calc(x):
    return (1.0*(df[reference] * x).count())/df[reference].count() # Not sure why 1.0* is needed here to coerce to a float
df.apply(calc, axis=0).order(ascending=False)

