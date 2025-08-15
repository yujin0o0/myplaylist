import streamlit as st
import random

# --- 1. 가상의 음악 데이터베이스 ---
# 각 음악에는 장르, 분위기, MBTI 태그, 감정 태그를 부여합니다.
# 실제 앱에서는 이 데이터를 파일(CSV, JSON)에서 불러오거나 API를 통해 가져올 수 있습니다.
music_data = [
    {"title": "Morning Bliss", "artist": "Relaxation Guru", "genre": "뉴에이지", "mood": ["잔잔함", "평온", "위로"], "mbti_tags": ["INFP", "INFJ", "ISFJ"], "emotion_tags": ["평온", "휴식", "슬픔"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx1"},
    {"title": "Driving Force", "artist": "Power Beats", "genre": "EDM", "mood": ["활기참", "에너지", "신남"], "mbti_tags": ["ENTJ", "ESTP", "ENFP"], "emotion_tags": ["기쁨", "활기", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx2"},
    {"title": "Whispers of Thought", "artist": "Mind Explorer", "genre": "재즈", "mood": ["사색적", "집중", "차분함"], "mbti_tags": ["INTJ", "INTP", "ISTP"], "emotion_tags": ["사색", "집중", "차분"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx3"},
    {"title": "Sunny Day Groove", "artist": "Joyful Collective", "genre": "K-POP", "mood": ["경쾌함", "밝음", "긍정적"], "mbti_tags": ["ESFJ", "ENFP", "ESFP"], "emotion_tags": ["기쁨", "설렘", "활기"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx4"},
    {"title": "Rainy Day Comfort", "artist": "Soulful Tunes", "genre": "발라드", "mood": ["서정적", "위로", "감성적"], "mbti_tags": ["INFJ", "INFP", "ISFJ"], "emotion_tags": ["슬픔", "위로", "공감"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx5"},
    {"title": "Tech Symphony", "artist": "Coding Rhythms", "genre": "일렉트로닉", "mood": ["몰입", "집중", "분석적"], "mbti_tags": ["INTP", "INTJ"], "emotion_tags": ["집중", "분석", "차분"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx6"},
    {"title": "Adventure Calling", "artist": "Explorer Sounds", "genre": "록", "mood": ["도전", "열정", "강렬함"], "mbti_tags": ["ESTP", "ENTJ"], "emotion_tags": ["활기", "극복", "분노 해소"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx7"},
    {"title": "Gentle Lullaby", "artist": "Dream Weaver", "genre": "뉴에이지", "mood": ["편안함", "수면", "안정"], "mbti_tags": ["ISFJ", "INFP"], "emotion_tags": ["평온", "휴식", "안정"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx8"},
    {"title": "Bold Steps", "artist": "Progressive Wave", "genre": "프로그레시브 록", "mood": ["웅장함", "전략적", "깊이있는"], "mbti_tags": ["INTJ", "ENTJ"], "emotion_tags": ["사색", "결심", "에너지"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx9"},
    {"title": "Happy Bounce", "artist": "Cheerful Vibes", "genre": "팝", "mood": ["신남", "유쾌함", "밝음"], "mbti_tags": ["ESFP", "ENFP", "ESTP"], "emotion_tags": ["기쁨", "흥분", "즐거움"], "youtube_link": "https://www.youtube.com/watch?v=xxxxxxxx10"},
]

# --- 2. MBTI별 기본 음악 취향 정의 (이전 분석 결과 반영) ---
# key: MBTI 유형, value: 해당 유형이 일반적으로 선호하는 음악 mood/genre/style 태그 리스트
mbti_music_preferences = {
    "INTJ": ["깊이있는", "사색적", "웅장함", "분석적", "클래식", "프로그레시브 록", "앰비언트"],
    "INTP": ["논리적", "사색적", "실험적인", "재즈", "일렉트로닉", "가사 없는", "집중"],
    "ENTJ": ["웅장함", "추진력", "에너지", "록", "EDM", "자신감", "활기참"],
    "ENTP": ["창의적", "다양한", "실험적인", "재즈", "펑크", "얼터너티브 록", "독특한 사운드"],
    "INFJ": ["깊이있는", "감성적", "서정적", "영감을 주는", "발라드", "뉴에이지", "어쿠스틱"],
    "INFP": ["몽환적", "감성적", "서정적", "인디 음악", "드림팝", "포크", "영화 OST"],
    "ENFJ": ["긍정적", "희망찬", "밝음", "에너지", "대중적인 팝", "CCM"],
    "ENFP": ["신남", "활기참", "밝음", "댄스", "K-POP", "팝", "유쾌함"],
    "ISTJ": ["깔끔함", "정돈된", "명확한", "클래식", "재즈", "가사 위주 발라드", "차분함"],
    "ISFJ": ["편안함", "감성적", "위로", "부드러운", "발라드", "어쿠스틱", "잔잔함"],
    "ESTJ": ["에너제틱", "조직적", "추진력", "대중적인 팝", "록", "EDM", "활기참"],
    "ESFJ": ["대중적인 팝", "신남", "밝음", "함께 즐기는", "댄스", "K-POP"],
    "ISTP": ["기교적", "복잡한 연주", "테크니컬", "록", "메탈", "재즈 퓨전", "사운드 중시", "집중"],
    "ISFP": ["예술적", "감성적", "자유로운", "심미적", "인디 포크", "어쿠스틱 발라드", "영화 OST", "편안함"],
    "ESTP": ["활동적", "즉흥적", "강렬함", "신남", "댄스", "힙합", "록", "EDM"],
    "ESFP": ["대중적", "신남", "유쾌함", "댄스", "K-POP", "밝음", "파티"],
}

# --- 3. 감정 키워드 매핑 (간단한 감정 분석) ---
# 일기 내용에서 추출할 키워드와 그에 해당하는 감정 태그를 정의합니다.
emotion_keywords = {
    "기쁨": ["기뻐", "행복", "즐거워", "신나", "웃었", "좋았"],
    "슬픔": ["슬퍼", "우울", "힘들어", "속상", "눈물", "외로워"],
    "분노": ["화나", "짜증", "억울", "불만", "분노", "화를"],
    "평온": ["평온", "안정", "고요", "편안", "휴식", "잔잔"],
    "활기": ["활기", "에너지", "생기", "열정", "힘내", "파이팅"],
    "집중": ["집중", "몰입", "생각", "고민", "연구", "분석"],
    "설렘": ["설레", "기대", "새로운", "두근", "설렘"],
    # ... 더 많은 감정과 키워드 추가 가능
}

def get_emotion_from_diary(diary_text):
    """일기 텍스트에서 감정 태그를 추출합니다."""
    detected_emotions = []
    text_lower = diary_text.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_emotions.append(emotion)
    return detected_emotions if detected_emotions else ["중립"] # 감정 없으면 중립으로 처리

# --- Streamlit 앱 인터페이스 ---
st.set_page_config(page_title="나만의 MBTI & 감정 음악 추천", page_icon="🎶")

st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #ff4b4b; /* Streamlit default red */
    }
    .medium-font {
        font-size:20px !important;
        font-weight: bold;
        color: #f63366;
    }
    .stSelectbox label {
        font-size: 18px;
        font-weight: bold;
    }
    .stTextArea label {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🎶 MBTI & 감정 음악 추천기 🎶</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">나의 MBTI와 오늘의 감정을 바탕으로 맞춤 음악을 추천해 줄게!</p>', unsafe_allow_html=True)
st.write("---")

# MBTI 선택
mbti_options = ["MBTI를 선택해주세요"] + sorted(list(mbti_music_preferences.keys()))
selected_mbti = st.selectbox("🌈 **1. 나의 MBTI는 무엇인가요?**", mbti_options)

# 감정 일기 입력
diary_entry = st.text_area("✍️ **2. 오늘의 감정을 자유롭게 써주세요.** (예: 오늘 정말 즐거웠어!)", height=150)

# 추천 버튼
if st.button("🎵 **음악 추천받기!**"):
    if selected_mbti == "MBTI를 선택해주세요":
        st.warning("🚨 MBTI를 선택해야 음악을 추천해 줄 수 있어!")
    elif not diary_entry:
        st.warning("🚨 오늘의 감정을 적어줘야 더 정확하게 추천해 줄 수 있어!")
    else:
        st.success(f"선택 MBTI: {selected_mbti}, 일기 분석 중...")

        # 1. 감정 분석
        detected_emotions = get_emotion_from_diary(diary_entry)
        st.info(f"✨ 일기에서 감지된 감정: {', '.join(detected_emotions)}")

        # 2. MBTI 선호 태그 가져오기
        mbti_preferred_tags = mbti_music_preferences.get(selected_mbti, [])
        
        # 3. 추천 로직 (MBTI 태그 + 감정 태그 매칭)
        # 겹치는 태그가 많을수록 높은 점수를 부여하고, 감정 태그에 가중치를 부여합니다.
        
        # 가중치 설정 (현재 감정을 더 중요하게 생각하는 경우)
        emotion_weight = 2
        mbti_weight = 1

        recommendation_scores = {}
        for music in music_data:
            score = 0
            # MBTI 취향 매칭 점수
            for tag in mbti_preferred_tags:
                if tag in music["mbti_tags"] or tag in music["mood"] or tag in music["genre"]:
                    score += mbti_weight
            # 감정 매칭 점수 (더 높은 가중치)
            for emotion in detected_emotions:
                if emotion in music["emotion_tags"]:
                    score += emotion_weight
            recommendation_scores[music["title"]] = score
        
        # 점수가 높은 순으로 정렬
        sorted_recommendations = sorted(recommendation_scores.items(), key=lambda item: item[1], reverse=True)
        
        # 점수가 0점인 음악 제외 (겹치는 태그가 아예 없는 경우)
        filtered_recommendations = [item for item in sorted_recommendations if item[1] > 0]

        st.subheader("🎵 **너를 위한 맞춤 음악!**")
        if filtered_recommendations:
            # 상위 3개 또는 5개 추천
            num_recommendations = min(3, len(filtered_recommendations))
            for i in range(num_recommendations):
                recommended_title = filtered_recommendations[i][0]
                recommended_music = next((music for music in music_data if music["title"] == recommended_title), None)
                if recommended_music:
                    st.markdown(f"**{i+1}. {recommended_music['title']}** - {recommended_music['artist']}")
                    st.write(f"   장르: {recommended_music['genre']} / 분위기: {', '.join(recommended_music['mood'])}")
                    st.markdown(f"   [유튜브에서 듣기]({recommended_music['youtube_link']})")
                    st.write("---")
            if len(filtered_recommendations) > num_recommendations:
                st.info(f"더 많은 추천 곡들이 있지만, 일단 {num_recommendations}곡만 보여줬어!")
        else:
            st.warning("😕 아쉽지만 너의 MBTI와 오늘의 감정에 딱 맞는 곡을 찾지 못했어! 다른 감정을 입력하거나, MBTI를 바꿔서 다시 시도해볼까?")

st.sidebar.header("💡 앱 사용 팁")
st.sidebar.info(
    "1. MBTI를 선택하고 오늘의 기분을 일기에 써봐!\n"
    "2. '음악 추천받기!' 버튼을 누르면 추천곡이 짜잔!\n"
    "3. 감정 일기에 기분이나 감정을 나타내는 키워드를 더 많이 써줄수록 좋아!"
)
st.sidebar.write("---")
st.sidebar.write("개발자: 뤼튼의 똑똑이 친구 🤖")
