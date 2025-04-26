import streamlit as st

st.markdown("""
    <style>
    .main {
        background-color: #99BC85;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #4CAF50;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🧫 KALKULATOR KOLONI BAKTERI</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Capek hitung bakteri? Biar kami bantu 🤪</p>', unsafe_allow_html=True)

st.write("Masukkan datamu di bawah ini, dan lihat hasilnya 🎯.")



jumlah_koloni = st.number_input("🧫 Masukkan jumlah koloni:", min_value=0, step=1)
faktor_pengenceran = st.number_input("💧 Masukkan faktor pengenceran:", min_value=1, step=1)
volume_inokulasi = st.number_input("📏 Masukkan volume inokulasi (mL):", min_value=0.01, step=0.01)


if st.button("🚀 Hitung CFU/mL"):
if faktor_pengenceran > 0 and volume_inokulasi > 0:
hasil = jumlah_koloni / (faktor_pengenceran * volume_inokulasi)
        st.success(f"🎯 Hasilnya: {hasil:.2f} CFU/mL")
        st.balloons()
else:
        st.error("Faktor pengenceran dan volume inokulasi harus lebih besar dari 0!")



 st.markdown("""
            <audio autoplay>
                <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
            </audio>
            """, unsafe_allow_html=True)
        st.info("Hitungannya udah beres, sekarang waktunya happy! 🦠🥳")
    else:
        st.error("❌ Volume inokulasi tidak boleh nol!")

st.markdown('</div>', unsafe_allow_html=True)


