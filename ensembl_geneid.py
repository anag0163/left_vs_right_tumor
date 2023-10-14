import requests
import pandas as pd

df = pd.read_excel('C:\\Users\\anjal\\Downloads\\gene_expression_data.xlsx', sheet_name='step1')

ensembl_id = []
for index, row in df.iterrows():
    gene_name = row['gene_name']
    ensembl_api_endpoint = "https://rest.ensembl.org/xrefs/symbol/"
    response = requests.get(f"{ensembl_api_endpoint}homo_sapiens/{gene_name}?external_db=HGNC;content-type=application/json")
    if (response.status_code == 200):
        try:
            gene_data = response.json()
            print(gene_data[0]['id'])
            ensembl_id.append(gene_data[0]['id'])
        except:
            print("NA")
            ensembl_id.append("NA")
    else:
        print("whoops")
        ensembl_id.append("NA")
    

print(df)        
df.to_excel('ensembl_ids.xlsx')