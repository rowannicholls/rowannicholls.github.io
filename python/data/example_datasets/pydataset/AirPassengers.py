"""
AirPassengers.

- 2025-08-19: Created
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'AirPassengers'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

ax = df.plot('time', 'AirPassengers', legend=False)
ax.set_ylabel('Number of Air Passengers')
ax.set_xlabel('Year')
ax.set_title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
