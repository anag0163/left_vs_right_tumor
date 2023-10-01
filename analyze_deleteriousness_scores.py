import pandas as pd
from scipy.stats import mannwhitneyu


df = pd.read_excel('C:\\Users\\anjal\\Downloads\\fm.xlsx', sheet_name='fm')
df2 = pd.read_excel('C:\\Users\\anjal\\Downloads\\fm.clinicaldata.xlsx', sheet_name='fm.clinicaldata')

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
    if (tumor_sample in dictionary_storing_left_right and row['SIFT_score'] != '.' and pd.isna(row['SIFT_score']) == False):
        if (dictionary_storing_left_right[tumor_sample] == "left"):
            scores_for_left.append(row['SIFT_score'])
        else:
            scores_for_right.append(row['SIFT_score'])
print(scores_for_right)
print(scores_for_left)
statistic, p_value = mannwhitneyu(scores_for_right, scores_for_left, alternative='less')
print(f"Wilcoxon statistic: {statistic}")
print(f"P-value: {p_value}")