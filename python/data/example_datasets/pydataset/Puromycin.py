"""
Puromycin.

PyDataset Documentation (adopted from R Documentation):

Reaction Velocity of an Enzymatic Reaction

The `Puromycin` data frame has 23 rows and 3 columns of the reaction velocity
versus substrate concentration in an enzymatic reaction involving untreated
cells or cells treated with Puromycin.

This data frame contains the following columns:

- `conc`: a numeric vector of substrate concentrations (ppm)
- `rate`: a numeric vector of instantaneous reaction rates (counts/min/min)
- `state`: a factor with levels `treated` `untreated`

Data on the velocity of an enzymatic reaction were obtained by Treloar (1974).
The number of counts per minute of radioactive product from the reaction was
measured as a function of substrate concentration in parts per million (ppm)
and from these counts the initial rate (or velocity) of the reaction was
calculated (counts/min/min). The experiment was conducted once with the enzyme
treated with Puromycin, and once with the enzyme untreated.

Source:

Bates, D.M. and Watts, D.G. (1988), _Nonlinear Regression Analysis and Its
Applications_, Wiley, Appendix A1.3.

Treloar, M. A. (1974), _Effects of Puromycin on Galactosyltransferase in Golgi
Membranes_, M.Sc. Thesis, U. of Toronto.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'Puromycin'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Scatter plot of reaction rate vs. concentration, colored by state
for state, group_df in df.groupby('state'):
    plt.scatter(group_df['conc'], group_df['rate'], label=state)

plt.xlabel('Substrate Concentration (µM)')
plt.ylabel('Reaction Rate')
plt.title(dataset_name)
plt.legend(title='State')

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
