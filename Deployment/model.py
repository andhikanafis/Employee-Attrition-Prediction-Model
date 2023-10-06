import streamlit as st
import pandas as pd
import pickle

def run():
    # Load All Files
    # Load pipeline.pkl
    with open('pipeline.pkl', 'rb') as file:
        pipeline = pickle.load(file)
    with open('knn_best.pkl', 'rb') as file_2:
        knn_best = pickle.load(file_2)

    st.title('Prediksi Attrition Karyawan')

    # Input data
    OverTime = st.selectbox('OverTime', ['Yes', 'No'])
    TotalWorkingYears = st.slider('Total Working Years', 1, 40)
    StockOptionLevel = st.slider('Stock Option Level', 0, 2)
    MonthlyIncome = st.slider('Monthly Income', 1000, 19513)
    Age = st.slider('Age', 18, 45)
    YearsWithCurrManager = st.slider('Years With Current Manager', 0, 3)
    YearsAtCompany = st.slider('Years At Company', 1, 40)
    JobRole = st.selectbox('Job Role', ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                    'Manufacturing Director', 'Healthcare Representative', 'Manager',
                                    'Sales Representative', 'Research Director', 'Human Resources'])
    YearsInCurrentRole = st.slider('Years In Current Role', 0, 18)
    JobInvolvement = st.selectbox('Job Involvement', [1, 2, 3])

    # Membuat DataFrame dari input pengguna
    input_data = pd.DataFrame({
        'OverTime': [OverTime],
        'TotalWorkingYears': [TotalWorkingYears],
        'StockOptionLevel': [StockOptionLevel],
        'MonthlyIncome': [MonthlyIncome],
        'Age': [Age],
        'YearsWithCurrManager': [YearsWithCurrManager],
        'YearsAtCompany': [YearsAtCompany],
        'JobRole': [JobRole],
        'YearsInCurrentRole': [YearsInCurrentRole],
        'JobInvolvement': [JobInvolvement]
    })

    if st.button(label='Prediksi'):
        # Melakukan prediksi menggunakan model dalam pipeline
        df_inf_prep=pipeline.transform(input_data)
        hasil_prediksi = knn_best.predict(df_inf_prep)
        
        if hasil_prediksi[0] == 0:
            st.write('Karyawan tidak berpotensi untuk keluar (Attrition = No).')
        else:
            st.write('Karyawan berpotensi untuk keluar (Attrition = Yes).')

if __name__ == '__main__':
    run()
