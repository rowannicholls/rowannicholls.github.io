import pandas as pd
import numpy as np

# Set Pandas display options
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 120)

# Create a data frame
raw = pd.DataFrame({
    'only_text': ['Value 1', 'Value 2', 'Value 3', 'Value 4'],
    'only_trues': [True, True, True, True],
    'text_and_nones': ['Value 1', 'Value 2', None, None],
    'only_falses': [False, False, False, False],
    'only_nones': [None, None, None, None],
    'only_nans': [np.NaN, np.NaN, np.NaN, np.NaN],
    'only_zeroes': [0, 0, 0, 0],
    'falses_and_nones': [False, False, None, None],
    'falses_and_nans': [False, False, np.NaN, np.NaN],
    'falses_and_zeroes': [False, False, 0, 0],
    'nones_and_nans': [None, None, np.NaN, np.NaN],
    'nones_and_zeroes': [None, None, 0, 0],
    'nans_and_zeroes': [np.NaN, np.NaN, 0, 0],
}, dtype='object')

print(raw)

#
# Drop Columns That Only Contain "False"
#
# Make a copy of the data frame
df = raw.copy()

# Find which columns contain only Booleans and only Falses. Use the `bool_only=True`
# option with the `any()` method to have it only recognise Booleans:
bool_cols = ~df.any(bool_only=True)
only_falses = bool_cols[bool_cols]
# Get the names of these columns
cols_only_falses = only_falses.index.to_list()
# Remove these columns
df = df.drop(cols_only_falses, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# The same output can be achieved using a loop:
#
# Make a copy of the data frame
df = raw.copy()

# Drop the columns that only contain 'False'
for col in list(df.any(bool_only=True)[~df.any(bool_only=True)].index):
    df = df.drop(col, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "None"
#
# Make a copy of the data frame
df = raw.copy()

# Find the nones
nones = df.applymap(type) == type(None)
# Find columns with only nones
cols = nones.all()[nones.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "NaN"
#
# Make a copy of the data frame
df = raw.copy()

# Find the nans
nans = (df.isna()) & (df.applymap(type) != type(None))
# Find columns with only nans
cols = nans.all()[nans.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "0"
#
# Make a copy of the data frame
df = raw.copy()

# Find the zeroes
zeroes = (df == 0) & (df.applymap(type) == int)
# Find columns with only zeroes
cols = zeroes.all()[zeroes.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "False" and "None"
#
# Make a copy of the data frame
df = raw.copy()

# Find the falses
falses = (df == False) & (df.astype(str) != '0')
# Find the nones
nones = df.applymap(type) == type(None)
# Find both the falses and the nones
falses_nones = falses | nones
# Find columns with only falses and nones
cols = falses_nones.all()[falses_nones.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "False" and "NaN"
#
# Make a copy of the data frame
df = raw.copy()

# Find the falses
falses = (df == False) & (df.astype(str) != '0')
# Find the nans
nans = (df.isna()) & (df.applymap(type) != type(None))
# Find both the falses and the nans
falses_nans = falses | nans
# Find columns with only falses and nans
cols = falses_nans.all()[falses_nans.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "False" and "0"
#
# Make a copy of the data frame
df = raw.copy()

# Find columns that only contain falses and zeroes
only_falses_zeroes = (df == 0).all()
falses_zeroes_cols = only_falses_zeroes[only_falses_zeroes].index.to_list()
# Remove these columns which are all nones
df = df.drop(falses_zeroes_cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "None" and "NaN"
#
# Make a copy of the data frame
df = raw.copy()

# Drop the columns that only contain Nones and/or NaNs
for col in df:
    if df[col].isnull().all():
        df = df.drop(col, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Version 2
#
# Make a copy of the data frame
df = raw.copy()

# Drop the columns that only contain 'None' and/or 'NaN'
df = df.dropna(axis='columns', how='all')

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "None" and "0"
#
# Make a copy of the data frame
df = raw.copy()

# Find the nones
nones = df.applymap(type) == type(None)
# Find the zeroes
zeroes = df.astype(str) == '0'
# Find both the nones and the zeroes
nones_zeroes = nones | zeroes
# Find columns with only nones and nones
cols = nones_zeroes.all()[nones_zeroes.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "NaN" and "0"
#
# Make a copy of the data frame
df = raw.copy()

# Find the nans
nans = (df.isna()) & (df.applymap(type) != type(None))
# Find the zeroes
zeroes = df.astype(str) == '0'
# Find both the nans and the zeroes
nans_zeroes = nans | zeroes
# Find columns with only nans and zeroes
cols = nans_zeroes.all()[nans_zeroes.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "False", "None" and "NaN"
#
# Make a copy of the data frame
df = raw.copy()

# Find the falses
falses = (df == False) & (df.astype(str) != '0')
# Find the nones
nones = df.applymap(type) == type(None)
# Find the nans
nans = (df.isna()) & (df.applymap(type) != type(None))
# Combine the above
falses_nones_nans = falses | nones | nans
# Find columns with only nones and nones
cols = falses_nones_nans.all()[falses_nones_nans.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "False", "None" and "0"
#
# Make a copy of the data frame
df = raw.copy()

# Drop the columns that only contain 'False', 'None' and 'NaN'
for col in list(df):
    if not df[col].astype('bool').any():
        df = df.drop(col, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "False", "NaN" and "0"
#
# Make a copy of the data frame
df = raw.copy()

# Find the falses
falses = (df == False) & (df.astype(str) != '0')
# Find the nans
nans = (df.isna()) & (df.applymap(type) != type(None))
# Find the zeroes
zeroes = df.astype(str) == '0'
# Combine the above
falses_nans_zeroes = falses | nans | zeroes
# Find columns with only nones and nones
cols = falses_nans_zeroes.all()[falses_nans_zeroes.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "None", "NaN" and "0"
#
# Make a copy of the data frame
df = raw.copy()

# Find the nones
nones = df.applymap(type) == type(None)
# Find the nans
nans = (df.isna()) & (df.applymap(type) != type(None))
# Find the zeroes
zeroes = df.astype(str) == '0'
# Combine the above
nones_nans_zeroes = nones | nans | zeroes
# Find columns with only nones and nones
cols = nones_nans_zeroes.all()[nones_nans_zeroes.all()].index.to_list()
# Drop these columns
df = df.drop(cols, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Drop Columns That Only Contain "False", "None", "NaN" and "0"
#
# Make a copy of the data frame
df = raw.copy()

# Drop the columns that only contain 'False', 'None', 'NaN' and '0'
df = df.drop(df.any()[~df.any()].index, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))

#
# Version 2
#
# Make a copy of the data frame
df = raw.copy()

# Drop the columns that only contain Falses, Nones and/or NaNs
for col in df:
    if not df[col].any():
        df = df.drop(col, axis=1)

# Which columns have been removed?
print(set(list(raw)) - set(list(df)))
