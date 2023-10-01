import pandas as pd

df = pd.read_excel('C:\\Users\\anjal\\Downloads\\fm.reference.xlsx', sheet_name='fm.reference')
df2 = pd.read_excel('C:\\Users\\anjal\\Downloads\\DoneSoFar.xlsx', sheet_name='Sheet1')
# Find rows in excel1 that are not in excel2
excel1_not_in_excel2 = df.merge(df2, on=df.columns.to_list(), how='left', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)

# Find rows in excel2 that are not in excel1
excel2_not_in_excel1 = df2.merge(df, on=df.columns.to_list(), how='left', indicator=True).query('_merge == "left_only"').drop('_merge', axis=1)


excel1_not_in_excel2.to_excel('excel1_not_in_excel2.xlsx', index=False)
excel2_not_in_excel1.to_excel('excel2_not_in_excel1.xlsx', index=False)