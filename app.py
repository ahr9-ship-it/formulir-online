import streamlit as st
st. set_page_config(page_title="formulir online" ,page_icon="📝")
st.title("📝 formulir onlie")
st.write("jujur itu bagus, jawab ya!.")
with st.form("formulir_kamu"):
    nama = st.text_input("nama lengkap")
    umur = st.number_input("umur" ,
                           min_value=1 ,
                           max-value=30 ,step=1)
    pesan = st.text_area("pesan atau jawaban kamu")
    kirim = st.form_submit_button("kirm jawaban")
if kirim:
    if nama.strip() and pesan.strip():
        st.success("tengkyu besti ini lagi belajar aja.")
        st.write("Nama:", nama)
        st.write("Umur:", umur)
        st.write("Pesan:", pesan)
    else:
        st.warning("isi nama dan pesan terlebih dahulu.")
