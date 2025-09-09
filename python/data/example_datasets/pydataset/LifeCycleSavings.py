"""
LifeCycleSavings.

PyDataset Documentation (adopted from R Documentation):

Intercountry Life-Cycle Savings Data

Data on the savings ratio 1960–1970.

A data frame with 50 observations on 5 variables.

- `[,1] sr`: numeric, Aggregate personal savings ratio
- `[,2] pop15`: numeric, % of population under 15
- `[,3] pop75`: numeric, % of population over 75
- `[,4] dpi`: numeric, Real per-capita disposable income
- `[,5] ddpi`: numeric, Growth rate of dpi

Under the life-cycle savings hypothesis as developed by Franco Modigliani, the
savings ratio (aggregate personal saving divided by disposable income) is
explained by per-capita disposable income, the percentage rate of change in
per-capita disposable income, and two demographic variables: the percentage of
population less than 15 years old and the percentage of the population over 75
years old. The data are averaged over the decade 1960–1970 to remove the
business cycle or other short-term fluctuations.

Source:

The data were obtained from Belsley, Kuh and Welsch (1980). They in turn
obtained the data from Sterling (1977).

References:

Sterling, Arnie (1977) Unpublished BS Thesis. Massachusetts Institute of
Technology.

Belsley, D. A., Kuh. E. and Welsch, R. E. (1980) _Regression Diagnostics_. New
York: Wiley.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'LifeCycleSavings'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Scatter plot: savings ratio vs. disposable income
plt.scatter(df['dpi'], df['sr'])
plt.xlabel('Real per-capita disposable income (dpi)')
plt.ylabel('Personal savings ratio (sr)')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
