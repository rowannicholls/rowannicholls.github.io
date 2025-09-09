"""
JohnsonJohnson.

PyDataset Documentation (adopted from R Documentation):

Quarterly Earnings per Johnson & Johnson Share

Quarterly earnings (dollars) per Johnson & Johnson share 1960–80.

A quarterly time series

- `[,1] time`: numeric, The time index (in fractional years)
- `[,2] value`: numeric, Quarterly earnings per share

Source:

Shumway, R. H. and Stoffer, D. S. (2000) _Time Series Analysis and its
Applications_. Second Edition. Springer. Example 1.1.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'JohnsonJohnson'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Line plot of quarterly earnings over time
plt.plot(df['time'], df['JohnsonJohnson'])
plt.xlabel('Time (Year)')
plt.ylabel('Quarterly Earnings per Share (USD)')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
