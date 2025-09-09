"""
ToothGrowth.

PyDataset Documentation (adopted from R Documentation):

The Effect of Vitamin C on Tooth Growth in Guinea Pigs

The response is the length of odontoblasts (teeth) in each of 10 guinea pigs
at each of three dose levels of Vitamin C (0.5, 1, and 2 mg) with each of two
delivery methods (orange juice or ascorbic acid).

A data frame with 60 observations on 3 variables.

- `[,1] len`, numeric: Tooth length
- `[,2] supp`, factor: Supplement type (VC or OJ).
- `[,3] dose`, numeric: Dose in milligrams.

Source:

C. I. Bliss (1952) _The Statistics of Bioassay_. Academic Press.

References:

McNeil, D. R. (1977) _Interactive Data Analysis_. New York: Wiley.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'ToothGrowth'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Boxplot of tooth length by supplement type
df.boxplot(column='len', by='supp')
plt.suptitle('')
plt.xlabel('Supplement Type')
plt.ylabel('Tooth Length')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
