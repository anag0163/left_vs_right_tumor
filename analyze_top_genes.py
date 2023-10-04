import pandas as pd
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest 


df = pd.read_excel('C:\\Users\\anjal\\Downloads\\fm.xlsx', sheet_name='fm')
df2 = pd.read_excel('C:\\Users\\anjal\\Downloads\\fm.clinicaldata.xlsx', sheet_name='fm.clinicaldata')

score_name = 'LRT_score'
dict_for_left = {}
dict_for_right = {}
dictionary_storing_left_right = {}
left_count = 0
right_count = 0
for index, row in df2.iterrows():
    if row['side']=='other':
        continue
    dictionary_storing_left_right[row['Tumor_Sample_Barcode']] = row['side']
#print(dictionary_storing_left_right)

for index, row in df.iterrows():
    tumor_sample = row['Tumor_Sample_Barcode']
    if (tumor_sample in dictionary_storing_left_right and row['Hugo_Symbol'] != '.' and pd.isna(row[score_name]) == False):
        if (dictionary_storing_left_right[tumor_sample] == "left"):
            left_count = left_count+1
            if row['Hugo_Symbol'] not in dict_for_left:
                dict_for_left[row['Hugo_Symbol']]=1
            else:
                dict_for_left[row['Hugo_Symbol']] = dict_for_left[row['Hugo_Symbol']]+1
        else:
            right_count = right_count+1
            if row['Hugo_Symbol'] not in dict_for_right:
                dict_for_right[row['Hugo_Symbol']]=1
            else:
                dict_for_right[row['Hugo_Symbol']] = dict_for_right[row['Hugo_Symbol']]+1

"""
for entry in dict_for_left:
    dict_for_left[entry]= dict_for_left[entry]/left_count
for entry in dict_for_right:
    dict_for_right[entry]= dict_for_right[entry]/right_count
    
"""
    
#print(dict_for_left)
#print(dict_for_right)

p_value_rights_smaller = {}
p_value_lefts_smaller = {}

for gene in dict_for_left:
    if gene in dict_for_right:
        stat, p_value_left_smaller = proportions_ztest([dict_for_left[gene], dict_for_right[gene]], [left_count, right_count], alternative='smaller')
        if (p_value_left_smaller < 0.05) :
            p_value_lefts_smaller[gene] = p_value_left_smaller
        else :
            stat, p_value_right_smaller = proportions_ztest([dict_for_left[gene], dict_for_right[gene]], [left_count, right_count], alternative='larger')
            if (p_value_right_smaller < 0.05):
                p_value_rights_smaller[gene] = p_value_right_smaller
                
print(p_value_lefts_smaller)
print(p_value_rights_smaller)

df = pd.DataFrame(data=p_value_lefts_smaller, index=[0])

df = (df.T)

print (df)

df.to_excel('lefts_smaller.xlsx')


df = pd.DataFrame(data=p_value_rights_smaller, index=[0])

df = (df.T)

print (df)

df.to_excel('rights_smaller.xlsx')