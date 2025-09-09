"""
Titanic.

PyDataset Documentation (adopted from R Documentation):

Survival of passengers on the Titanic

This data set provides information on the fate of passengers on the fatal
maiden voyage of the ocean liner ‘Titanic’, summarized according to economic
status (class), sex, age and survival.

A 4-dimensional array resulting from cross-tabulating 2201 observations on 4
variables. The variables and their levels are as follows:

1. `Class`: 1st, 2nd, 3rd, Crew
2. `Sex`: Male, Female
3. `Age`: Child, Adult
4. `Survived`: No, Yes

The sinking of the Titanic is a famous event, and new books are still being
published about it. Many well-known facts—from the proportions of first-class
passengers to the ‘women and children first’ policy, and the fact that that
policy was not entirely successful in saving the women and children in the
third class—are reflected in the survival rates for various classes of
passenger.

These data were originally collected by the British Board of Trade in their
investigation of the sinking. Note that there is not complete agreement among
primary sources as to the exact numbers on board, rescued, or lost.

Due in particular to the very successful film ‘Titanic’, the last years saw a
rise in public interest in the Titanic. Very detailed data about the
passengers is now available on the Internet, at sites such as _Encyclopedia
Titanica_ (http://www.rmplc.co.uk/eduweb/sites/phind).

Source:

Dawson, Robert J. MacG. (1995), The ‘Unusual Episode’ Data Revisited. _Journal
of Statistics Education_, **3**.
http://www.amstat.org/publications/jse/v3n3/datasets.dawson.html

The source provides a data set recording class, sex, age, and survival status
for each person on board of the Titanic, and is based on data originally
collected by the British Board of Trade and reprinted in:

British Board of Trade (1990), _Report on the Loss of the ‘Titanic’ (S.S.)_.
British Board of Trade Inquiry Report (reprint). Gloucester, UK: Allan Sutton
Publishing.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'Titanic'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())
# Pivot data for easier plotting
pivot_df = df.pivot_table(index='Class', columns='Sex', values='Freq', aggfunc='sum')

pivot_df.plot(kind='bar')
plt.xlabel('Class')
plt.ylabel('Count')
plt.title(dataset_name)
plt.xticks(rotation=0)
plt.legend(title='Sex')

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
