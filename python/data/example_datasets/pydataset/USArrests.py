"""
USArrests

PyDataset Documentation (adopted from R Documentation):

Violent Crime Rates by US State

This data set contains statistics, in arrests per 100,000 residents for
assault, murder, and rape in each of the 50 US states in 1973. Also given is
the percent of the population living in urban areas.

A data frame with 50 observations on 4 variables.

- `[,1] Murder`, numeric: Murder arrests (per 100,000)
- `[,2] Assault`, numeric: Assault arrests (per 100,000)
- `[,3] UrbanPop`, numeric: Percent urban population
- `[,4] `Rape`, numeric: Rape arrests (per 100,000)

Source:

World Almanac and Book of facts 1975. (Crime rates).

Statistical Abstracts of the United States 1975. (Urban rates).

References:

McNeil, D. R. (1977) _Interactive Data Analysis_. New York: Wiley.
"""
import os

from matplotlib import pyplot as plt
from pydataset import data
import seaborn as sns

dataset_name = 'USArrests'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())
sns.pairplot(df, diag_kind='kde')

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
