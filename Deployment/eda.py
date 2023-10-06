import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

def run():

    st.title('Welcome to Explaration Data Analysis')

    df= pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
    st.table(df.head(5))
    with st.expander('Penjelasan:'):
        st.caption('Ini adalah Tabel Data')

    st.title('Persentase Attrition')
    # Membuat plot pie dari kolom 'Attrition'
    fig, ax = plt.subplots(figsize=(7, 7))
    (df['Attrition'].value_counts()).plot.pie(autopct="%1.1f%%", colors=['#836096', '#ED7B7B'], ax=ax)
    plt.title('Attrition Percentage')

    # Menampilkan plot dalam aplikasi Streamlit
    st.pyplot(fig)
#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Hasil : Kebanyakan Karyawan Di Perusahaan Bertahan Di Perusahaan.')

    st.title('Hubungan antara Attrition dengan Gender')
    # Buat plot menggunakan seaborn
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Attrition', hue='Gender')
    plt.xlabel('Attrition')
    plt.ylabel('Count')
    plt.title('Attrition by Gender')

    # Tampilkan plot di Streamlit
    st.pyplot(plt)
#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Hasil : Karyawan laki laki lebih cenderung untuk bertahan di perusahaan di banding dengan karyawan wanita.')

    # Judul Aplikasi Streamlit
    st.title('Grafik Education Terhadap Attrition')

    # Menampilkan plot menggunakan Seaborn
    sns.set(style='whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.countplot(data=df, x='Education', hue='Attrition', ax=ax)
    plt.title('Education Terhadap Attrition')
    plt.xlabel('Education')
    plt.ylabel('Count')

    # Menampilkan plot di aplikasi Streamlit
    st.pyplot(fig)  # Menggunakan 'fig' sebagai argumen untuk st.pyplot()
   
    #menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Hasil : Karyawan dengan level Edukasi 3/Bachelor memiliki tinggal Attration yang kecil.')

    # Judul Aplikasi
    st.title('Visualisasi Attrition Terhadap Tahun Bekerja')

    # Pilihan kolom untuk ditampilkan
    pilihan_kolom = st.selectbox('Pilih Kolom:', ['YearsAtCompany', 'YearsInCurrentRole', 'TotalWorkingYears'])

    # Visualisasi
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.countplot(data=df, x=pilihan_kolom, hue='Attrition', palette=['red', 'green'])
    plt.title('Relasi terhadap Attrition')
    plt.xlabel(pilihan_kolom)
    plt.ylabel('Count')

    # Tampilkan visualisasi di Streamlit
    st.pyplot(fig)  # Gunakan figur yang telah dibuat
    #menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Hasil : Karyawan yang baru berkerja dibawah 5 tahun, memiliki jumlah attrition yang paling tinggi di banding yang lain.')

