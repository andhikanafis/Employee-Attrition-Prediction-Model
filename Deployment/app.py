import streamlit as st
from PIL import Image 
import eda
import model


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])
def home_page():
    st.header('Welcome Page') 
    st.write('')
    img = Image.open('hacktiv8-1.png')
    st.image(img, use_column_width=True)  # Menggunakan use_column_width=True untuk membuat gambar memiliki lebar kolom yang sama
    st.write('Milestone 2')
    st.write('Nama      : Andhika Abdurachim Nafis')
    st.write('Batch     : HCK-007')
    st.write('Tujuan Milestone2    : Program ini dilakukan untuk memenuhi Milestone 2, dan bertujuan untuk membuat model yang bisa memprediksi kemungkinan attrition karyawan di masa depan berdasarkan atribut-atribut yang ada dalam dataset.')
    st.write('')

    st.write('')
    with st.expander("Problem Statement"):
        st.caption('Problem Statement : Project ini bertujuan untuk merancang model predisi, menggunakan data dalam dataset IBM HR Analytics Attrition, mengenali faktor-faktor yang memengaruhi tingkat attrition (keluar) karyawan di perusahaan. Tingkat attrition yang tinggi dapat memiliki dampak negatif pada produktivitas perusahaan, biaya rekrutmen, dan kemampuan perusahaan untuk mempertahankan karyawan.')

# Mengatur tampilan agar konten halaman 'Home Page' berada di tengah
st.write("<style>div.Widget.row-widget.stRadio > div{flex-direction:row; justify-content:center;}</style>", unsafe_allow_html=True)

# Menampilkan konten sesuai halaman yang dipilih
if page == 'Home Page':
    home_page()
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model .run()
