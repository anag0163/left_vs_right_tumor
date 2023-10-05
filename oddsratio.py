import pandas as pd
from scipy.stats import mannwhitneyu
import matplotlib.pyplot as plt
from statsmodels.stats.proportion import proportions_ztest 
import scipy.stats as stats


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
print(dict_for_left)
print(dict_for_right)

p_value_left_genes = {}
p_value_right_genes = {}

for gene in dict_for_left:
   left_side_present = dict_for_left[gene]
   left_side_absent = left_count - left_side_present
   if gene in dict_for_right:
        right_side_present = dict_for_right[gene]
   else:
       right_side_present = 0
   right_side_absent = right_count - right_side_present
   odds_ratio_side_a, p_value_side_a = stats.fisher_exact([[left_side_present, left_side_absent], [right_side_present, right_side_absent]])
   if (p_value_side_a < 0.05):
       p_value_left_genes[gene] = p_value_side_a
       
for gene in dict_for_right:
   right_side_present = dict_for_right[gene]
   right_side_absent = right_count - right_side_present
   if gene in dict_for_left:
        left_side_present = dict_for_left[gene]
   else:
        left_side_present = 0
   left_side_absent = left_count - left_side_present
   odds_ratio_side_a, p_value_side_a = stats.fisher_exact([[right_side_present, right_side_absent], [left_side_present, left_side_absent]])
   if (p_value_side_a < 0.05):
       p_value_right_genes[gene] = p_value_side_a

                
print(p_value_left_genes)
print(p_value_right_genes)

df = pd.DataFrame(data=p_value_left_genes, index=[0])

df = (df.T)

print (df)

df.to_excel('left_associated.xlsx')


df = pd.DataFrame(data=p_value_right_genes, index=[0])

df = (df.T)

print (df)

df.to_excel('right_associated.xlsx')