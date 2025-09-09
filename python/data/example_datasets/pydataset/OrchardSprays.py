"""
OrchardSprays.

PyDataset Documentation (adopted from R Documentation):

Potency of Orchard Sprays

An experiment was conducted to assess the potency of various constituents of
orchard sprays in repelling honeybees, using a Latin square design.

A data frame with 64 observations on 4 variables.

- `[,1] decrease`: numeric, The response (decrease in bee visits)
- `[,2] rowpos`: numeric, Row position in the orchard
- `[,3] colpos`: numeric, Column position in the orchard
- `[,4] treatment`: factor, Type of spray treatment

Individual cells of dry comb were filled with measured amounts of lime sulphur
emulsion in sucrose solution. Seven different concentrations of lime sulphur
ranging from a concentration of 1/100 to 1/1,562,500 in successive factors of
1/5 were used as well as a solution containing no lime sulphur.

The responses for the different solutions were obtained by releasing 100 bees
into the chamber for two hours, and then measuring the decrease in volume of
the solutions in the various cells.

An _8 x 8_ Latin square design was used and the treatments were coded as
follows:

- `A`: highest level of lime sulphur
- `B`: next highest level of lime sulphur

...

- `G`: lowest level of lime sulphur
- `H`: no lime sulphur

Source:

Finney, D. J. (1947) _Probit Analysis_. Cambridge.

References:

McNeil, D. R. (1977) _Interactive Data Analysis_. New York: Wiley.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'OrchardSprays'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Boxplot of decrease by treatment
df.boxplot(column='decrease', by='treatment')
plt.suptitle('')
plt.xlabel('Treatment')
plt.ylabel('Decrease in Bee Visits')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
