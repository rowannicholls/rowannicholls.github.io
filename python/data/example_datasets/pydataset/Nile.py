"""
Nile.

PyDataset Documentation (adopted from R Documentation):

Flow of the River Nile

Measurements of the annual flow of the river Nile at Ashwan 1871–1970.

A time series of length 100.

- `[,1] time`: numeric, The time index (years)
- `[,2] value`: numeric, Annual flow of the Nile (10^8 m^3)

Source:

Durbin, J. and Koopman, S. J. (2001) _Time Series Analysis by State Space
Methods._ Oxford University Press. http://www.ssfpack.com/DKbook.html

References:

Balke, N. S. (1993) Detecting level shifts in time series. _Journal of
Business and Economic Statistics_ **11**, 81–92.

Cobb, G. W. (1978) The problem of the Nile: conditional solution to a change-
point problem. _Biometrika_ **65**, 243–51.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'Nile'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Line plot of Nile flow over time
plt.plot(df['time'], df['Nile'])
plt.xlabel('Year')
plt.ylabel('Annual Flow (10^8 m³)')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
