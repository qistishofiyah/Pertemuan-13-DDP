import streamlit as st
# Side Bar Direktory
dashboard = st.Page("./Fitur/dashboard.py", title="dashboard")
nabung = st.Page("./Fitur/nabung.py", title="nabung")
penarikan = st.Page("./Fitur/penarikan.py", title="penarikan")

pg = st.navigation(
  {
    "dashboard":[dashboard],
    "transaksi":[nabung, penarikan],
    
  }
)

if 'jumlah' not in st.session_state:
  st.session_state['jumlah'] = []

  
# Menjalankan Navigasi
pg.run()


