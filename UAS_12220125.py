#UAS IF-2112 KELAS 01
#SATRIO HASIAN SITANGGANG
#12220125
#Aplikasi Analisis Produksi Minyak

import json
import pandas as pd
import streamlit as st

#load file yang diperlukan
file_json = open('kode_negara_lengkap.json')
file_json = file_json.read()
negara = json.loads(file_json)
negara_dict = pd.DataFrame.from_dict(negara)
df = pd.read_csv('produksi_minyak_mentah.csv')
df = df.set_index('kode_negara')
df = df.drop(["WLD", "G20", "OECD", "OEU", "EU28"])
df = df.reset_index()
kode = list()
listnegara=dict()

#layout
st.sidebar.header ("Input data yang diinginkan:")
st.title ('APLIKASI PRODUKSI MINYAK NEGARA TAHUN 1971 S/D 2015')
st.subheader ('UAS IF-2112 Kelas 01')
st.caption ('Oleh: Satrio Hasian Sitanggang | NIM: 12220125')
st.caption ('------------------------')
st.sidebar.caption ('----------------')

#input-input
for i in negara:
    listnegara[i["name"]] = i["alpha-3"]

input_negara = st.sidebar.selectbox ('Pilih negara', listnegara)
tahun = st.sidebar.slider('Pilih tahun yang diinginkan', min_value=1971, max_value=2015, step=1)
jumlah_negara = st.sidebar.number_input('Masukkan jumlah negara yang indin ditampilkan', min_value=1, max_value=200, step=1)

#Soal a
kode_string = listnegara[input_negara]

pilihan = df[(df["kode_negara"] == kode_string)]
slice_pilihan = ["tahun","produksi"]
pilihan1 = pilihan [slice_pilihan]
pilihan1.set_index('tahun',inplace=True)

st.subheader('Grafik Jumlah Produksi Minyak Mentah terhadap Waktu (Tahun) Negara ' + input_negara)
st.line_chart(pilihan1)

#Soal b
daftar_tahun = df[(df["tahun"]==tahun)]
daftar_tahun = daftar_tahun.sort_values(by='produksi', ascending=False)
produksi_terbesar_urut = daftar_tahun [0:int(jumlah_negara)]
slice_prod_kode = ["produksi","kode_negara"]
produksi_terbesar_urut = produksi_terbesar_urut [slice_prod_kode]
produksi_terbesar_urut.set_index('kode_negara', inplace=True)
st.subheader(str(int(jumlah_negara)) + ' Besar Negara dengan Jumlah Produksi Terbesar pada Tahun ' + str(tahun))
st.bar_chart(produksi_terbesar_urut)

#Soal c
df['Total'] = df.groupby(['kode_negara'])['produksi'].transform('sum')
new_df = df.drop_duplicates(subset=['kode_negara'])
produksi_terbesar = new_df.sort_values(by='Total', ascending=False)

produksi_terbesar_urut_total = produksi_terbesar [0:int(jumlah_negara)]

slice_prod_terbesar = ['kode_negara','Total']
prod = produksi_terbesar_urut_total [slice_prod_terbesar]
prod.set_index('kode_negara', inplace=True)

st.subheader('Grafik ' + str(int(jumlah_negara)) + ' Besar Negara dengan Jumlah Produksi Terbesar Secara Kumulatif ')
st.bar_chart(prod)

#Soal d
#mencari total produksi dari tahun yang diinput
pilihan_tahun = df[(df["tahun"] == tahun)]
pilihan_tahun['Total'] = pilihan_tahun.groupby(['tahun'])['produksi'].transform('sum')
new_df_tahun = pilihan_tahun.drop_duplicates(subset=['tahun'])
prod_terbanyak_total_str = new_df_tahun.iloc[0]['Total']

st.subheader('Produksi Total pada Tahun ' + str(tahun))
st.write(prod_terbanyak_total_str)

#bagian 1
produksi_urut = daftar_tahun [0:1]

prod_tahun_terbanyak_str = produksi_urut.iloc[0]['produksi']
negara_tahun_terbanyak_str = produksi_urut.iloc[0]['kode_negara']

slice = ['name','alpha-3','region','sub-region']
list_negara = negara_dict[(negara_dict["alpha-3"] == negara_tahun_terbanyak_str)]
list_negara_fix = list_negara [slice]
list_negara_fix ['jumlah_produksi'] = prod_tahun_terbanyak_str

pilihan_high = df[(df["kode_negara"] == negara_tahun_terbanyak_str)]
slice_pilihan_high = ["kode_negara", "tahun", "produksi"]
pilihan1_high = pilihan_high [slice_pilihan_high]

