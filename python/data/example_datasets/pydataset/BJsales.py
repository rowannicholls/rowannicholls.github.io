"""
BJsales.

- 2025-08-31: Created
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'BJsales'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

ax = df.plot('time', 'BJsales', legend=False)
ax.set_ylabel('Sales')
ax.set_xlabel('Time')
ax.set_title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
