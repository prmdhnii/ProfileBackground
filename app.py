import streamlit as st
from pathlib import Path

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Profil | Dashboard",
    page_icon="🧑‍💻",
    layout="wide",
)

# =========================================================
# ISI DATA — EDIT BAGIAN INI SESUAI DATA KAMU
# =========================================================

PROFILE = {
    "nama": "Nama Lengkap Kamu",
    "peran": "Job Title / Peran Kamu (contoh: Data Analyst)",
    "lokasi": "Kota, Indonesia",
    "email": "email@contoh.com",
    "linkedin": "https://linkedin.com/in/username-kamu",
    "github": "https://github.com/username-kamu",
    "foto": "assets/foto.jpg",  # ganti dengan file foto kamu di folder assets/
    "tentang": (
        "Tulis deskripsi singkat tentang dirimu di sini. "
        "Ceritakan latar belakang, minat, dan tujuan karier kamu "
        "dalam 3-5 kalimat."
    ),
}

EXPERIENCE = [
    {
        "posisi": "Nama Posisi",
        "perusahaan": "Nama Perusahaan",
        "periode": "Jan 2023 - Sekarang",
        "deskripsi": [
            "Poin tanggung jawab / pencapaian pertama.",
            "Poin tanggung jawab / pencapaian kedua.",
            "Poin tanggung jawab / pencapaian ketiga.",
        ],
    },
    {
        "posisi": "Nama Posisi Sebelumnya",
        "perusahaan": "Nama Perusahaan Sebelumnya",
        "periode": "Jun 2021 - Des 2022",
        "deskripsi": [
            "Poin tanggung jawab / pencapaian pertama.",
            "Poin tanggung jawab / pencapaian kedua.",
        ],
    },
]

CERTIFICATIONS = [
    {
        "nama": "Nama Sertifikasi / Pelatihan",
        "penerbit": "Nama Lembaga / Platform",
        "tahun": "2024",
        "link": "https://contoh-link-sertifikat.com",
    },
    {
        "nama": "Nama Sertifikasi Lainnya",
        "penerbit": "Nama Lembaga / Platform",
        "tahun": "2023",
        "link": "",
    },
]

# Skill teknis: nilai 0-100 dipakai untuk progress bar
SKILLS_TEKNIS = {
    "Python": 85,
    "SQL": 80,
    "Data Visualization": 75,
    "Microsoft Excel": 90,
    "Streamlit": 70,
}

# Skill non-teknis / soft skill: ditampilkan sebagai badge
SOFT_SKILLS = [
    "Komunikasi",
    "Kerja Tim",
    "Problem Solving",
    "Manajemen Waktu",
    "Adaptif",
]

# =========================================================
# CSS RINGAN UNTUK TAMPILAN
# =========================================================
st.markdown(
    """
    <style>
    .card {
        padding: 1.2rem 1.5rem;
        border-radius: 14px;
        background-color: rgba(135, 135, 135, 0.08);
        margin-bottom: 1rem;
    }
    .badge {
        display: inline-block;
        padding: 0.35rem 0.9rem;
        margin: 0.2rem;
        border-radius: 999px;
        background-color: rgba(99, 102, 241, 0.15);
        color: #6366f1;
        font-size: 0.85rem;
        font-weight: 600;
    }
    .section-title {
        margin-top: 0.5rem;
        margin-bottom: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# HEADER / PROFIL
# =========================================================
col_foto, col_info = st.columns([1, 3], gap="large")

with col_foto:
    foto_path = Path(PROFILE["foto"])
    if foto_path.exists():
        st.image(str(foto_path), use_container_width=True)
    else:
        st.info("📷 Letakkan foto kamu di `assets/foto.jpg` agar tampil di sini.")

with col_info:
    st.markdown(f"## {PROFILE['nama']}")
    st.markdown(f"**{PROFILE['peran']}**  \n📍 {PROFILE['lokasi']}")

    kontak_cols = st.columns(4)
    with kontak_cols[0]:
        st.markdown(f"✉️ [{PROFILE['email']}](mailto:{PROFILE['email']})")
    with kontak_cols[1]:
        st.markdown(f"🔗 [LinkedIn]({PROFILE['linkedin']})")
    with kontak_cols[2]:
        st.markdown(f"🐙 [GitHub]({PROFILE['github']})")

    st.write("")
    st.write(PROFILE["tentang"])

st.divider()

# =========================================================
# TAB NAVIGASI: Experience | Sertifikasi | Skill
# =========================================================
tab_exp, tab_cert, tab_skill = st.tabs(
    ["💼 Pengalaman", "🎓 Sertifikasi & Pelatihan", "🛠️ Kemampuan"]
)

# ---------- TAB PENGALAMAN ----------
with tab_exp:
    st.markdown("### Riwayat Pengalaman")
    for exp in EXPERIENCE:
        with st.container():
            st.markdown(
                f"""
                <div class="card">
                    <h4 style="margin-bottom:0;">{exp['posisi']}</h4>
                    <p style="margin-bottom:0.3rem; opacity:0.8;">
                        {exp['perusahaan']} &nbsp;·&nbsp; {exp['periode']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            for poin in exp["deskripsi"]:
                st.markdown(f"- {poin}")
            st.write("")

# ---------- TAB SERTIFIKASI ----------
with tab_cert:
    st.markdown("### Sertifikasi & Pelatihan")
    cols = st.columns(2)
    for i, cert in enumerate(CERTIFICATIONS):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <h5 style="margin-bottom:0.2rem;">{cert['nama']}</h5>
                    <p style="margin-bottom:0.2rem; opacity:0.8;">
                        {cert['penerbit']} · {cert['tahun']}
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            if cert.get("link"):
                st.markdown(f"[Lihat sertifikat →]({cert['link']})")
            st.write("")

# ---------- TAB SKILL ----------
with tab_skill:
    st.markdown("### Kemampuan Teknis")
    for skill, level in SKILLS_TEKNIS.items():
        st.write(f"**{skill}**")
        st.progress(level / 100)

    st.write("")
    st.markdown("### Soft Skill")
    badges_html = "".join(f'<span class="badge">{s}</span>' for s in SOFT_SKILLS)
    st.markdown(badges_html, unsafe_allow_html=True)

st.divider()
st.caption("Dibuat dengan ❤️ menggunakan Streamlit")
