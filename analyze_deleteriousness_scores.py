import pandas as pd

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
    if (tumor_sample in dictionary_storing_left_right):
        if (dictionary_storing_left_right[tumor_sample] == "left"):
            scores_for_left.append(row['SIFT_score'])
        else:
            scores_for_right.append(row['SIFT_score'])
print(scores_for_right)
print(scores_for_left)