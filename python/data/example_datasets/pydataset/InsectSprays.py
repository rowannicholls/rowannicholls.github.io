"""
InsectSprays.

PyDataset Documentation (adopted from R Documentation):

Effectiveness of Insect Sprays

The counts of insects in agricultural experimental units treated with
different insecticides.

A data frame with 72 observations on 2 variables.

- `[,1] count`: numeric, Insect count
- `[,2] spray`: factor, The type of spray

Source:

Beall, G., (1942) The Transformation of data from entomological field
experiments, _Biometrika_, **29**, 243–262.

References:

McNeil, D. (1977) _Interactive Data Analysis_. New York: Wiley.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'InsectSprays'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

df.boxplot(column='count', by='spray')
plt.suptitle('')
plt.xlabel('spray')
plt.ylabel('count')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
