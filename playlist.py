# mbti_mood_music_simple.py

import streamlit as st

# -------------------------
# 배경 이미지 설정
# -------------------------
def set_background_image(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }}
        .block-container {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 10px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# MBTI + 기분 기반 데이터
# -------------------------
mbti_music_data = {
    "INTJ": {"genres": ["영화 음악", "프로그레시브 록"], "artists": ["Hans Zimmer", "Pink Floyd"]},
    "INTP": {"genres": ["인디", "전자음악"], "artists": ["Tame Impala", "Aphex Twin"]},
    "ENTJ": {"genres": ["팝/록", "클래식"], "artists": ["Queen", "Imagine Dragons"]},
    "ENTP": {"genres": ["퓨전", "인디"], "artists": ["Gorillaz", "Childish Gambino"]},
    "INFJ": {"genres": ["포크", "클래식"], "artists": ["Bon Iver", "Einaudi"]},
    "INFP": {"genres": ["인디 팝", "드림 팝"], "artists": ["Lana Del Rey", "Aurora"]},
    "ENFJ": {"genres": ["팝 발라드", "소울"], "artists": ["Adele", "Sam Smith"]},
    "ENFP": {"genres": ["팝", "EDM"], "artists": ["Dua Lipa", "Avicii"]},
    "ISTJ": {"genres": ["클래식", "컨트리"], "artists": ["Frank Sinatra", "John Mayer"]},
    "ISFJ": {"genres": ["발라드", "OST"], "artists": ["Ed Sheeran", "Taylor Swift"]},
    "ESTJ": {"genres": ["클래식 록", "팝 락"], "artists": ["Bruce Springsteen", "Coldplay"]},
    "ESFJ": {"genres": ["팝", "댄스 팝"], "artists": ["Bruno Mars", "Ariana Grande"]},
    "ISTP": {"genres": ["하드 록", "트랩"], "artists": ["Linkin Park", "Travis Scott"]},
    "ISFP": {"genres": ["인디", "감성 팝"], "artists": ["Lorde", "Phoebe Bridgers"]},
    "ESTP": {"genres": ["힙합", "라틴"], "artists": ["Drake", "Bad Bunny"]},
    "ESFP": {"genres": ["K-pop", "댄스"], "artists": ["BTS", "Katy Perry"]}
}

mood_songs = {
    "행복한": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake"],
    "슬픈": ["Someone Like You - Adele", "Fix You - Coldplay"],
    "차분한": ["Weightless - Marconi Union", "River Flows in You - Yiruma"],
    "신나는": ["Levitating - Dua Lipa", "Uptown Funk - Bruno Mars"]
}

# -------------------------
# Streamlit 앱 시작
# -------------------------
st.set_page_config(page_title="MBTI + 기분 음악 추천기", layout="centered")
set_background_image("https://images.unsplash.com/photo-1521335629791-ce4aec67dd47?auto=format&fit=crop&w=1350&q=80")

st.markdown("<h1 style='text-align: center;'>🎧 MBTI + 기분 음악 추천기</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>당신의 성격과 현재 기분에 어울리는 노래를 추천해드릴게요!</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 사용자 입력
mbti = st.selectbox("당신의 MBTI는 무엇인가요?", list(mbti_music_data.keys()))
mood = st.radio("지금 기분은 어떤가요?", list(mood_songs.keys()))

# 추천 결과
if mbti and mood:
    info = mbti_music_data[mbti]
    songs = mood_songs[mood]

    st.markdown("## 🎼 추천 결과")

    st.write(f"**🎧 MBTI({mbti})에게 어울리는 장르:** {', '.join(info['genres'])}")
    st.write(f"**🎤 추천 아티스트:** {', '.join(info['artists'])}")
    st.write(f"**😊 '{mood}' 기분일 때 어울리는 노래:**")
    for song in songs:
        st.markdown(f"- {song}")
