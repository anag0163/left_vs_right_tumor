import subprocess
import urllib.parse
import pandas as pd 
wget_path = '/path/to/wget'  # Replace with the actual path to wget
# URL of the resource you want to download

df = pd.read_excel('C:\\Users\\anjal\\Downloads\\gene_coordinates.xlsx', sheet_name='data_with_coords')
user_input = input("num1")
user_input1 = input("num2")
output_num = input("output")
base_url = "http://www.ensembl.org/biomart/martservice?query="
for index, row in df.iloc[int(user_input):int(user_input1)].iterrows():
    chromosone_num = row['Chromosome_Number']
    start = row['Start']
    end = row['End']
    xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
    <Query virtualSchemaName="default" formatter="TSV" header="0" uniqueRows="0" count="" datasetConfigVersion="0.6">
    <Dataset name="hsapiens_regulatory_feature" interface="default">
    <Filter name="chromosome_name" value="{chromosone_num}"/>
    <Filter name="end" value="{end}"/>
    <Filter name="start" value="{start}"/>
    <Filter name="regulatory_feature_type_name" value="CTCF Binding Site,Enhancer,Open chromatin,Promoter,TF binding"/>
    <Attribute name="chromosome_name" />
    <Attribute name="chromosome_start" />
    <Attribute name="chromosome_end" />
    <Attribute name="feature_type_name" />
    </Dataset></Query>"""

    encoded_xml = urllib.parse.quote(xml_content)

    filename = f'download{output_num}.txt'
    url = base_url + encoded_xml
    # Construct the wget command
    wget_command = f'wget -O {filename} {url}'

    # Execute the wget command
    subprocess.call(wget_command, shell=True)
    
    with open(f'download{output_num}.txt', 'r') as file:
        with open(f'output{output_num}.txt', 'a') as output_file:
                # Read each line from the input file
                for line in file:
                    # Process or modify the line as needed
                    processed_line = line.strip()+ " " + str(row['stat']) + " " + row['gene_id'] + " " + row['gene_name'] + " "+row['gene_type'] +" "+ str(row['Chromosome_Number']) + " "+str(row['Start']) + " "+str(row['End']) +'\n'
                    print(processed_line)
                    # Write the modified line to the output file
                    output_file.write(processed_line)


