"""
UKDriverDeaths.

PyDataset Documentation (adopted from R Documentation):

Road Casualties in Great Britain 1969–84

`UKDriverDeaths` is a time series giving the monthly totals of car drivers in
Great Britain killed or seriously injured Jan 1969 to Dec 1984. Compulsory
wearing of seat belts was introduced on 31 Jan 1983.

`Seatbelts` is more information on the same problem.

`Seatbelts` is a multiple time series, with columns

- `DriversKilled`: car drivers killed.
- `drivers`: same as `UKDriverDeaths`.
- `front`: front-seat passengers killed or seriously injured.
- `rear`: rear-seat passengers killed or seriously injured.
- `kms`: distance driven.
- `PetrolPrice`: petrol price.
- `VanKilled`: number of van (‘light goods vehicle’) drivers.
- `law`: 0/1: was the law in effect that month?

Sources:

Harvey, A.C. (1989) _Forecasting, Structural Time Series Models and the Kalman
Filter._ Cambridge University Press, pp. 519–523.

Durbin, J. and Koopman, S. J. (2001) _Time Series Analysis by State Space
Methods._ Oxford University Press. http://www.ssfpack.com/dkbook/

Reference:

Harvey, A. C. and Durbin, J. (1986) The effects of seat belt legislation on
British road casualties: A case study in structural time series modelling.
_Journal of the Royal Statistical Society_ series B, **149**, 187–227.
"""
from matplotlib import pyplot as plt
from pydataset import data
import os

dataset_name = 'UKDriverDeaths'
# data(dataset_name, show_doc=True)
df = data(dataset_name)
print(df.head())

plt.plot(df['time'], df['UKDriverDeaths'])
plt.xlabel('Year')
plt.ylabel('Deaths')
plt.title(dataset_name)

if 'pydataset' in os.getcwd():
    plt.savefig(dataset_name)
else:
    plt.savefig(os.path.join('pydataset', dataset_name))
