"""
LakeHuron.

PyDataset Documentation (adopted from R Documentation):

Level of Lake Huron 1875–1972

Annual measurements of the level, in feet, of Lake Huron 1875–1972.

A time series of length 98.

- `[,1] time`: numeric, The time index (years)
- `[,2] value`: numeric, Level of Lake Huron (feet)

Source:

Brockwell, P. J. and Davis, R. A. (1991). _Time Series and Forecasting
Methods_. Second edition. Springer, New York. Series A, page 555.

Brockwell, P. J. and Davis, R. A. (1996). _Introduction to Time Series and
Forecasting_. Springer, New York. Sections 5.1 and 7.6.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'LakeHuron'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Line plot of water levels over time
plt.plot(df['time'], df['LakeHuron'])
plt.xlabel('Year')
plt.ylabel('Lake Level (feet)')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
