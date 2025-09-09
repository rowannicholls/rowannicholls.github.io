"""
UKgas.

PyDataset Documentation (adopted from R Documentation):

UK Quarterly Gas Consumption

Quarterly UK gas consumption from 1960Q1 to 1986Q4, in millions of therms.

A quarterly time series of length 108.

Source:

Durbin, J. and Koopman, S. J. (2001) _Time Series Analysis by State Space
Methods._ Oxford University Press. http://www.ssfpack.com/dkbook/
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'UKgas'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

plt.plot(df['time'], df['UKgas'])
plt.xlabel('Year')
plt.ylabel('Gas Consumption')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
