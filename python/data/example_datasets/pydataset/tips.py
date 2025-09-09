"""
tips.

PyDataset Documentation (adopted from R Documentation):

Tipping data

One waiter recorded information about each tip he received over a period of a
few months working in one restaurant.

A data frame with 244 rows and 7 variables:

- tip in dollars
- bill in dollars
- sex of the bill payer
- whether there were smokers in the party
- day of the week
- time of day
- size of the party

In all he recorded 244 tips. The data was reported in a collection of case
studies for business statistics (Bryant & Smith 1995).

References:

Bryant, P. G. and Smith, M (1995) _Practical Data Analysis: Case Studies in
Business Statistics_. Homewood, IL: Richard D. Irwin Publishing:
"""
import os
from matplotlib import pyplot as plt
from pydataset import data

dataset_name = 'tips'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

for day, group in df.groupby('day'):
    plt.scatter(group['total_bill'], group['tip'], label=day, alpha=0.7)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title(dataset_name)
plt.legend(title='Day')
plt.grid(True, linestyle='--', alpha=0.5)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
