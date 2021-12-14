import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

#load file yang diperlukan
file_json = open ('D:\\Test py\\UAS\\kode_negara_lengkap.json')
file_json = file_json.read()
negara = json.loads(file_json)
negara_dict = pd.DataFrame.from_dict(negara)
df = pd.read_csv('D:\\Test py\\UAS\\produksi_minyak_mentah.csv')
df.loc[(df[['produksi']] != 0).all(axis=1)]
kode = list()

#input-input
input_negara = input('Enter location: ')
input_negara = input_negara.title()
tahun = int(input("Masukkan tahun yang diinginkan: "))
jumlah_negara = int(input("Masukkan jumlah negara: "))

#Soal a
awal = next((x for x in negara if x["name"] == input_negara), None)
    
for k, v in awal.items():
    if k == 'alpha-3':
        kode.append(v)

kode_string = kode[0]

pilihan = df[(df["kode_negara"] == kode_string)]

pilihan.plot.bar(x='tahun', y='produksi')

#Soal b
daftar_tahun = df[(df["tahun"]==tahun)]
daftar_tahun = daftar_tahun.sort_values(by='produksi', ascending=False)
jumlah_negara_tot = jumlah_negara + 1
produksi_terbesar_urut = daftar_tahun[1:jumlah_negara_tot]

#Soal c
df['Total'] = df.groupby(['kode_negara'])['produksi'].transform('sum')
new_df = df.drop_duplicates(subset=['kode_negara'])
produksi_terbesar = new_df.sort_values(by='Total', ascending=False)
slice_prod_terbesar = ['kode_negara','tahun','Total']
produksi_terbesar [slice_prod_terbesar]

number_of_input = jumlah_negara + 1
produksi_terbesar_urut = produksi_terbesar[1:number_of_input]

produksi_terbesar_urut.plot.bar(x='kode_negara', y='Total', rot=0)

#Soal d
#bagian 1
dataframe = pd.DataFrame.from_dict(negara)
produksi_terbesar_urut
slice_produksi = ['produksi']
tahun_terbanyak = produksi_terbesar_urut [slice_produksi]
tahun_terbanyak_str = tahun_terbanyak.head(1)['produksi'].values[0]

slice_nama_negara = ['kode_negara']
negara_tahun_terbanyak = produksi_terbesar_urut [slice_nama_negara]
negara_tahun_terbanyak_str = negara_tahun_terbanyak.head(1)['kode_negara'].values[0]
print (negara_tahun_terbanyak_str)

slice = ['name','alpha-3','region','sub-region']
list_negara = negara_dict[(negara_dict["name"] == negara_tahun_terbanyak_str)]
list_negara_fix = list_negara [slice]
list_negara_fix ['produksi-terbanyak-tahun ', tahun] = tahun_terbanyak_str

total_prod = produksi_terbesar[(produksi_terbesar["kode_negara"] == kode_string)]
prod_total_str = total_prod.head(1)['Total'].values[0]
list_negara_fix ['total-produksi'] = prod_total_str