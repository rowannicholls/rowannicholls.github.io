"""
UCBAdmissions.

PyDataset Documentation (adopted from R Documentation):

Student Admissions at UC Berkeley

Aggregate data on applicants to graduate school at Berkeley for the six
largest departments in 1973 classified by admission and sex.

A 3-dimensional array resulting from cross-tabulating 4526 observations on 3
variables. The variables and their levels are as follows:

1. `Admit`, factor: Admission status (Admitted or Rejected)
2. `Gender`, factor: Male or Female
3. `Dept`, factor: Department (A, B, C, D, E, F)
4. `Freq`, numeric: Number of applicants with this combination of factors

This data set is frequently used for illustrating Simpson's paradox, see
Bickel _et al_ (1975). At issue is whether the data show evidence of sex bias
in admission practices. There were 2691 male applicants, of whom 1198 (44.5%)
were admitted, compared with 1835 female applicants of whom 557 (30.4%) were
admitted. This gives a sample odds ratio of 1.83, indicating that males were
almost twice as likely to be admitted. In fact, graphical methods (as in the
example below) or log-linear modelling show that the apparent association
between admission and sex stems from differences in the tendency of males and
females to apply to the individual departments (females used to apply _more_
to departments with higher rejection rates).

This data set can also be used for illustrating methods for graphical display
of categorical data, such as the general-purpose mosaic plot or the fourfold
display for 2-by-2-by-_k_ tables. See the home page of Michael Friendly
(http://www.math.yorku.ca/SCS/friendly.html) for further information.

References:

Bickel, P. J., Hammel, E. A., and O'Connell, J. W. (1975) Sex bias in graduate
admissions: Data from Berkeley. _Science_, **187**, 398–403.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'UCBAdmissions'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

# Bar plot of admitted vs rejected by gender
# Aggregate counts by Admit and Gender
agg_df = df.groupby(['Admit', 'Gender'])['Freq'].sum().unstack()
agg_df.plot(kind='bar')
plt.xlabel('Admission Status')
plt.ylabel('Number of Applicants')
plt.title(dataset_name)
plt.xticks(rotation=0)
plt.legend(title='Gender')

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
