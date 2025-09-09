"""
PlantGrowth.

PyDataset Documentation (adopted from R Documentation):

Results from an Experiment on Plant Growth

Results from an experiment to compare yields (as measured by dried weight of
plants) obtained under a control and two different treatment conditions.

A data frame of 30 cases on 2 variables.

- `[,1] weight`: numeric, Dry weight of the plants
- `[,2] group`: factor, Treatment group (`ctrl`, `trt1`, `trt2`)

Source:

Dobson, A. J. (1983) _An Introduction to Statistical Modelling_. London:
Chapman and Hall.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'PlantGrowth'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Boxplot of plant weight by treatment group
df.boxplot(column='weight', by='group')
plt.suptitle('')
plt.xlabel('Group')
plt.ylabel('Weight')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
