"""
USAccDeaths.

PyDataset Documentation (adopted from R Documentation):

Accidental Deaths in the US 1973–1978

A time series giving the monthly totals of accidental deaths in the USA. The
values for the first six months of 1979 are 7798 7406 8363 8460 9217 9316.

P. J. Brockwell and R. A. Davis (1991) _Time Series: Theory and Methods._
Springer, New York.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'USAccDeaths'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

plt.plot(df['time'], df['USAccDeaths'])
plt.xlabel('Year')
plt.ylabel('Deaths')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
