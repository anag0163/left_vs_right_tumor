#In this program, I flag rows that contain incorrect information for columns 9-12 (in the fm spreadsheet using the fm reference sheet) 

import pandas as pd

df = pd.read_excel('C:\\Users\\anjal\\Downloads\\fmFinal.xlsx', sheet_name='fm')
df2 = pd.read_excel('C:\\Users\\anjal\\Downloads\\fmrefFinal.xlsx', sheet_name='Sheet1')

dict_for_reference = {}
dict_for_current = {}

for index, row in df2.iterrows():
    correct_reference = row['HGVSc']
    dict_for_reference[index] = correct_reference

for index, row in df.iterrows():
    current_reference = row['txChange']
    dict_for_current[index] = current_reference

list_of_flags = []
for item in dict_for_reference:
    if (dict_for_current[item] != dict_for_reference[item]):
        current_row = df.iloc[item]
        #print(current_row['AAChange.refGene'])
        try:
            text = current_row['AAChange.refGene'].split(":")
        except:
            current_row['Debugging_Messages'] = "Sorry but there was no text to analyze"
            print("Sorry but there was no text to analyze")
        #print(text)
        try:
            index = text.index(dict_for_reference[item])
            current_row['aaChange'] = text[index+1]
            current_row['txChange'] = text[index]
            current_row['exon'] = text[index-1]
            current_row['tx'] = text[index-2]
            print(index)
        except ValueError:
            current_row['Debugging_Messages'] = "We couldnt find the reference HGVSc in the list for row"
            print("We couldnt find the reference HGVSc in the list for row" + str(item+2))
            print("this is for gene " + current_row['Hugo_Symbol'])
        df.iloc[item] = current_row
        
        
print(df)
df.to_excel("NewFM.xlsx", index=False)


    