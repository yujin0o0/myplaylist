# mbti_mood_music_app.py

import streamlit as st
from googleapiclient.discovery import build

# -------------------------
# 유튜브 API 설정
# -------------------------
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"  # 여기 본인의 API 키 입력
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_youtube(query, max_results=2):
    try:
        res = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            maxResults=max_results
        ).execute()
        return [
            {
                "title": item["snippet"]["title"],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}",
                "thumbnail": item["snippet"]["thumbnails"]["medium"]["url"]
            }
            for item in res.get("items", [])
        ]
    except Exception as e:
        st.error(f"유튜브 API 요청 실패: {e}")
        return []

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

mood_data = {
    "행복한": {"keywords": ["happy", "feel good", "cheerful"]},
    "슬픈": {"keywords": ["sad", "emotional", "melancholic"]},
    "차분한": {"keywords": ["calm", "relaxing", "soothing"]},
    "신나는": {"keywords": ["energetic", "hype", "upbeat"]}
}

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
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# Streamlit UI 시작
# -------------------------
st.set_page_config(page_title="MBTI + 기분 노래 추천기", layout="centered")
set_background_image("https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=1350&q=80")

st.markdown("<h1 style='text-align: center; color: white;'>🎧 MBTI + 기분 기반 음악 추천기</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #eeeeee;'>당신의 성격과 현재 기분에 어울리는 노래를 추천해드릴게요!</p>", unsafe_allow_html=True)

# 사용자 입력
mbti = st.selectbox("MBTI를 선택하세요:", list(mbti_music_data.keys()))
mood = st.radio("현재 기분은 어떤가요?", list(mood_data.keys()))

if st.button("🎶 노래 추천받기"):
    # 추천 키워드 생성
    mbti_info = mbti_music_data[mbti]
    mood_keywords = mood_data[mood]["keywords"]
    query = f"{mbti_info['genres'][0]} {mood_keywords[0]} music"

    st.subheader(f"🎼 {mbti} + {mood} 기분에 어울리는 음악")
    st.markdown(f"**추천 장르:** {', '.join(mbti_info['genres'])}")
    st.markdown(f"**추천 아티스트:** {', '.join(mbti_info['artists'])}")

    st.write("---")
    st.subheader("📺 추천 유튜브 영상")
    results = search_youtube(query)

    if results:
        for r in results:
            st.markdown(f"**{r['title']}**")
            st.video(r["url"])
    else:
        st.warning("추천 영상을 불러오지 못했습니다.")

