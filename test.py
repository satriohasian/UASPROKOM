import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

file_json = open ('D:\\Test py\\UAS\\kode_negara_lengkap.json')
file_json = file_json.read() #biar jadi string
negara = json.loads(file_json) #masukin ke python
df = pd.read_csv('D:\\Test py\\UAS\\produksi_minyak_mentah.csv')
'''df_indexed = df.set_index("kode_negara")'''
kode = list()

while True:
    input_negara = input('Enter location: ')
    input_negara = input_negara.title()
    if len(input_negara) < 1: break

    awal = next((x for x in negara if x["name"] == input_negara), None)
    
    for k, v in awal.items():
        if k == 'alpha-3':
            kode.append(v)

    kode_string = kode[0]

    tahun = input('Enter year of production: ')
    
    new = df[(df["tahun"]==tahun)&(df["kode_negara"]==kode_string)]
    
    print(new)

'''    index_kode_negara = df_indexed.loc[kode_string]'''
    


    
'''    print (index_kode_negara["tahun"] == tahun)'''