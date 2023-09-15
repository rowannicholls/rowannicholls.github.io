# import matplotlib.pyplot as plt

# # Plot
# plt.scatter(df['hue'], df['malic_acid'], c=df['cultivator'])
# plt.title('Wine recognition dataset')
# plt.xlabel('hue')
# plt.ylabel('malic_acid')
# plt.show()

from sklearn import datasets

# Load the dataset
wine = datasets.load_wine(as_frame=True)

# Extract the feature data only
features = wine['data']

# Extract the target data only
target = wine['target']

# Extract the feature and target data together
df = wine['frame']

# print(df.head())

from matplotlib import pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(5, 3, figsize=(8, 10))
for i, ax in enumerate(fig.get_axes()):
    if i < 13:
        feature = wine['feature_names'][i]
        sns.boxplot(df, x='target', y=feature, whis=[0, 100], ax=ax)
        ax.set_title(feature)
        ax.set_ylabel('')
        ax.set_xlabel('')
fig.delaxes(axs[(4, 2)])
fig.delaxes(axs[(4, 1)])
plt.tight_layout()
plt.savefig('wine.png')
