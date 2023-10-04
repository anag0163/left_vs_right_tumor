import pandas as pd
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt


df = pd.read_excel('C:\\Users\\anjal\\Downloads\\fm.xlsx', sheet_name='fm')
df2 = pd.read_excel('C:\\Users\\anjal\\Downloads\\fm.clinicaldata.xlsx', sheet_name='fm.clinicaldata')

score_name = 'LRT_score'
scores_for_left = []
scores_for_right = []
dictionary_storing_left_right = {}

for index, row in df2.iterrows():
    if row['side']=='other':
        continue
    dictionary_storing_left_right[row['Tumor_Sample_Barcode']] = row['side']
#print(dictionary_storing_left_right)

for index, row in df.iterrows():
    tumor_sample = row['Tumor_Sample_Barcode']
    if (tumor_sample in dictionary_storing_left_right and row[score_name] != '.' and pd.isna(row[score_name]) == False):
        if (dictionary_storing_left_right[tumor_sample] == "left"):
            scores_for_left.append(row[score_name])
        else:
            scores_for_right.append(row[score_name])
print(scores_for_right)
print(scores_for_left)
statistic, p_value = mannwhitneyu(scores_for_right, scores_for_left, alternative='less')
print(f"Wilcoxon statistic: {statistic}")
print(f"P-value: {p_value}")

fig, ax = plt.subplots()

data_to_plot = [scores_for_right, scores_for_left]
ax.violinplot(data_to_plot)

ax.set_xlabel('Tumor Side')
ax.set_ylabel(score_name)
ax.set_title('Side-by-Side Boxplots')

plt.show()
