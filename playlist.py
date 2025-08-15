# mbti_mood_music_no_install.py

import streamlit as st

# -------------------------
# MBTI + 성격/음악 추천 정보
# -------------------------
mbti_data = {
    "INTJ": {"desc": "독창적이고 전략적인 사색가형", "genres": ["영화 음악", "프로그레시브 록"], "artists": ["Hans Zimmer", "Pink Floyd"]},
    "INTP": {"desc": "호기심 많고 논리적인 철학자형", "genres": ["인디", "전자음악"], "artists": ["Tame Impala", "Aphex Twin"]},
    "ENTJ": {"desc": "리더십과 추진력이 강한 지휘관형", "genres": ["팝/록", "클래식"], "artists": ["Queen", "Imagine Dragons"]},
    "ENTP": {"desc": "새로운 아이디어에 열정적인 발명가형", "genres": ["퓨전", "인디"], "artists": ["Gorillaz", "Childish Gambino"]},
    "INFJ": {"desc": "이상주의적이고 직관적인 옹호자형", "genres": ["포크", "클래식"], "artists": ["Bon Iver", "Einaudi"]},
    "INFP": {"desc": "감성적이고 깊은 생각을 지닌 중재자형", "genres": ["인디 팝", "드림 팝"], "artists": ["Lana Del Rey", "Aurora"]},
    "ENFJ": {"desc": "따뜻한 카리스마를 가진 선도자형", "genres": ["팝 발라드", "소울"], "artists": ["Adele", "Sam Smith"]},
    "ENFP": {"desc": "자유롭고 창의적인 활동가형", "genres": ["팝", "EDM"], "artists": ["Dua Lipa", "Avicii"]},
    "ISTJ": {"desc": "신중하고 책임감 있는 관리자형", "genres": ["클래식", "컨트리"], "artists": ["Frank Sinatra", "John Mayer"]},
    "ISFJ": {"desc": "헌신적이고 온화한 수호자형", "genres": ["발라드", "OST"], "artists": ["Ed Sheeran", "Taylor Swift"]},
    "ESTJ": {"desc": "체계적이고 현실적인 경영자형", "genres": ["클래식 록", "팝 락"], "artists": ["Bruce Springsteen", "Coldplay"]},
    "ESFJ": {"desc": "따뜻하고 친절한 사교가형", "genres": ["팝", "댄스 팝"], "artists": ["Bruno Mars", "Ariana Grande"]},
    "ISTP": {"desc": "유연하고 현실적인 장인형", "genres": ["하드 록", "트랩"], "artists": ["Linkin Park", "Travis Scott"]},
    "ISFP": {"desc": "예술적이고 조용한 예술가형", "genres": ["인디", "감성 팝"], "artists": ["Lorde", "Phoebe Bridgers"]},
    "ESTP": {"desc": "모험을 즐기는 활동가형", "genres": ["힙합", "라틴"], "artists": ["Drake", "Bad Bunny"]},
    "ESFP": {"desc": "자유롭고 에너지 넘치는 연예인형", "genres": ["K-pop", "댄스"], "artists": ["BTS", "Katy Perry"]}
}

# -------------------------
# 기분별 배경 이미지 + 추천곡 + 이모지
# -------------------------
mood_data = {
    "행복한": {
        "bg": "https://images.unsplash.com/photo-1498931299472-f7a63a5a1cfa?auto=format&fit=crop&w=1350&q=80",
        "songs": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake"],
        "emoji": "😊"
    },
    "슬픈": {
        "bg": "https://images.unsplash.com/photo-1608889174521-637750df981f?auto=format&fit=crop&w=1350&q=80",
        "songs": ["Someone Like You - Adele", "Fix You - Coldplay"],
        "emoji": "😢"
    },
    "차분한": {
        "bg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1350&q=80",
        "songs": ["Weightless - Marconi Union", "River Flows in You - Yiruma"],
        "emoji": "😌"
    },
    "신나는": {
        "bg": "https://images.unsplash.com/photo-1515169067865-5387ec356754?auto=format&fit=crop&w=1350&q=80",
        "songs": ["Levitating - Dua Lipa", "Uptown Funk - Bruno Mars"],
        "emoji": "🎉"
    }
}

# -------------------------
# 배경 적용 함수
# -------------------------
def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: white;
        }}
        .block-container {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 10px;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #fff;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# 이모지 애니메이션 (간단 버전)
# -------------------------
def show_emoji_rain(emoji: str):
    st.markdown(
        f"""
        <div style='font-size: 40px; text-align: center; animation: fall 3s ease-in-out infinite;'>
            {" ".join([emoji]*20)}
        </div>
        <style>
        @keyframes fall {{
            0% {{ transform: translateY(-100px); opacity: 0; }}
            50% {{ opacity: 1; }}
            100% {{ transform: translateY(100vh); opacity: 0; }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# 앱 시작
# -------------------------
st.set_page_config(page_title="MBTI 기분별 음악 추천기", layout="centered")

st.markdown("<h1 style='text-align: center;'>🎧 MBTI + 기분 음악 추천기</h1>", unsafe_allow_html=True)

# 사용자 입력
mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_data.keys()))
mood = st.radio("현재 기분은 어떤가요?", list(mood_data.keys()))

# 배경 이미지 설정
set_background_image(mood_data[mood]["bg"])
show_emoji_rain(mood_data[mood]["emoji"])

# 추천 결과
st.markdown(f"## 🧠 {mbti}형: {mbti_data[mbti]['desc']}")
st.markdown("### 🎼 추천 장르:")
st.write(", ".join(mbti_data[mbti]["genres"]))

st.markdown("### 🎤 추천 아티스트:")
st.write(", ".join(mbti_data[mbti]["artists"]))

st.markdown(f"### 🎵 '{mood}' 기분일 때 추천곡:")
for song in mood_data[mood]["songs"]:
    st.markdown(f"- {song}")
