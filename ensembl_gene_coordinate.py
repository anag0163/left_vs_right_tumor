import requests
import pandas as pd
import openpyxl


df = pd.read_excel('C:\\Users\\anjal\\Downloads\\gene_expression_data.xlsx', sheet_name='significant_data')
user_input = input("num1")
user_input1 = input("num2")

    
for index, row in df.iloc[int(user_input):int(user_input1)].iterrows():
    id = row['gene_id'].split(".")
    ensembl_api_endpoint = "https://rest.ensembl.org/lookup/id/"
    response = requests.get(f"{ensembl_api_endpoint}{id[0]}?content-type=application/json")
    if (response.status_code == 200):
        try:
            gene_data = response.json()
            print(gene_data['seq_region_name'] + " " + str(gene_data['start']) + " "+ str(gene_data['end']))
        except:
            print("NA")
    else:
        print("whoops")
    

