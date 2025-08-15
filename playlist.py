# mbti_mood_music_fancy.py

import streamlit as st

# -------------------------
# MBTI 데이터: 성격, 장르, 아티스트
# -------------------------
mbti_data = {
    "INTJ": {
        "desc": "독창적이고 전략적인 성향을 지닌 사색가형.",
        "genres": ["영화 음악", "프로그레시브 록"],
        "artists": ["Hans Zimmer", "Pink Floyd"]
    },
    "INTP": {
        "desc": "호기심 많고 논리적인 철학자형.",
        "genres": ["인디", "전자음악"],
        "artists": ["Tame Impala", "Aphex Twin"]
    },
    "ENTJ": {
        "desc": "리더십과 추진력이 강한 지휘관형.",
        "genres": ["팝/록", "클래식"],
        "artists": ["Queen", "Imagine Dragons"]
    },
    "ENTP": {
        "desc": "새로운 아이디어에 열정적인 발명가형.",
        "genres": ["퓨전", "인디"],
        "artists": ["Gorillaz", "Childish Gambino"]
    },
    "INFJ": {
        "desc": "이상주의적이고 직관적인 옹호자형.",
        "genres": ["포크", "클래식"],
        "artists": ["Bon Iver", "Einaudi"]
    },
    "INFP": {
        "desc": "감성적이고 깊은 생각을 지닌 중재자형.",
        "genres": ["인디 팝", "드림 팝"],
        "artists": ["Lana Del Rey", "Aurora"]
    },
    "ENFJ": {
        "desc": "따뜻한 카리스마를 가진 선도자형.",
        "genres": ["팝 발라드", "소울"],
        "artists": ["Adele", "Sam Smith"]
    },
    "ENFP": {
        "desc": "자유롭고 창의적인 활동가형.",
        "genres": ["팝", "EDM"],
        "artists": ["Dua Lipa", "Avicii"]
    },
    "ISTJ": {
        "desc": "신중하고 책임감 있는 관리자형.",
        "genres": ["클래식", "컨트리"],
        "artists": ["Frank Sinatra", "John Mayer"]
    },
    "ISFJ": {
        "desc": "헌신적이고 온화한 수호자형.",
        "genres": ["발라드", "OST"],
        "artists": ["Ed Sheeran", "Taylor Swift"]
    },
    "ESTJ": {
        "desc": "체계적이고 현실적인 경영자형.",
        "genres": ["클래식 록", "팝 락"],
        "artists": ["Bruce Springsteen", "Coldplay"]
    },
    "ESFJ": {
        "desc": "따뜻하고 친절한 사교가형.",
        "genres": ["팝", "댄스 팝"],
        "artists": ["Bruno Mars", "Ariana Grande"]
    },
    "ISTP": {
        "desc": "유연하고 현실적인 장인형.",
        "genres": ["하드 록", "트랩"],
        "artists": ["Linkin Park", "Travis Scott"]
    },
    "ISFP": {
        "desc": "예술적이고 조용한 예술가형.",
        "genres": ["인디", "감성 팝"],
        "artists": ["Lorde", "Phoebe Bridgers"]
    },
    "ESTP": {
        "desc": "모험을 즐기는 활동가형.",
        "genres": ["힙합", "라틴"],
        "artists": ["Drake", "Bad Bunny"]
    },
    "ESFP": {
        "desc": "자유롭고 에너지 넘치는 연예인형.",
        "genres": ["K-pop", "댄스"],
        "artists": ["BTS", "Katy Perry"]
    }
}

# -------------------------
# 기분에 따른 배경 이미지 및 추천곡
# -------------------------
mood_data = {
    "행복한": {
        "bg": "https://images.unsplash.com/photo-1498931299472-f7a63a5a1cfa?auto=format&fit=crop&w=1350&q=80",
        "songs": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake"]
    },
    "슬픈": {
        "bg": "https://images.unsplash.com/photo-1608889174521-637750df981f?auto=format&fit=crop&w=1350&q=80",
        "songs": ["Someone Like You - Adele", "Fix You - Coldplay"]
    },
    "차분한": {
        "bg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1350&q=80",
        "songs": ["Weightless - Marconi Union", "River Flows in You - Yiruma"]
    },
    "신나는": {
        "bg": "https://images.unsplash.com/photo-1515169067865-5387ec356754?auto=format&fit=crop&w=1350&q=80",
        "songs": ["Levitating - Dua Lipa", "Uptown Funk - Bruno Mars"]
    }
}

# -------------------------
# 스타일 설정
# -------------------------
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('{image_url}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: white;
        }}
        .block-container {{
            background-color: rgba(0, 0, 0, 0.65);
            padding: 2rem;
            border-radius: 10px;
        }}
        h1, h2, h3, h4, h5 {{
            color: #f8f8f8;
        }}
        .css-1cpxqw2 {{
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# 앱 시작
# -------------------------
st.set_page_config(page_title="MBTI + 기분 음악 추천", layout="centered")

# 사용자 입력 받기
mbti = st.selectbox("당신의 MBTI는 무엇인가요?", list(mbti_data.keys()))
mood = st.radio("지금 기분은 어떤가요?", list(mood_data.keys()))

# 배경 이미지 설정
set_background_image(mood_data[mood]["bg"])

# 결과 출력
if mbti and mood:
    info = mbti_data[mbti]
    mood_songs = mood_data[mood]["songs"]

    st.markdown("<h1 style='text-align: center;'>🎧 추천 음악</h1>", unsafe_allow_html=True)
    st.markdown(f"### 🧠 {mbti}형의 성격")
    st.write(info["desc"])

    st.markdown("### 🎼 추천 장르")
    st.write(", ".join(info["genres"]))

    st.markdown("### 🎤 추천 아티스트")
    st.write(", ".join(info["artists"]))

    st.markdown(f"### 🎵 '{mood}' 기분일 때 어울리는 노래")
    for song in mood_songs:
        st.markdown(f"- {song}")
