"""
BOD.

- 2025-08-31: Created
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'BOD'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

ax = df.plot('Time', 'demand', legend=False)
ax.set_ylabel('Biochemical Oxygen Demand (mg/l)')
ax.set_xlabel('Time (Days)')
ax.set_title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
