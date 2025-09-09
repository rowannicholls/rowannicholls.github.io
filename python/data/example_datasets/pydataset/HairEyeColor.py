"""
HairEyeColor.

- 2025-08-31: Created
"""
from matplotlib import pyplot as plt
from pydataset import data
from statsmodels.graphics.mosaicplot import mosaic
import os

dataset_name = 'HairEyeColor'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

ser = df.set_index(['Hair', 'Eye', 'Sex'])['Freq']
mosaic(ser)
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
