"""Unpaired Two-Sample t-Tests."""
import numpy as np
from scipy import stats as st
from sklearn import datasets
from matplotlib import pyplot as plt
from matplotlib import lines
import seaborn as sns

"""
Example Data
"""
# Load the dataset
breast_cancer = datasets.load_breast_cancer(as_frame=True)
# Extract the feature and target data together
df = breast_cancer['frame']
# Clean the raw data
df['target'] = df['target'].apply(lambda x: breast_cancer['target_names'][x])

# Extract the data
cols = ['mean smoothness', 'target']
df = df[cols]
# Rename
df = df.rename(columns={'mean smoothness': 'smoothness'})
print(df.tail())

# Plot
ax = plt.axes()
sns.boxplot(
   df, x='target', y='smoothness', color='lightgrey', whis=[0, 100],
   showmeans=True, meanline=True, meanprops={'color': 'black'}
)
sns.stripplot(
   df, x='target', y='smoothness',
   color='lightgrey', edgecolor='black', linewidth=1
)
ax.set_title('Breast Cancer Wisconsin Dataset')
ax.set_ylabel('Tumour Smoothness')
ax.set_ylim([0, 0.17])
ax.set_xlabel('')
ax.set_xticklabels(['Malignant', 'Benign'])
handles = [lines.Line2D([0], [0], color='k', linewidth=1, linestyle='--')]
ax.legend(handles, ['Group Means'], loc='lower left')
# plt.savefig('load_breast_cancer.png')

"""
Choose a Statistical Test
"""
# Sample sizes
n = df['target'].value_counts()
print(n)

# Homogeneity of variance (using sample standard deviations)
s = df.groupby('target')['smoothness'].std(ddof=1)
ratio = s[0] / s[1]
print(f'Ratio of standard deviations: {ratio:.2f}')

"""
Descriptive Statistics
"""
# Sample means
x_bar = df.groupby('target')['smoothness'].mean()
print(x_bar)

# Difference between the sample means
diff_btwn_means = x_bar.diff()
diff_btwn_means = diff_btwn_means.dropna()[0]
print(f'Difference between the means: {diff_btwn_means:.4f}')

# # https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_confidence_intervals/bs704_confidence_intervals5.html
# n = [1623, 1911]
# s = [17.5, 20.1]
# x_bar = [128.2, 126.5]
# diff_btwn_means = x_bar[0] - x_bar[1]

# # https://www.statology.org/confidence-interval-difference-between-means/
# n = [15, 15]
# s = [18.5, 16.4]
# x_bar = [310, 300]
# diff_btwn_means = x_bar[0] - x_bar[1]

# # https://en.wikipedia.org/wiki/Student%27s_t-test#Equal_variances
# x_0 = np.array([30.02, 29.99, 30.11, 29.97, 30.01, 29.99])
# x_1 = np.array([29.89, 29.93, 29.72, 29.98, 30.02, 29.98])
# n = [len(x_0), len(x_1)]
# s = [np.std(x_0, ddof=1), np.std(x_1, ddof=1)]
# x_bar = [np.mean(x_0), np.mean(x_1,)]
# diff_btwn_means = x_bar[0] - x_bar[1]

# Degrees of freedom
dof = n[0] + n[1] - 2
# Pooled standard deviation
s_p = np.sqrt(((n[0] - 1) * s[0]**2 + (n[1] - 1) * s[1]**2) / dof)
print(f'Pooled standard deviation: {s_p:.4f}')

# Standard error (SE) of the difference between sample means
se = s_p * np.sqrt((1 / n[0]) + (1 / n[1]))
print(f'Standard error (SE) of the difference between sample means: {se:.5f}')

# Confidence interval
upper = diff_btwn_means + 1.96 * se
lower = diff_btwn_means - 1.96 * se
print(f'Difference between the means: {diff_btwn_means:.4f}, 95% CI [{lower:.4f}, {upper:.4f}]')

# Confidence level
C = 0.95  # 95%
# Significance level, α
alpha = 1 - C
# Number of tails
tails = 2
# Quantile (the cumulative probability)
q = 1 - (alpha / tails)
# Critical z-score, calculated using the percent-point function (aka the
# quantile function) of the normal distribution
z_star = st.norm.ppf(q)
print(f'95% of values lie within {z_star:.5f} standard deviations of the mean')

# t-statistic
t_statistic = diff_btwn_means / se
print(f't = {t_statistic:.3f}')

# p-value
p_value = (1 - st.t.cdf(t_statistic, dof)) * 2
print(f'p = {p_value:.3f}')

# Separate out the samples
malignant = df.groupby('target').get_group('malignant')
benign = df.groupby('target').get_group('benign')
# Unpaired two-sample Student's t-test
t_statistic, p_value = st.ttest_ind(malignant['smoothness'], benign['smoothness'])
print(f'Two-sample t-test: s = {t_statistic:5.3f}, p = {p_value:.2e}')


def get_significance(p):
    """Get the significance of a p-values as a string of stars."""
    if p <= 0.001:
        return '***'
    elif p <= 0.01:
        return '**'
    elif p <= 0.05:
        return '*'
    elif p <= 0.1:
        return '.'
    else:
        return ''


def round_p_value(p):
    """Round a small p-value so that it is human-readable."""
    if p < 0.001:
        return '<0.001'
    else:
        return f'{p:5.3}'


p_rounded = round_p_value(p_value)
significance = get_significance(p_value)

print(f'The p-value is {p_rounded} ({significance})')
