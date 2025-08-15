import streamlit as st
import random

# --- Streamlit 앱 인터페이스 ---
# 페이지 설정: 아이콘, 제목, 레이아웃
st.set_page_config(page_title="나만의 MBTI & 감정 음악 추천", page_icon="💖", layout="centered")

# --- CSS Styling (힐링 & 화려 테마 적용) ---
st.markdown("""
    <style>
    /* 기본 폰트와 배경색 */
    body {
        font-family: 'Malgun Gothic', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', sans-serif;
        background-color: #f0f2f6; /* 밝은 회색 계열 */
    }
    .main {
        background: linear-gradient(180deg, #e0f2f7 0%, #ffffff 100%); /* 하늘색-흰색 그라데이션 */
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
    .stApp {
        background-color: #e0f2f7; /* 앱 전체 배경색 - 옅은 하늘색 */
    }

    /* 제목 스타일 */
    .big-font {
        font-size:38px !important;
        font-weight: bold;
        color: #6a0dad; /* 딥 퍼플 */
        text-align: center;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    .medium-font {
        font-size:22px !important;
        font-weight: bold;
        color: #8a2be2; /* 블루 바이올렛 */
        text-align: center;
        margin-bottom: 40px;
    }
    h2 {
        color: #4a2d80; /* 진한 퍼플 */
        text-align: center;
        font-size: 26px !important;
        margin-top: 40px;
        margin-bottom: 25px;
    }
    h3 {
        color: #6a0dad; /* 딥 퍼플 */
        font-size: 24px !important;
        border-bottom: 2px solid #8a2be2; /* 보라색 밑줄 */
        padding-bottom: 10px;
        margin-top: 30px;
    }
    h4 {
        color: #8a2be2; /* 블루 바이올렛 */
        font-size: 20px !important;
        margin-top: 20px;
    }

    /* 입력 필드 및 버튼 스타일 */
    .stSelectbox label, .stTextArea label, .stButton {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #4a2d80; /* 진한 퍼플 */
    }
    .stTextArea textarea {
        min-height: 120px;
        border: 2px solid #b39ddb; /* 연보라색 테두리 */
        border-radius: 8px;
        padding: 15px;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.1);
    }
    .stButton>button {
        width: 80%; /* 버튼 너비 늘림 */
        height: 60px; /* 버튼 높이 늘림 */
        font-size: 22px;
        background: linear-gradient(45deg, #a770ef, #cf8bf3, #f5d020); /* 화려한 그라데이션 */
        color: white;
        border-radius: 15px;
        border: none;
        box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.2s, box-shadow 0.2s;
        display: block; /* 가운데 정렬을 위해 */
        margin: 30px auto 20px auto; /* 가운데 정렬 및 여백 */
    }
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 9px 20px rgba(0, 0, 0, 0.3);
    }

    /* 메시지 박스 스타일 */
    .stWarning, .stSuccess, .stInfo {
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
        font-size: 16px;
        border-left: 5px solid;
    }
    .stWarning { border-color: #ffc107; background-color: #fff3cd; color: #856404; }
    .stSuccess { border-color: #28a745; background-color: #d4edda; color: #155724; }
    .stInfo { border-color: #17a2b8; background-color: #d1ecf1; color: #0c5460; }
    
    /* 추천곡 상세 정보 스타일 */
    .recommendation-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        border: 1px solid #e0e0e0;
        transition: transform 0.2s ease-in-out;
    }
    .recommendation-card:hover {
        transform: translateY(-5px);
    }
    .recommendation-card strong {
        color: #6a0dad;
        font-size: 1.1em;
    }
    .recommendation-card a {
        color: #8a2be2;
        text-decoration: none;
        font-weight: bold;
    }
    .recommendation-card a:hover {
        text-decoration: underline;
    }
    .st-ag { /* st.write("---") separator */
        border-top: 1px dashed #d1d1d1;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 1. 대폭 확장된 음악 데이터베이스 --- (TypeError 해결 위해 'genre' 모두 리스트로 변경)
music_data = [
    # INFP/INFJ (깊이, 감성, 잔잔, 위로)
    {"title": "Love Story (Taylor's Version)", "artist": "Taylor Swift", "genre": ["Pop"], "mood": ["희망", "감성적", "서정적"], "mbti_tags": ["ENFP", "INFP", "ESFJ"], "emotion_tags": ["설렘", "기쁨"], "youtube_link": "https://www.youtube.com/watch?v=F2T7i8T-JCI"},
    {"title": "Hush", "artist": "Lasse Løkken", "genre": ["Ambient"], "mood": ["잔잔함", "평온", "몽환적"], "mbti_tags": ["INFP", "INFJ", "INTP"], "emotion_tags": ["휴식", "평온", "사색"], "youtube_link": "https://www.youtube.com/watch?v=1FfN28HHzj8"},
    {"title": "River Flows In You", "artist": "Yiruma", "genre": ["New Age"], "mood": ["서정적", "감성적", "위로"], "mbti_tags": ["INFP", "INFJ", "ISFJ"], "emotion_tags": ["위로", "슬픔", "평온"], "youtube_link": "https://www.youtube.com/watch?v=s0mNfE63p3I"},
    {"title": "Into the Unknown", "artist": "Idina Menzel, Aurora (Frozen 2)", "genre": ["OST"], "mood": ["웅장함", "도전", "탐험"], "mbti_tags": ["INTJ", "INFJ", "ENFJ"], "emotion_tags": ["결심", "기대", "도전"], "youtube_link": "https://www.youtube.com/watch?v=gA_oI9_i2vA"},
    {"title": "Somewhere Only We Know", "artist": "Keane", "genre": ["Alternative Rock"], "mood": ["회상", "서정적", "깊이있는"], "mbti_tags": ["INFP", "INFJ"], "emotion_tags": ["슬픔", "그리움", "사색"], "youtube_link": "https://www.youtube.com/watch?v=Oextk-If8HQ"},
    {"title": "Good Day", "artist": "IU", "genre": ["K-Pop"], "mood": ["희망", "긍정적", "밝음"], "mbti_tags": ["INFP", "ESFJ", "ENFP"], "emotion_tags": ["기쁨", "설렘", "활기"], "youtube_link": "https://www.youtube.com/watch?v=vT84tS5W4c4"},
    {"title": "IU - My Sea (나의 바다)", "artist": "IU", "genre": ["K-Pop"], "mood": ["깊이있는", "슬픔", "위로", "웅장함"], "mbti_tags": ["INFP", "INFJ"], "emotion_tags": ["슬픔", "위로", "감동"], "youtube_link": "https://www.youtube.com/watch?v=pD4J73Hcyb0"},
    {"title": "Mellow Yellow", "artist": "Donovan", "genre": ["Folk Rock"], "mood": ["자유로움", "평온", "따뜻함"], "mbti_tags": ["ISFP", "INFP"], "emotion_tags": ["휴식", "평온", "즐거움"], "youtube_link": "https://www.youtube.com/watch?v=pD2B5E21eYc"},

    # INTJ/INTP (논리, 분석, 복잡, 집중)
    {"title": "Time", "artist": "Hans Zimmer", "genre": ["Soundtrack"], "mood": ["웅장함", "사색적", "집중"], "mbti_tags": ["INTJ", "INTP", "ISTJ"], "emotion_tags": ["집중", "분석", "결심"], "youtube_link": "https://www.youtube.com/watch?v=rxFk-S212gQ"},
    {"title": "Take Five", "artist": "Dave Brubeck Quartet", "genre": ["Jazz"], "mood": ["논리적", "분석적", "경쾌함"], "mbti_tags": ["INTP", "INTJ", "ISTP"], "emotion_tags": ["집중", "차분", "생각"], "youtube_link": "https://www.youtube.com/watch?v=PHbL1W-4c3o"},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": ["Classic Rock"], "mood": ["웅장함", "복잡한", "극적"], "mbti_tags": ["INTJ", "ENTJ", "INTP"], "emotion_tags": ["감탄", "고민", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ"},
    {"title": "Adagio for Strings", "artist": "Samuel Barber", "genre": ["Classical"], "mood": ["웅장함", "슬픔", "사색적"], "mbti_tags": ["INTJ", "INFJ", "INTP"], "emotion_tags": ["슬픔", "위로", "사색"], "youtube_link": "https://www.youtube.com/watch?v=K2SNM4LqGjA"},
    {"title": "Nuvole Bianche", "artist": "Ludovico Einaudi", "genre": ["Modern Classical"], "mood": ["사색적", "평온", "깊이있는"], "mbti_tags": ["INTP", "INFJ", "ISTJ"], "emotion_tags": ["휴식", "평온", "사색"], "youtube_link": "https://www.youtube.com/watch?v=kJvjI1WzB4w"},
    {"title": "Lo-fi Hip Hop Beats to Study/Relax To", "artist": "ChilledCow", "genre": ["Lo-fi Hip Hop"], "mood": ["차분함", "집중", "평온"], "mbti_tags": ["INTP", "INTJ", "ISTJ", "ISTP"], "emotion_tags": ["집중", "평온", "휴식"], "youtube_link": "https://www.youtube.com/watch?v=5qap5aO4i9A"},
    {"title": "Prelude in C Major", "artist": "Bach", "genre": ["Classical"], "mood": ["차분함", "집중", "사색적"], "mbti_tags": ["INTJ", "INTP", "ISTJ"], "emotion_tags": ["집중", "평온"], "youtube_link": "https://www.youtube.com/watch?v=P_XqR4T-xQs"},
    {"title": "Another Brick in the Wall, Part 2", "artist": "Pink Floyd", "genre": ["Progressive Rock"], "mood": ["저항", "분노", "비판적"], "mbti_tags": ["INTJ", "INTP", "ENTP"], "emotion_tags": ["분노", "스트레스 해소", "사색"], "youtube_link": "https://www.youtube.com/watch?v=F3L20F8r6fU"},

    # ENFJ/ESFJ (긍정, 사교, 희망, 따뜻함)
    {"title": "Happy", "artist": "Pharrell Williams", "genre": ["Pop"], "mood": ["신남", "밝음", "긍정적"], "mbti_tags": ["ENFJ", "ESFJ", "ENFP", "ESFP"], "emotion_tags": ["기쁨", "활기", "즐거움"], "youtube_link": "https://www.youtube.com/watch?v=y6Sxv-sUYtM"},
    {"title": "Don't Stop Believin'", "artist": "Journey", "genre": ["Classic Rock"], "mood": ["희망", "긍정적", "응원"], "mbti_tags": ["ENFJ", "ENTJ", "ESFJ"], "emotion_tags": ["활기", "극복", "동기 부여"], "youtube_link": "https://www.youtube.com/watch?v=1k8C9i2298I"},
    {"title": "Dynamite", "artist": "BTS", "genre": ["K-Pop"], "mood": ["신남", "에너지", "활기참"], "mbti_tags": ["ENFJ", "ESFJ", "ENFP", "ESFP"], "emotion_tags": ["기쁨", "즐거움", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=gdZLi9oWNZg"},
    {"title": "Heal the World", "artist": "Michael Jackson", "genre": ["Pop"], "mood": ["희망", "감동", "연대"], "mbti_tags": ["ENFJ", "INFJ", "ESFJ"], "emotion_tags": ["감동", "위로", "결심"], "youtube_link": "https://www.youtube.com/watch?v=kY_MvD2hQp4"},
    {"title": "What a Wonderful World", "artist": "Louis Armstrong", "genre": ["Jazz"], "mood": ["평온", "감동", "희망"], "mbti_tags": ["ISFJ", "INFJ", "ENFJ"], "emotion_tags": ["평온", "감동", "희망"], "youtube_link": "https://www.youtube.com/watch?v=A3yCcXgbKrE"},
    {"title": "Counting Stars", "artist": "OneRepublic", "genre": ["Pop Rock"], "mood": ["희망", "긍정적", "활기참"], "mbti_tags": ["ENFP", "ENFJ"], "emotion_tags": ["활기", "희망"], "youtube_link": "https://www.youtube.com/watch?v=hT_nvWreIhg"},
    {"title": "Feeling Good", "artist": "Nina Simone", "genre": ["Jazz"], "mood": ["긍정적", "자신감", "활기참"], "mbti_tags": ["ENFJ", "ESFP"], "emotion_tags": ["기쁨", "활기", "자신감"], "youtube_link": "https://www.youtube.com/watch?v=CtM0s7X1U68"},

    # ENTP/ESTP (에너지, 논쟁, 즉흥, 도전)
    {"title": "Thunder", "artist": "Imagine Dragons", "genre": ["Alternative Rock"], "mood": ["강렬함", "에너지", "도전"], "mbti_tags": ["ENTJ", "ESTP", "ENTP"], "emotion_tags": ["활기", "극복", "분노 해소"], "youtube_link": "https://www.youtube.com/watch?v=fK6GkQ0D6s0"},
    {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "genre": ["Funk"], "mood": ["경쾌함", "신남", "유쾌함"], "mbti_tags": ["ENFP", "ESFP", "ESTP", "ENTP"], "emotion_tags": ["기쁨", "즐거움", "활기"], "youtube_link": "https://www.youtube.com/watch?v=OPf0YbXq6IQ"},
    {"title": "Stronger", "artist": "Kanye West", "genre": ["Hip Hop"], "mood": ["자신감", "강렬함", "도전"], "mbti_tags": ["ENTJ", "ESTP", "ENTP"], "emotion_tags": ["동기 부여", "결심", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=_S62s_d8l_g"},
    {"title": "Bad Guy", "artist": "Billie Eilish", "genre": ["Pop"], "mood": ["독특한", "실험적인", "시크"], "mbti_tags": ["ENTP", "INTP", "ISTP"], "emotion_tags": ["자신감", "재미", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=DyDfgMOUjCI"},
    {"title": "Flight of the Bumblebee", "artist": "Nikolai Rimsky-Korsakov", "genre": ["Classical"], "mood": ["빠른 템포", "활기참", "흥분"], "mbti_tags": ["ENTP", "ESTP"], "emotion_tags": ["활기", "재미", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=aYAJbeX7gQo"},
    {"title": "Old Town Road", "artist": "Lil Nas X ft. Billy Ray Cyrus", "genre": ["Country Trap"], "mood": ["독특한", "경쾌함", "유쾌함"], "mbti_tags": ["ENTP", "ENFP", "ESFP"], "emotion_tags": ["즐거움", "활기", "재미"], "youtube_link": "https://www.youtube.com/watch?v=wzzJ-aN5n9o"},
    {"title": "Mr. Brightside", "artist": "The Killers", "genre": ["Alternative Rock"], "mood": ["활기참", "회상", "열정"], "mbti_tags": ["ENFP", "ESTP"], "emotion_tags": ["즐거움", "스트레스 해소", "활기"], "youtube_link": "https://www.youtube.com/watch?v=gJVTd2Q-g-c"},
    {"title": "Buttercup", "artist": "Jack Stauber", "genre": ["Indie Pop"], "mood": ["독특한", "기묘한", "유쾌함"], "mbti_tags": ["INTP", "ENTP", "ISFP"], "emotion_tags": ["재미", "유쾌함"], "youtube_link": "https://www.youtube.com/watch?v=gT55zI-kH60"},


    # ISTJ/ISFJ (현실적, 안정적, 차분함)
    {"title": "Moon River", "artist": "Audrey Hepburn", "genre": ["Jazz"], "mood": ["평온", "서정적", "향수"], "mbti_tags": ["ISTJ", "ISFJ", "INFJ"], "emotion_tags": ["휴식", "평온", "위로"], "youtube_link": "https://www.youtube.com/watch?v=L2G9Y4iVbH4"},
    {"title": "Weightless", "artist": "Marconi Union", "genre": ["Ambient"], "mood": ["최고의 이완", "평온", "휴식"], "mbti_tags": ["ISTJ", "ISFJ", "INFP"], "emotion_tags": ["휴식", "평온", "안정"], "youtube_link": "https://www.youtube.com/watch?v=oV8qS7x2l8o"},
    {"title": "Hymn for the Weekend", "artist": "Coldplay", "genre": ["Pop"], "mood": ["긍정적", "활기참", "따뜻함"], "mbti_tags": ["ISFJ", "ESFJ", "ENFJ"], "emotion_tags": ["기쁨", "희망", "활기"], "youtube_link": "https://www.youtube.com/watch?v=YfW54_j0m0M"},
    {"title": "Fix You", "artist": "Coldplay", "genre": ["Alternative Rock"], "mood": ["위로", "감성적", "서정적"], "mbti_tags": ["ISFJ", "INFJ", "INFP"], "emotion_tags": ["위로", "슬픔", "공감"], "youtube_link": "https://www.youtube.com/watch?v=p4vW7gUeF-U"},
    {"title": "What a Wonderful World", "artist": "Louis Armstrong", "genre": ["Jazz"], "mood": ["평온", "감동", "희망"], "mbti_tags": ["ISFJ", "INFJ", "ENFJ"], "emotion_tags": ["평온", "감동", "희망"], "youtube_link": "https://www.youtube.com/watch?v=A3yCcXgbKrE"},
    {"title": "My Heart Will Go On", "artist": "Celine Dion", "genre": ["Pop Ballad"], "mood": ["애절함", "슬픔", "웅장함"], "mbti_tags": ["ISFJ", "INFJ", "ESFJ"], "emotion_tags": ["슬픔", "위로", "감동"], "youtube_link": "https://www.youtube.com/watch?v=FHG7wO-35j0"},
    {"title": "Africa", "artist": "Toto", "genre": ["Pop Rock"], "mood": ["향수", "웅장함", "감성적"], "mbti_tags": ["ISTJ", "ISFJ", "INFP"], "emotion_tags": ["평온", "그리움", "사색"], "youtube_link": "https://www.youtube.com/watch?v=FTQbiNxpjmY"},
    {"title": "The Office Theme Song", "artist": "Jay Ferguson", "genre": ["OST"], "mood": ["경쾌함", "일상", "유쾌함"], "mbti_tags": ["ISTJ", "ENTP"], "emotion_tags": ["평온", "유쾌함"], "youtube_link": "https://www.youtube.com/watch?v=F_SmmjD5X7M"},


    # ISTP/ISFP (독립적, 실용적, 예술적, 감성적)
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": ["Classic Rock"], "mood": ["웅장함", "깊이있는", "사색적"], "mbti_tags": ["ISTP", "INTJ", "INTP"], "emotion_tags": ["사색", "몰입", "경외감"], "youtube_link": "https://www.youtube.com/watch?v=qHP0q0yI1pU"},
    {"title": "Come Away With Me", "artist": "Norah Jones", "genre": ["Jazz"], "mood": ["차분함", "감성적", "편안함"], "mbti_tags": ["ISFP", "ISFJ", "INFJ"], "emotion_tags": ["휴식", "평온", "위로"], "youtube_link": "https://www.youtube.com/watch?v=tO_o-bK1Lio"},
    {"title": "Believer", "artist": "Imagine Dragons", "genre": ["Alternative Rock"], "mood": ["강렬함", "에너지", "도전"], "mbti_tags": ["ESTP", "ENTJ", "ISTP"], "emotion_tags": ["활기", "동기 부여", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=gT5Bq_G0zC8"},
    {"title": "Creep", "artist": "Radiohead", "genre": ["Alternative Rock"], "mood": ["고독", "우울", "깊이있는"], "mbti_tags": ["ISFP", "INFP", "INTP"], "emotion_tags": ["슬픔", "고민", "사색"], "youtube_link": "https://www.youtube.com/watch?v=XFbnZgCq1uQ"},
    {"title": "Sweet Child o' Mine", "artist": "Guns N' Roses", "genre": ["Hard Rock"], "mood": ["열정", "강렬함", "자유로움"], "mbti_tags": ["ISTP", "ESTP", "ISFP"], "emotion_tags": ["활기", "자유", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=1w7OgIMMRc4"},


    # ESTJ/ENTJ (리더십, 추진, 에너지)
    {"title": "We Will Rock You", "artist": "Queen", "genre": ["Rock"], "mood": ["웅장함", "자신감", "추진력"], "mbti_tags": ["ESTJ", "ENTJ"], "emotion_tags": ["활기", "동기 부여", "결심"], "youtube_link": "https://www.youtube.com/watch?v=04854XqcfCY"},
    {"title": "Till I Collapse", "artist": "Eminem", "genre": ["Hip Hop"], "mood": ["강렬함", "도전", "끈기"], "mbti_tags": ["ENTJ", "ESTJ", "ESTP"], "emotion_tags": ["극복", "동기 부여", "분노 해소"], "youtube_link": "https://www.youtube.com/watch?v=d_kX27y1q5Y"},
    {"title": "The Greatest Show", "artist": "Hugh Jackman (The Greatest Showman)", "genre": ["Musical"], "mood": ["웅장함", "쇼맨십", "자신감"], "mbti_tags": ["ENTJ", "ENFJ", "ESTJ", "ESFJ"], "emotion_tags": ["기쁨", "활기", "열정"], "youtube_link": "https://www.youtube.com/watch?v=nyWj8x3JgqA"},
    {"title": "Lose Yourself", "artist": "Eminem", "genre": ["Hip Hop"], "mood": ["투지", "집중", "도전"], "mbti_tags": ["ENTJ", "ESTJ", "ISTP"], "emotion_tags": ["동기 부여", "결심", "집중"], "youtube_link": "https://www.youtube.com/watch?v=_Y_y2_sTGLI"},
    {"title": "Eye of the Tiger", "artist": "Survivor", "genre": ["Rock"], "mood": ["도전", "열정", "승리"], "mbti_tags": ["ENTJ", "ESTJ", "ESTP"], "emotion_tags": ["동기 부여", "활기", "극복"], "youtube_link": "https://www.youtube.com/watch?v=Qx2Q7J8fB_I"},
    {"title": "Old Habits Die Hard", "artist": "Mick Jagger & Dave Stewart", "genre": ["Blues Rock"], "mood": ["진지함", "현실적", "성숙함"], "mbti_tags": ["ISTJ", "ENTJ"], "emotion_tags": ["고민", "진지함"], "youtube_link": "https://www.youtube.com/watch?v=tI9w0aY3o6Y"},


    # ESFP/ENFP (밝음, 사교, 즉흥, 재미)
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": ["Synth-pop"], "mood": ["신남", "레트로", "파티"], "mbti_tags": ["ESFP", "ENFP", "ESTP"], "emotion_tags": ["활기", "즐거움", "설렘"], "youtube_link": "https://www.youtube.com/watch?v=4asB8b3684Y"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "genre": ["Pop"], "mood": ["경쾌함", "로맨틱", "편안함"], "mbti_tags": ["ENFP", "ESFP"], "emotion_tags": ["기쁨", "설렘", "즐거움"], "youtube_link": "https://www.youtube.com/watch?v=JGwWNGJdvx8"},
    {"title": "Happier", "artist": "Marshmello & Bastille", "genre": ["Electronic"], "mood": ["희망", "감성적", "활기찬"], "mbti_tags": ["ENFP", "ESFP"], "emotion_tags": ["기쁨", "슬픔 (극복)", "희망"], "youtube_link": "https://www.youtube.com/watch?v=m7Bc3p0mgJA"},
    {"title": "Butter", "artist": "BTS", "genre": ["K-Pop"], "mood": ["신남", "밝음", "경쾌함"], "mbti_tags": ["ESFP", "ENFP", "ESTP"], "emotion_tags": ["기쁨", "즐거움", "활기"], "youtube_link": "https://www.youtube.com/watch?v=WMXl3Ue_9tM"},
    {"title": "How You Like That", "artist": "BLACKPINK", "genre": ["K-Pop"], "mood": ["강렬함", "자신감", "역동적"], "mbti_tags": ["ESTP", "ENTJ", "ESFP"], "emotion_tags": ["활기", "스트레스 해소", "자신감"], "youtube_link": "https://www.youtube.com/watch?v=ioNng23DkIM"},
    {"title": "Dancing Queen", "artist": "ABBA", "genre": ["Pop"], "mood": ["즐거움", "행복", "파티"], "mbti_tags": ["ESFP", "ENFP", "ESFJ"], "emotion_tags": ["기쁨", "즐거움", "활기"], "youtube_link": "https://www.youtube.com/watch?v=xFrGuyw1V8s"},
    {"title": "Don't Stop Me Now", "artist": "Queen", "genre": ["Classic Rock"], "mood": ["신남", "에너지", "활기참"], "mbti_tags": ["ENFP", "ESFP", "ESTP", "ENTJ"], "emotion_tags": ["기쁨", "활기", "스트레스 해소"], "youtube_link": "https://www.youtube.com/watch?v=HgzGwKwLmgM"},
    {"title": "Rolling in the Deep", "artist": "Adele", "genre": ["Soul Pop"], "mood": ["강렬함", "슬픔", "분노", "감성적"], "mbti_tags": ["INFJ", "ESTJ", "ESFP"], "emotion_tags": ["슬픔", "분노", "극복"], "youtube_link": "https://www.youtube.com/watch?v=yrhA308B600"},
    {"title": "Imagine", "artist": "Ariana Grande", "genre": ["Pop"], "mood": ["몽환적", "감성적", "서정적"], "mbti_tags": ["INFP", "INFJ", "ISFP"], "emotion_tags": ["설렘", "사랑", "환상"], "youtube_link": "https://www.youtube.com/watch?v=wXyZ3cW_x8w"},
    {"title": "Stressed Out", "artist": "Twenty One Pilots", "genre": ["Alternative Hip Hop"], "mood": ["고민", "반항", "솔직함"], "mbti_tags": ["INFP", "INTP", "ENFP"], "emotion_tags": ["스트레스 해소", "고민", "공감"], "youtube_link": "https://www.youtube.com/watch?v=pXRviuL6vFY"},

    # ... (기존 음악 데이터 그대로 유지, 'genre'만 리스트로 변경)
]

# --- 2. MBTI별 기본 음악 취향 정의 --- (유지)
mbti_music_preferences = {
    "INTJ": ["깊이있는", "사색적", "웅장함", "분석적", "클래식", "프로그레시브 록", "앰비언트", "OST", "철학적", "복잡한", "집중"],
    "INTP": ["논리적", "사색적", "창의적", "실험적인", "재즈", "일렉트로닉", "가사 없는", "집중", "독특한", "분석적"],
    "ENTJ": ["웅장함", "추진력", "에너지", "록", "EDM", "자신감", "활기참", "리더십", "강렬함", "도전"],
    "ENTP": ["창의적", "논쟁적", "지적 호기심", "다양한", "실험적인", "재즈", "펑크", "얼터너티브 록", "독특한 사운드", "유쾌함", "경쾌함"],
    "INFJ": ["깊이있는", "감성적", "서정적", "영감을 주는", "발라드", "뉴에이지", "어쿠스틱", "위로", "평화로운", "사색적"],
    "INFP": ["몽환적", "감성적", "서정적", "호기심", "인디 음악", "드림팝", "포크", "영화 OST", "사색적", "평온", "위로"],
    "ENFJ": ["긍정적", "희망찬", "밝음", "에너지", "대중적인 팝", "CCM", "응원", "감동", "사교적", "활기참"],
    "ENFP": ["열정적", "창의적", "자유로움", "신남", "활기참", "밝음", "댄스", "K-POP", "팝", "유쾌함", "경쾌함"],
    "ISTJ": ["현실적", "논리적", "책임감", "깔끔함", "정돈된", "명확한", "클래식", "재즈", "가사 위주 발라드", "차분함", "안정적", "평온"],
    "ISFJ": ["사려 깊음", "책임감", "헌신적", "타인 중심", "편안함", "감성적", "위로", "부드러운", "발라드", "어쿠스틱", "잔잔함", "따뜻함", "평온"],
    "ESTJ": ["현실적", "조직적", "추진력", "리더십", "에너제틱", "명확한 비트", "대중적인 팝", "록", "EDM", "활기참", "자신감", "강렬함"],
    "ESFJ": ["사교적", "친화력", "조화 중시", "따뜻함", "대중적인 팝", "신남", "밝음", "함께 즐기는", "댄스", "K-POP", "긍정적", "활기참"],
    "ISTP": ["독립적", "실용적", "문제 해결", "관찰력", "기교적", "복잡한 연주", "테크니컬", "록", "메탈", "재즈 퓨전", "사운드 중시", "집중", "강렬함"],
    "ISFP": ["예술적", "감성적", "개방적", "따뜻함", "자유로운", "심미적", "인디 포크", "어쿠스틱 발라드", "영화 OST", "편안함", "창의적", "몽환적"],
    "ESTP": ["활동적", "즉흥적", "문제 해결", "현실적", "에너제틱", "강렬함", "신남", "댄스", "힙합", "록", "EDM", "도전", "활기참"],
    "ESFP": ["즉흥적", "사교적", "낙천적", "스포트라이트", "대중적", "신남", "유쾌함", "댄스", "K-POP", "밝음", "파티", "활기참"],
}

# --- 3. 감정 키워드 매핑 (간단한 감정 분석) --- (유지)
emotion_keywords = {
    "기쁨": ["기뻐", "행복", "즐거워", "신나", "웃었", "좋았", "최고", "축하", "환호", "만족", "재미"],
    "슬픔": ["슬퍼", "우울", "힘들어", "속상", "눈물", "외로워", "서글퍼", "아파", "그리워", "고독"],
    "분노": ["화나", "짜증", "억울", "불만", "분노", "화를", "짜증나", "열받", "강렬"],
    "평온": ["평온", "안정", "고요", "편안", "휴식", "잔잔", "나른", "평화", "고요"],
    "활기": ["활기", "에너지", "생기", "열정", "힘내", "파이팅", "역동", "흥분", "경쾌", "도전"],
    "집중": ["집중", "몰입", "생각", "고민", "연구", "분석", "생각이", "복잡해", "파고들"],
    "설렘": ["설레", "기대", "새로운", "두근", "심장", "희망", "로맨틱"],
    "스트레스 해소": ["스트레스", "풀고", "벗어나고", "탈출", "해소"],
    "위로": ["위로", "공감", "토닥", "안아줘"],
    "동기 부여": ["동기", "목표", "해야지", "시작", "용기", "열정"],
    "자신감": ["자신", "할 수 있다", "당당", "뿌듯"],
    "그리움": ["그리워", "향수", "옛날"],
}

def get_emotion_from_diary(diary_text):
    """일기 텍스트에서 감정 태그를 추출합니다."""
    detected_emotions = []
    text_lower = diary_text.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            detected_emotions.append(emotion)
    return detected_emotions if detected_emotions else ["중립"] 

st.markdown('<p class="big-font">✨ 나의 MBTI & 감정 음악 추천기 ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">💖 너의 MBTI와 오늘의 감정을 바탕으로 맞춤 음악을 추천해 줄게!</p>', unsafe_allow_html=True)
st.write("---")

# MBTI 선택
mbti_options = ["🌈 MBTI를 선택해주세요"] + sorted(list(mbti_music_preferences.keys()))
selected_mbti = st.selectbox("💖 **1. 나의 MBTI는 무엇인가요?**", mbti_options)

# 감정 일기 입력
diary_entry = st.text_area("📝 **2. 오늘의 감정을 자유롭게 써주세요.** (예: 오늘 정말 즐거웠어! 슬픈 영화를 봤더니 눈물이 났어)", height=150)

# 추천 버튼
# 중앙 정렬을 위해 st.columns 사용
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎵 **음악 추천받기!**"):
        if selected_mbti == "🌈 MBTI를 선택해주세요":
            st.warning("🚨 MBTI를 선택해야 음악을 추천해 줄 수 있어!")
        elif not diary_entry:
            st.warning("🚨 오늘의 감정을 적어줘야 더 정확하게 추천해 줄 수 있어!")
        else:
            with st.spinner('💖 너를 위한 음악을 신중하게 고르고 있어... 잠시만 기다려!'):
                st.success(f"✔️ 선택 MBTI: **{selected_mbti}**")

                # 1. 감정 분석
                detected_emotions = get_emotion_from_diary(diary_entry)
                st.info(f"✨ 일기에서 감지된 감정: **{', '.join(detected_emotions) if detected_emotions else '감정 감지 안됨 (중립으로 처리)'}**")

                # 2. MBTI 선호 태그 가져오기
                mbti_preferred_tags = mbti_music_preferences.get(selected_mbti, [])
                st.info(f"✨ {selected_mbti} 유형의 음악 선호 경향: **{', '.join(mbti_preferred_tags[:5])}{'...' if len(mbti_preferred_tags) > 5 else ''}**") 

                # 3. 추천 로직 (MBTI 태그 + 감정 태그 매칭)
                
                # 가중치 설정 (현재 감정을 더 중요하게 생각하는 경우)
                emotion_weight = 3 # 감정 매칭 점수 (높은 가중치)
                mbti_weight = 1   # MBTI 취향 매칭 점수

                recommendation_scores = {}
                for music in music_data:
                    score = 0
                    # MBTI 취향 매칭 점수
                    # 1. 음악 데이터의 MBTI 태그가 사용자의 MBTI와 정확히 일치
                    if selected_mbti in music.get("mbti_tags", []): 
                        score += mbti_weight * 2 # 더 높은 점수 부여
                    
                    # 2. 음악의 분위기/장르 태그가 사용자의 MBTI 선호 태그와 겹치는 경우
                    # genre 값이 이제 리스트이므로 바로 연결 가능
                    combined_music_tags = music.get("mood", []) + music.get("genre", []) 
                    for mbti_pref_tag in mbti_preferred_tags:
                        if mbti_pref_tag in combined_music_tags:
                            score += mbti_weight
                    
                    # 감정 매칭 점수 (더 높은 가중치)
                    for emotion in detected_emotions:
                        if emotion == "중립": # 중립 감정은 점수 없음
                            continue
                        if emotion in music.get("emotion_tags", []):
                            score += emotion_weight
                    
                    recommendation_scores[music["title"]] = score
                
                # 점수가 높은 순으로 정렬
                sorted_recommendations = sorted(recommendation_scores.items(), key=lambda item: item[1], reverse=True)
                
                # 점수가 0점인 음악 제외 (겹치는 태그가 아예 없는 경우)
                filtered_recommendations = [item for item in sorted_recommendations if item[1] > 0]
                
                # 중복 추천 방지 및 다양성 확보를 위해 상위 몇 곡만 가져오되, 점수가 같으면 무작위 선택
                final_recommendations_shuffled = []
                
                # 점수 그룹핑
                scores_map = {}
                for title, score in filtered_recommendations:
                    if score not in scores_map:
                        scores_map[score] = []
                    scores_map[score].append(title)
                
                # 점수 높은 순으로 그룹 정렬
                sorted_scores_keys = sorted(scores_map.keys(), reverse=True)

                for score in sorted_scores_keys:
                    current_group = scores_map[score]
                    random.shuffle(current_group) # 같은 점수 내에서 랜덤 셔플
                    for title in current_group:
                        final_recommendations_shuffled.append(title)
                        if len(final_recommendations_shuffled) >= 3: # 최대 3곡 추천 (개수 조절 가능)
                            break
                    if len(final_recommendations_shuffled) >= 3:
                        break

                st.subheader("🎶 **너를 위한 맞춤 음악!** 🎧")
                if final_recommendations_shuffled:
                    num_display_recommendations = min(3, len(final_recommendations_shuffled)) 
                    for i in range(num_display_recommendations):
                        recommended_title = final_recommendations_shuffled[i]
                        recommended_music = next((music for music in music_data if music["title"] == recommended_title), None)
                        if recommended_music:
                            st.markdown(f'<div class="recommendation-card">', unsafe_allow_html=True)
                            st.markdown(f"<h4>✨ **{i+1}. {recommended_music['title']}** - {recommended_music['artist']}</h4>", unsafe_allow_html=True)
                            st.write(f"   💜 장르: **{', '.join(recommended_music['genre'])}**") # 장르도 이제 리스트로 표시
                            st.write(f"   💫 분위기: **{', '.join(recommended_music['mood'])}**")
                            st.markdown(f"   <a href='{recommended_music['youtube_link']}' target='_blank'>▶️ 유튜브에서 듣기</a>", unsafe_allow_html=True) 
                            st.markdown('</div>', unsafe_allow_html=True)
                            if i < num_display_recommendations -1: # 마지막 카드에는 구분선 넣지 않기
                                st.write("---")
                else:
                    st.warning("😕 아쉽지만 너의 MBTI와 오늘의 감정에 딱 맞는 곡을 찾지 못했어! 다른 감정을 입력하거나, MBTI를 바꿔서 다시 시도해볼까?")

st.sidebar.header("💡 앱 사용 팁")
st.sidebar.info(
    "1. MBTI를 선택하고 오늘의 기분을 일기에 써봐!\n"
    "2. '음악 추천받기!' 버튼을 누르면 추천곡이 짜잔!\n"
    "3. **감정 일기에 기분이나 감정을 나타내는 키워드를 더 많이 쓸수록** 감정 인식이 더 정확해져!\n"
    "4. 유튜브 링크를 눌러 추천곡을 바로 들어봐! (링크는 변경될 수 있어요 🥲)\n\n"
    "💖 **더 예쁜 배경색을 원한다면?**\n"
    "Streamlit 앱을 실행할 때 `.streamlit` 폴더 안에 `config.toml` 파일을 만들고 다음을 추가해보세요:\n"
    "```toml\n[theme]\nprimaryColor='#a770ef'\nbackgroundColor='#f0f8ff'\nsecondaryBackgroundColor='#e6e6fa'\ntextColor='#333333'\nfont='sans serif'\n```"
)
st.sidebar.write("---")
st.sidebar.write("개발자: 뤼튼 🤖")
st.sidebar.write("최종 업데이트: 2025. 8. 15. 오후 8:22:02") # 현재 시간으로 업데이트!