pilihan1_high['Total_dalam_setahun_high'] = pilihan1_high.groupby(['kode_negara'])['produksi'].transform('sum')
new_df_total_tahun_high = pilihan1_high.drop_duplicates(subset=['tahun'])
total_high_str = new_df_total_tahun_high.iloc[0]['Total_dalam_setahun_high']

list_negara_fix ['total-produksi-negara'] = total_high_str
list_negara_fix = list_negara_fix.set_index('name')

st.subheader('Negara dengan Produksi Terbesar pada Tahun ' + str(tahun))
st.dataframe (list_negara_fix)

#bagian 2
df_new = df.loc[(df[['produksi']] != 0).all(axis=1)]

daftar_tahun_low = df_new[(df_new["tahun"]==tahun)]
daftar_tahun_low = daftar_tahun_low.sort_values(by='produksi', ascending=True)
produksi_terbesar_urut_low = daftar_tahun_low [0:int(jumlah_negara)]
slice_prod_kode_low = ["produksi","kode_negara"]
produksi_terbesar_urut_low = produksi_terbesar_urut_low [slice_prod_kode_low]

produksi_urut_low = daftar_tahun_low [0:1]

prod_tahun_terkecil_str = produksi_urut_low.iloc[0]['produksi']
negara_tahun_terkecil_str = produksi_urut_low.iloc[0]['kode_negara']

slice = ['name','alpha-3','region','sub-region']
list_negara_low = negara_dict[(negara_dict["alpha-3"] == negara_tahun_terkecil_str)]
list_negara_fix_low = list_negara_low [slice]
list_negara_fix_low ['jumlah_produksi'] = prod_tahun_terkecil_str

pilihan_low = df_new[(df_new["kode_negara"] == negara_tahun_terkecil_str)]
slice_pilihan_low = ["kode_negara", "tahun", "produksi"]
pilihan1_low = pilihan_low [slice_pilihan_low]

pilihan1_low['Total_dalam_setahun_low'] = pilihan1_low.groupby(['kode_negara'])['produksi'].transform('sum')
new_df_total_tahun_low = pilihan1_low.drop_duplicates(subset=['tahun'])
total_low_str = new_df_total_tahun_low.iloc[0]['Total_dalam_setahun_low']

list_negara_fix_low ['total-produksi-negara'] = total_low_str
list_negara_fix_low = list_negara_fix_low.set_index('name')

st.subheader('Negara dengan Produksi Terkecil pada Tahun ' + str(tahun))
st.dataframe (list_negara_fix_low)

#bagian 3 part 1
daftar_nol = daftar_tahun[(daftar_tahun["produksi"] == 0)]
kode_negara_list = daftar_nol['kode_negara'].values.tolist()

kode_list = list()
nama_list = list()
region_list = list()
sub_region_list = list()

for i in negara:
    if i['alpha-3'] in kode_negara_list:
        kode_list.append(i['alpha-3'])
        nama_list.append(i['name'])
        region_list.append(i['region'])
        sub_region_list.append(i['sub-region'])

data_total_nol = {"name" : nama_list, "alpha-3": kode_list, "region": region_list, "sub-region": sub_region_list}
data_frame_total_nol = pd.DataFrame(data_total_nol).set_index('name')

st.subheader('Negara dengan Produksi 0 pada Tahun ' + str(tahun))
st.write (data_frame_total_nol)

#bagian 3 part 2
produksi_nol_kumulatif = new_df.sort_values(by='Total', ascending=False)
daftar_nol_tot = produksi_nol_kumulatif[(produksi_nol_kumulatif["Total"] == 0)]
kode_negara_list_nol = daftar_nol_tot['kode_negara'].values.tolist()

kode_list_nol = list()
nama_list_nol = list()
region_list_nol = list()
sub_region_list_nol = list()

for i in negara:
    if i['alpha-3'] in kode_negara_list_nol:
        kode_list_nol.append(i['alpha-3'])
        nama_list_nol.append(i['name'])
        region_list_nol.append(i['region'])
        sub_region_list_nol.append(i['sub-region'])

data_total_nol_kumulatif = {"name" : nama_list_nol, "alpha-3": kode_list_nol, "region": region_list_nol, "sub-region": sub_region_list_nol}
data_frame_total_nol_kumulatif = pd.DataFrame(data_total_nol_kumulatif).set_index('name')

st.subheader('Negara dengan Produksi 0 pada Keseluruhan Tahun')
st.write (data_frame_total_nol_kumulatif)