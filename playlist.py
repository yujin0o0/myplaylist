import streamlit as st
import random
import time 

# --- Streamlit 앱 인터페이스 설정 ---
st.set_page_config(page_title="나만의 MBTI & 감정 음악 추천기", page_icon="🌟", layout="centered")

# --- CSS Styling (화려하고 힐링되는 마법 테마 적용!) ---
st.markdown("""
    <style>
    /* 웹폰트 적용 (옵션, 로딩 속도 고려) */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700&family=Pacifico&display=swap');
    
    /* 기본 폰트와 배경색 */
    html, body {
        font-family: 'Noto Sans KR', sans-serif; /* 한글 폰트 적용 */
        background-color: #f0e6fa; /* 연한 라벤더 배경 */
    }
    .main {
        background: linear-gradient(180deg, #e6e6fa 0%, #ffffff 100%); /* 라벤더-흰색 그라데이션 */
        border-radius: 25px; /* 모서리 더 둥글게 */
        padding: 40px; /* 패딩 늘림 */
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15); /* 그림자 더 선명하게 */
        animation: fadeIn 1s ease-out; /* 페이지 로드 시 페이드인 */
    }
    .stApp {
        background-color: #f0e6fa; /* 앱 전체 배경색 - 옅은 라벤더 */
    }

    /* 제목 스타일 */
    .big-font {
        font-family: 'Pacifico', cursive; /* 더 개성있는 폰트 (선택사항) */
        font-size:48px !important; /* 엄청 크게! */
        font-weight: bold;
        color: #8a2be2; /* 블루 바이올렛 */
        text-align: center;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.2), 0 0 10px rgba(138, 43, 226, 0.5); /* 그림자 & 빛나는 효과 */
        margin-bottom: 15px;
        letter-spacing: 2px; /* 자간 조절 */
    }
    .medium-font {
        font-size:24px !important;
        font-weight: bold;
        color: #b19cd9; /* 연한 보라 */
        text-align: center;
        margin-bottom: 50px; /* 여백 늘림 */
    }
    h2 {
        color: #6a0dad; /* 딥 퍼플 */
        text-align: center;
        font-size: 30px !important;
        margin-top: 50px;
        margin-bottom: 30px;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    h3 {
        color: #6a0dad; /* 딥 퍼플 */
        font-size: 26px !important;
        border-bottom: 3px solid #e0b0ff; /* 빛나는 보라색 밑줄 */
        padding-bottom: 12px;
        margin-top: 35px;
        font-weight: bold;
    }
    h4 {
        color: #8a2be2; /* 블루 바이올렛 */
        font-size: 22px !important;
        margin-top: 25px;
        font-weight: bold;
    }

    /* 입력 필드 및 버튼 스타일 */
    .stSelectbox label, .stTextArea label, .stButton {
        font-size: 22px !important; /* 더 크게 */
        font-weight: bold !important;
        color: #4a2d80; /* 진한 퍼플 */
    }
    .stTextArea textarea {
        min-height: 150px; /* 높이 늘림 */
        border: 3px solid #d1c4e9; /* 부드러운 보라색 테두리 */
        border-radius: 12px; /* 더 둥글게 */
        padding: 20px; /* 패딩 늘림 */
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.1);
        transition: all 0.3s ease-in-out;
    }
    .stTextArea textarea:focus {
        border-color: #8a2be2; /* 포커스 시 색상 변경 */
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.4); /* 포커스 시 빛나는 효과 */
    }
    .stButton>button {
        width: 90%; /* 버튼 너비 더 늘림 */
        height: 70px; /* 버튼 높이 더 늘림 */
        font-size: 26px; /* 폰트 더 크게 */
        background: linear-gradient(45deg, #FF69B4, #9400D3, #4B0082); /* 핫핑크-다크퍼플-인디고 그라데이션 */
        color: white;
        border-radius: 30px; /* 더 둥근 알약형 */
        border: none;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3), 0 0 20px rgba(255, 105, 180, 0.5); /* 강한 그림자 & 빛나는 효과 */
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        display: block; /* 가운데 정렬을 위해 */
        margin: 40px auto 30px auto; /* 가운데 정렬 및 여백 */
        text-shadow: 1px 1px 3px rgba(0,0,0,0.4); /* 텍스트 그림자 */
        letter-spacing: 1.5px;
    }
    .stButton>button:hover {
        transform: translateY(-5px) scale(1.02); /* 호버 시 더 크게 튀어 오름 */
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4), 0 0 30px rgba(255, 105, 180, 0.7); /* 그림자 & 빛나는 효과 강화 */
        cursor: pointer;
    }

    /* 메시지 박스 스타일 */
    .stWarning, .stSuccess, .stInfo {
        padding: 20px; /* 패딩 늘림 */
        border-radius: 15px; /* 둥글게 */
        margin-bottom: 20px;
        font-size: 18px;
        border-left: 8px solid; /* 테두리 두껍게 */
        font-weight: 500;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    }
    .stWarning { border-color: #ffc107; background-color: #fff8e1; color: #a1880a; }
    .stSuccess { border-color: #4CAF50; background-color: #e8f5e9; color: #2e7d32; }
    .stInfo { border-color: #2196F3; background-color: #e3f2fd; color: #1565c0; }
    
    /* 추천곡 상세 정보 스타일 */
    .recommendation-card {
        background: linear-gradient(135deg, #fce4ec 0%, #e1bee7 100%); /* 핑크-보라 그라데이션 */
        border-radius: 15px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1), 0 0 10px rgba(225, 190, 231, 0.7); /* 그림자 & 빛나는 효과 */
        border: 1px solid #d1c4e9;
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    }
    .recommendation-card:hover {
        transform: translateY(-8px) rotateZ(1deg); /* 더 극적인 효과 */
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.2), 0 0 25px rgba(225, 190, 231, 0.9);
    }
    .recommendation-card strong {
        color: #6a0dad;
        font-size: 1.1em;
    }
    .recommendation-card p {
        font-size: 1.05em;
        color: #4a2d80;
        margin-bottom: 5px;
    }
    .st-ag { /* st.write("---") separator */
        border-top: 2px dashed #d1c4e9; /* 점선 스타일 */
        margin: 30px 0;
    }

    /* 로딩 스피너 색상 */
    .stSpinner > div > div {
        border-top-color: #9400D3 !important;
    }

    /* 애니메이션 키프레임 */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# --- 음악 데이터베이스 --- (유지)
music_data = [
    # INFP/INFJ (깊이, 감성, 잔잔, 위로)
    {"title": "Love Story (Taylor's Version)", "artist": "Taylor Swift", "genre": ["Pop"], "mood": ["희망", "감성적", "서정적"], "mbti_tags": ["ENFP", "INFP", "ESFJ"], "emotion_tags": ["설렘", "기쁨"]},
    {"title": "Hush", "artist": "Lasse Løkken", "genre": ["Ambient"], "mood": ["잔잔함", "평온", "몽환적"], "mbti_tags": ["INFP", "INFJ", "INTP"], "emotion_tags": ["휴식", "평온", "사색"]},
    {"title": "River Flows In You", "artist": "Yiruma", "genre": ["New Age"], "mood": ["서정적", "감성적", "위로"], "mbti_tags": ["INFP", "INFJ", "ISFJ"], "emotion_tags": ["위로", "슬픔", "평온"]},
    {"title": "Into the Unknown", "artist": "Idina Menzel, Aurora (Frozen 2)", "genre": ["OST"], "mood": ["웅장함", "도전", "탐험"], "mbti_tags": ["INTJ", "INFJ", "ENFJ"], "emotion_tags": ["결심", "기대", "도전"]},
    {"title": "Somewhere Only We Know", "artist": "Keane", "genre": ["Alternative Rock"], "mood": ["회상", "서정적", "깊이있는"], "mbti_tags": ["INFP", "INFJ"], "emotion_tags": ["슬픔", "그리움", "사색"]},
    {"title": "Good Day", "artist": "IU", "genre": ["K-Pop"], "mood": ["희망", "긍정적", "밝음"], "mbti_tags": ["INFP", "ESFJ", "ENFP"], "emotion_tags": ["기쁨", "설렘", "활기"]},
    {"title": "IU - My Sea (나의 바다)", "artist": "IU", "genre": ["K-Pop"], "mood": ["깊이있는", "슬픔", "위로", "웅장함"], "mbti_tags": ["INFP", "INFJ"], "emotion_tags": ["슬픔", "위로", "감동"]},
    {"title": "Mellow Yellow", "artist": "Donovan", "genre": ["Folk Rock"], "mood": ["자유로움", "평온", "따뜻함"], "mbti_tags": ["ISFP", "INFP"], "emotion_tags": ["휴식", "평온", "즐거움"]},

    # INTJ/INTP (논리, 분석, 복잡, 집중)
    {"title": "Time", "artist": "Hans Zimmer", "genre": ["Soundtrack"], "mood": ["웅장함", "사색적", "집중"], "mbti_tags": ["INTJ", "INTP", "ISTJ"], "emotion_tags": ["집중", "분석", "결심"]},
    {"title": "Take Five", "artist": "Dave Brubeck Quartet", "genre": ["Jazz"], "mood": ["논리적", "분석적", "경쾌함"], "mbti_tags": ["INTP", "INTJ", "ISTP"], "emotion_tags": ["집중", "차분", "생각"]},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "genre": ["Classic Rock"], "mood": ["웅장함", "복잡한", "극적"], "mbti_tags": ["INTJ", "ENTJ", "INTP"], "emotion_tags": ["감탄", "고민", "스트레스 해소"]},
    {"title": "Adagio for Strings", "artist": "Samuel Barber", "genre": ["Classical"], "mood": ["웅장함", "슬픔", "사색적"], "mbti_tags": ["INTJ", "INFJ", "INTP"], "emotion_tags": ["슬픔", "위로", "사색"]},
    {"title": "Nuvole Bianche", "artist": "Ludovico Einaudi", "genre": ["Modern Classical"], "mood": ["사색적", "평온", "깊이있는"], "mbti_tags": ["INTP", "INFJ", "ISTJ"], "emotion_tags": ["휴식", "평온", "사색"]},
    {"title": "Lo-fi Hip Hop Beats to Study/Relax To", "artist": "ChilledCow", "genre": ["Lo-fi Hip Hop"], "mood": ["차분함", "집중", "평온"], "mbti_tags": ["INTP", "INTJ", "ISTJ", "ISTP"], "emotion_tags": ["집중", "평온", "휴식"]},
    {"title": "Prelude in C Major", "artist": "Bach", "genre": ["Classical"], "mood": ["차분함", "집중", "사색적"], "mbti_tags": ["INTJ", "INTP", "ISTJ"], "emotion_tags": ["집중", "평온"]},
    {"title": "Another Brick in the Wall, Part 2", "artist": "Pink Floyd", "genre": ["Progressive Rock"], "mood": ["저항", "분노", "비판적"], "mbti_tags": ["INTJ", "INTP", "ENTP"], "emotion_tags": ["분노", "스트레스 해소", "사색"]},

    # ENFJ/ESFJ (긍정, 사교, 희망, 따뜻함)
    {"title": "Happy", "artist": "Pharrell Williams", "genre": ["Pop"], "mood": ["신남", "밝음", "긍정적"], "mbti_tags": ["ENFJ", "ESFJ", "ENFP", "ESFP"], "emotion_tags": ["기쁨", "활기", "즐거움"]},
    {"title": "Don't Stop Believin'", "artist": "Journey", "genre": ["Classic Rock"], "mood": ["희망", "긍정적", "응원"], "mbti_tags": ["ENFJ", "ENTJ", "ESFJ"], "emotion_tags": ["활기", "극복", "동기 부여"]},
    {"title": "Dynamite", "artist": "BTS", "genre": ["K-Pop"], "mood": ["신남", "에너지", "활기참"], "mbti_tags": ["ENFJ", "ESFJ", "ENFP", "ESFP"], "emotion_tags": ["기쁨", "즐거움", "스트레스 해소"]},
    {"title": "Heal the World", "artist": "Michael Jackson", "genre": ["Pop"], "mood": ["희망", "감동", "연대"], "mbti_tags": ["ENFJ", "INFJ", "ESFJ"], "emotion_tags": ["감동", "위로", "결심"]},
    {"title": "What a Wonderful World", "artist": "Louis Armstrong", "genre": ["Jazz"], "mood": ["평온", "감동", "희망"], "mbti_tags": ["ISFJ", "INFJ", "ENFJ"], "emotion_tags": ["평온", "감동", "희망"]},
    {"title": "Counting Stars", "artist": "OneRepublic", "genre": ["Pop Rock"], "mood": ["희망", "긍정적", "활기참"], "mbti_tags": ["ENFP", "ENFJ"], "emotion_tags": ["활기", "희망"]},
    {"title": "Feeling Good", "artist": "Nina Simone", "genre": ["Jazz"], "mood": ["긍정적", "자신감", "활기참"], "mbti_tags": ["ENFJ", "ESFP"], "emotion_tags": ["기쁨", "활기", "자신감"]},

    # ENTP/ESTP (에너지, 논쟁, 즉흥, 도전)
    {"title": "Thunder", "artist": "Imagine Dragons", "genre": ["Alternative Rock"], "mood": ["강렬함", "에너지", "도전"], "mbti_tags": ["ENTJ", "ESTP", "ENTP"], "emotion_tags": ["활기", "극복", "분노 해소"]},
    {"title": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "genre": ["Funk"], "mood": ["경쾌함", "신남", "유쾌함"], "mbti_tags": ["ENFP", "ESFP", "ESTP", "ENTP"], "emotion_tags": ["기쁨", "즐거움", "활기"]},
    {"title": "Stronger", "artist": "Kanye West", "genre": ["Hip Hop"], "mood": ["자신감", "강렬함", "도전"], "mbti_tags": ["ENTJ", "ESTP", "ENTP"], "emotion_tags": ["동기 부여", "결심", "스트레스 해소"]},
    {"title": "Bad Guy", "artist": "Billie Eilish", "genre": ["Pop"], "mood": ["독특한", "실험적인", "시크"], "mbti_tags": ["ENTP", "INTP", "ISTP"], "emotion_tags": ["자신감", "재미", "스트레스 해소"]},
    {"title": "Flight of the Bumblebee", "artist": "Nikolai Rimsky-Korsakov", "genre": ["Classical"], "mood": ["빠른 템포", "활기참", "흥분"], "mbti_tags": ["ENTP", "ESTP"], "emotion_tags": ["활기", "재미", "스트레스 해소"]},
    {"title": "Old Town Road", "artist": "Lil Nas X ft. Billy Ray Cyrus", "genre": ["Country Trap"], "mood": ["독특한", "경쾌함", "유쾌함"], "mbti_tags": ["ENTP", "ENFP", "ESFP"], "emotion_tags": ["즐거움", "활기", "재미"]},
    {"title": "Mr. Brightside", "artist": "The Killers", "genre": ["Alternative Rock"], "mood": ["활기참", "회상", "열정"], "mbti_tags": ["ENFP", "ESTP"], "emotion_tags": ["즐거움", "스트레스 해소", "활기"]},
    {"title": "Buttercup", "artist": "Jack Stauber", "genre": ["Indie Pop"], "mood": ["독특한", "기묘한", "유쾌함"], "mbti_tags": ["INTP", "ENTP", "ISFP"], "emotion_tags": ["재미", "유쾌함"]},

    # ISTJ/ISFJ (현실적, 안정적, 차분함)
    {"title": "Moon River", "artist": "Audrey Hepburn", "genre": ["Jazz"], "mood": ["평온", "서정적", "향수"], "mbti_tags": ["ISTJ", "ISFJ", "INFJ"], "emotion_tags": ["휴식", "평온", "위로"]},
    {"title": "Weightless", "artist": "Marconi Union", "genre": ["Ambient"], "mood": ["최고의 이완", "평온", "휴식"], "mbti_tags": ["ISTJ", "ISFJ", "INFP"], "emotion_tags": ["휴식", "평온", "안정"]},
    {"title": "Hymn for the Weekend", "artist": "Coldplay", "genre": ["Pop"], "mood": ["긍정적", "활기참", "따뜻함"], "mbti_tags": ["ISFJ", "ESFJ", "ENFJ"], "emotion_tags": ["기쁨", "희망", "활기"]},
    {"title": "Fix You", "artist": "Coldplay", "genre": ["Alternative Rock"], "mood": ["위로", "감성적", "서정적"], "mbti_tags": ["ISFJ", "INFJ", "INFP"], "emotion_tags": ["위로", "슬픔", "공감"]},
    {"title": "What a Wonderful World", "artist": "Louis Armstrong", "genre": ["Jazz"], "mood": ["평온", "감동", "희망"], "mbti_tags": ["ISFJ", "INFJ", "ENFJ"], "emotion_tags": ["평온", "감동", "희망"]},
    {"title": "My Heart Will Go On", "artist": "Celine Dion", "genre": ["Pop Ballad"], "mood": ["애절함", "슬픔", "웅장함"], "mbti_tags": ["ISFJ", "INFJ", "ESFJ"], "emotion_tags": ["슬픔", "위로", "감동"]},
    {"title": "Africa", "artist": "Toto", "genre": ["Pop Rock"], "mood": ["향수", "웅장함", "감성적"], "mbti_tags": ["ISTJ", "ISFJ", "INFP"], "emotion_tags": ["평온", "그리움", "사색"]},
    {"title": "The Office Theme Song", "artist": "Jay Ferguson", "genre": ["OST"], "mood": ["경쾌함", "일상", "유쾌함"], "mbti_tags": ["ISTJ", "ENTP"], "emotion_tags": ["평온", "유쾌함"]},

    # ISTP/ISFP (독립적, 실용적, 예술적, 감성적)
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "genre": ["Classic Rock"], "mood": ["웅장함", "깊이있는", "사색적"], "mbti_tags": ["ISTP", "INTJ", "INTP"], "emotion_tags": ["사색", "몰입", "경외감"]},
    {"title": "Come Away With Me", "artist": "Norah Jones", "genre": ["Jazz"], "mood": ["차분함", "감성적", "편안함"], "mbti_tags": ["ISFP", "ISFJ", "INFJ"], "emotion_tags": ["휴식", "평온", "위로"]},
    {"title": "Believer", "artist": "Imagine Dragons", "genre": ["Alternative Rock"], "mood": ["강렬함", "에너지", "도전을"], "mbti_tags": ["ESTP", "ENTJ", "ISTP"], "emotion_tags": ["활기", "동기 부여", "스트레스 해소"]},
    {"title": "Creep", "artist": "Radiohead", "genre": ["Alternative Rock"], "mood": ["고독", "우울", "깊이있는"], "mbti_tags": ["ISFP", "INFP", "INTP"], "emotion_tags": ["슬픔", "고민", "사색"]},
    {"title": "Sweet Child o' Mine", "artist": "Guns N' Roses", "genre": ["Hard Rock"], "mood": ["열정", "강렬함", "자유로움"], "mbti_tags": ["ISTP", "ESTP", "ISFP"], "emotion_tags": ["활기", "자유", "스트레스 해소"]},

    # ESTJ/ENTJ (리더십, 추진, 에너지)
    {"title": "We Will Rock You", "artist": "Queen", "genre": ["Rock"], "mood": ["웅장함", "자신감", "추진력"], "mbti_tags": ["ESTJ", "ENTJ"], "emotion_tags": ["활기", "동기 부여", "결심"]},
    {"title": "Till I Collapse", "artist": "Eminem", "genre": ["Hip Hop"], "mood": ["강렬함", "도전", "끈기"], "mbti_tags": ["ENTJ", "ESTJ", "ESTP"], "emotion_tags": ["극복", "동기 부여", "분노 해소"]},
    {"title": "The Greatest Show", "artist": "Hugh Jackman (The Greatest Showman)", "genre": ["Musical"], "mood": ["웅장함", "쇼맨십", "자신감"], "mbti_tags": ["ENTJ", "ENFJ", "ESTJ", "ESFJ"], "emotion_tags": ["기쁨", "활기", "열정"]},
    {"title": "Lose Yourself", "artist": "Eminem", "genre": ["Hip Hop"], "mood": ["투지", "집중", "도전"], "mbti_tags": ["ENTJ", "ESTJ", "ISTP"], "emotion_tags": ["동기 부여", "결심", "집중"]},
    {"title": "Eye of the Tiger", "artist": "Survivor", "genre": ["Rock"], "mood": ["도전", "열정", "승리"], "mbti_tags": ["ENTJ", "ESTJ", "ESTP"], "emotion_tags": ["동기 부여", "활기", "극복"]},
    {"title": "Old Habits Die Hard", "artist": "Mick Jagger & Dave Stewart", "genre": ["Blues Rock"], "mood": ["진지함", "현실적", "성숙함"], "mbti_tags": ["ISTJ", "ENTJ"], "emotion_tags": ["고민", "진지함"]},

    # ESFP/ENFP (밝음, 사교, 즉흥, 재미)
    {"title": "Blinding Lights", "artist": "The Weeknd", "genre": ["Synth-pop"], "mood": ["신남", "레트로", "파티"], "mbti_tags": ["ESFP", "ENFP", "ESTP"], "emotion_tags": ["활기", "즐거움", "설렘"]},
    {"title": "Shape of You", "artist": "Ed Sheeran", "genre": ["Pop"], "mood": ["경쾌함", "로맨틱", "편안함"], "mbti_tags": ["ENFP", "ESFP"], "emotion_tags": ["기쁨", "설렘", "즐거움"]},
    {"title": "Happier", "artist": "Marshmello & Bastille", "genre": ["Electronic"], "mood": ["희망", "감성적", "활기찬"], "mbti_tags": ["ENFP", "ESFP"], "emotion_tags": ["기쁨", "슬픔 (극복)", "희망"]},
    {"title": "Butter", "artist": "BTS", "genre": ["K-Pop"], "mood": ["신남", "밝음", "경쾌함"], "mbti_tags": ["ESFP", "ENFP", "ESTP"], "emotion_tags": ["기쁨", "즐거움", "활기"]},
    {"title": "How You Like That", "artist": "BLACKPINK", "genre": ["K-Pop"], "mood": ["강렬함", "자신감", "역동적"], "mbti_tags": ["ESTP", "ENTJ", "ESFP"], "emotion_tags": ["활기", "스트레스 해소", "자신감"]},
    {"title": "Dancing Queen", "artist": "ABBA", "genre": ["Pop"], "mood": ["즐거움", "행복", "파티"], "mbti_tags": ["ESFP", "ENFP", "ESFJ"], "emotion_tags": ["기쁨", "즐거움", "활기"]},
    {"title": "Don't Stop Me Now", "artist": "Queen", "genre": ["Classic Rock"], "mood": ["신남", "에너지", "활기참"], "mbti_tags": ["ENFP", "ESFP", "ESTP", "ENTJ"], "emotion_tags": ["기쁨", "활기", "스트레스 해소"]},
    {"title": "Rolling in the Deep", "artist": "Adele", "genre": ["Soul Pop"], "mood": ["강렬함", "슬픔", "분노", "감성적"], "mbti_tags": ["INFJ", "ESTJ", "ESFP"], "emotion_tags": ["슬픔", "분노", "극복"]},
    {"title": "Imagine", "artist": "Ariana Grande", "genre": ["Pop"], "mood": ["몽환적", "감성적", "서정적"], "mbti_tags": ["INFP", "INFJ", "ISFP"], "emotion_tags": ["설렘", "사랑", "환상"]},
    {"title": "Stressed Out", "artist": "Twenty One Pilots", "genre": ["Alternative Hip Hop"], "mood": ["고민", "반항", "솔직함"], "mbti_tags": ["INFP", "INTP", "ENFP"], "emotion_tags": ["스트레스 해소", "고민", "공감"]},
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
    "ISFP": ["예술적", "감성적", "개방적", "따뜻함", "자유로움", "심미적", "인디 포크", "어쿠스틱 발라드", "영화 OST", "편안함", "창의적", "몽환적"],
    "ESTP": ["활동적", "즉흥적", "문제 해결", "현실적", "에너제틱", "강렬함", "신남", "댄스", "힙합", "록", "EDM", "도전", "활기참"],
    "ESFP": ["즉흥적", "사교적", "낙천적", "스포트라이트", "대중적", "신남", "유쾌함", "댄스", "K-POP", "밝음", "파티", "활기참"],
}

# --- 3. 프리미엄 감정 분석을 위한 키워드 (강도 점수 및 부정어 포함) ---
# 각 키워드에 (감정, 점수) 튜플을 부여하여 감정의 강도를 나타냅니다.
# 점수가 높을수록 해당 감정의 핵심 키워드임을 의미합니다.
premium_emotion_keywords = {
    "기쁨": [("기쁨", 5), ("행복", 5), ("즐거워", 4), ("신나", 4), ("웃었", 3), ("좋았", 3), ("최고", 5), ("축하", 3), ("환호", 4), ("만족", 3), ("재미", 3)],
    "슬픔": [("슬픔", 5), ("우울", 5), ("힘들어", 4), ("속상", 4), ("눈물", 3), ("외로워", 3), ("서글퍼", 4), ("아파", 3), ("그리워", 3), ("고독", 3)],
    "분노": [("분노", 5), ("화나", 5), ("짜증", 4), ("억울", 4), ("불만", 3), ("화를", 3), ("짜증나", 4), ("열받", 5), ("강렬", 2)],
    "평온": [("평온", 5), ("안정", 4), ("고요", 3), ("편안", 4), ("휴식", 3), ("잔잔", 3), ("나른", 2), ("평화", 4)],
    "활기": [("활기", 5), ("에너지", 4), ("생기", 3), ("열정", 4), ("힘내", 3), ("파이팅", 3), ("역동", 3), ("흥분", 4), ("경쾌", 3), ("도전", 3)],
    "집중": [("집중", 5), ("몰입", 4), ("생각", 3), ("고민", 3), ("연구", 2), ("분석", 2), ("파고들", 2)],
    "설렘": [("설렘", 5), ("기대", 4), ("새로운", 3), ("두근", 3), ("심장", 2), ("희망", 3), ("로맨틱", 2)],
    "스트레스 해소": [("스트레스 해소", 5), ("스트레스", 3), ("풀고", 3), ("벗어나고", 2), ("탈출", 2), ("해소", 3)],
    "위로": [("위로", 5), ("공감", 4), ("토닥", 3), ("안아줘", 3)],
    "동기 부여": [("동기 부여", 5), ("동기", 3), ("목표", 3), ("해야지", 2), ("시작", 2), ("용기", 3), ("열정", 3)],
    "자신감": [("자신감", 5), ("자신", 3), ("할 수 있다", 3), ("당당", 2), ("뿌듯", 2)],
    "그리움": [("그리움", 5), ("향수", 4), ("옛날", 2)],
}

# 부정어 리스트 (간단한 부정 처리)
negative_words = ["아니", "않", "못", "없", "안", "그렇지 않아", "힘들지 않아"] # 이 키워드가 있으면 감정 점수 낮추기

def analyze_premium_emotions(diary_text):
    """
    일기 텍스트에서 프리미엄 감정을 분석하여 메인 감정과 보조 감정(강도 포함)을 반환합니다.
    """
    emotion_scores = {emotion: 0 for emotion in premium_emotion_keywords.keys()}
    text_lower = diary_text.lower()
    
    # 긍정/부정 판단을 위한 간단한 카운트
    negation_count = 0
    for neg_word in negative_words:
        if neg_word in text_lower:
            negation_count += 1

    # 각 감정 키워드 매칭 및 점수 부여
    for emotion_type, keywords_with_scores in premium_emotion_keywords.items():
        for keyword, score_value in keywords_with_scores:
            if keyword in text_lower:
                emotion_scores[emotion_type] += score_value
    
    # 부정어가 감지되면 점수 조정 (긍정적인 감점, 부정적인 감정 가중치 유지 또는 증폭)
    if negation_count > 0:
        for emotion in ["기쁨", "활기", "설렘", "자신감"]: # 긍정적 감정
            emotion_scores[emotion] = max(0, emotion_scores[emotion] - negation_count * 3) # 부정어 개수만큼 감점
        for emotion in ["슬픔", "분노", "고민", "스트레스 해소"]: # 부정적 감정은 유지 또는 약간 상승
            emotion_scores[emotion] += negation_count * 1 # 부정어에 대한 작은 가중치

    # 가장 높은 점수의 감정 찾기
    max_score = 0
    main_emotion = "중립"
    for emotion, score in emotion_scores.items():
        if score > max_score:
            max_score = score
            main_emotion = emotion
    
    # 보조 감정들 (메인 감정 점수의 30% 이상, 0점 초과)
    sub_emotions = []
    if main_emotion != "중립":
        for emotion, score in emotion_scores.items():
            if emotion != main_emotion and score > 0 and score >= max_score * 0.3: # 메인 감정의 30% 이상 점수면 보조 감정으로
                sub_emotions.append((emotion, score))
    
    # 보조 감정들을 점수 순으로 정렬
    sub_emotions.sort(key=lambda x: x[1], reverse=True)

    return main_emotion, [e for e, s in sub_emotions[:2]] # 최대 2개의 보조 감정만 반환

st.markdown('<p class="big-font">✨ 나의 MBTI & 감정 음악 추천기 ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="medium-font">💖 너의 MBTI와 오늘의 감정을 바탕으로 맞춤 음악을 추천해 줄게!</p>', unsafe_allow_html=True)
st.write("---")

# MBTI 선택
mbti_options = ["🌟 MBTI를 선택해주세요"] + sorted(list(mbti_music_preferences.keys()))
selected_mbti = st.selectbox("💖 **1. 나의 MBTI는 무엇인가요?**", mbti_options)

# 감정 일기 입력
diary_entry = st.text_area("📝 **2. 오늘의 감정을 자유롭게 써주세요.** (예: 오늘 정말 즐거웠어! 슬픈 영화를 봤더니 눈물이 났어)", height=150)

# 추천 버튼
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎶 **마법의 음악 추천 받기!** 🔮"):
        if selected_mbti == "🌟 MBTI를 선택해주세요":
            st.warning("🚨 MBTI를 선택해야 마법이 시작될 수 있어!")
        elif not diary_entry:
            st.warning("🚨 오늘의 감정을 적어줘야 마법 지팡이가 제대로 작동해!")
        else:
            with st.spinner('✨ 너를 위한 음악을 신중하게 고르고 있어... 마법 시전 중!'):
                time.sleep(1.5) # 실제 처리 시간처럼 보이게 약간 지연
                st.success(f"✔️ 선택 MBTI: **{selected_mbti}** ✨")

                # 1. 프리미엄 감정 분석 실행
                main_emotion, sub_emotions = analyze_premium_emotions(diary_entry)
                
                # 감정 표시
                if main_emotion != "중립":
                    st.info(f"✨ 일기에서 감지된 오늘의 메인 감정은 **{main_emotion}**이야!")
                    if sub_emotions:
                        st.info(f"✨ 보조 감정으로는 **{', '.join(sub_emotions)}**도 함께 느껴지네!")
                else:
                    st.info("✨ 오늘의 감정은 좀 더 중립적인 것 같아! 다양한 음악을 추천해 줄게!")

                # 2. MBTI 선호 태그 가져오기
                mbti_preferred_tags = mbti_music_preferences.get(selected_mbti, [])
                st.info(f"✨ {selected_mbti} 유형의 음악 선호 경향: **{', '.join(mbti_preferred_tags[:5])}{'...' if len(mbti_preferred_tags) > 5 else ''}**") 

                # 3. 추천 로직 (MBTI 태그 + 프리미엄 감정 태그 매칭)
                
                # 가중치 설정 (메인 감정에 더 큰 가중치)
                main_emotion_weight = 5 # 메인 감정에 주는 가중치
                sub_emotion_weight = 2  # 보조 감정에 주는 가중치
                mbti_weight = 1       # MBTI 취향 매칭 점수

                recommendation_scores = {}
                for music in music_data:
                    score = 0
                    # MBTI 취향 매칭 점수
                    if selected_mbti in music.get("mbti_tags", []): 
                        score += mbti_weight * 2 # 해당 MBTI가 직접 명시된 곡에 더 높은 점수
                    
                    combined_music_tags = music.get("mood", []) + music.get("genre", []) 
                    for mbti_pref_tag in mbti_preferred_tags:
                        if mbti_pref_tag in combined_music_tags:
                            score += mbti_weight
                    
                    # 프리미엄 감정 매칭 점수
                    if main_emotion != "중립" and main_emotion in music.get("emotion_tags", []):
                        score += main_emotion_weight
                    
                    for sub_e in sub_emotions:
                        if sub_e in music.get("emotion_tags", []):
                            score += sub_emotion_weight
                    
                    recommendation_scores[music["title"]] = score
                
                # 점수가 높은 순으로 정렬
                sorted_recommendations = sorted(recommendation_scores.items(), key=lambda item: item[1], reverse=True)
                
                # 점수가 0점인 음악 제외 (겹치는 태그가 아예 없는 경우)
                filtered_recommendations = [item for item in sorted_recommendations if item[1] > 0]
                
                # 중복 추천 방지 및 다양성 확보를 위해 상위 몇 곡만 가져오되, 점수가 같으면 무작위 선택
                final_recommendations_shuffled = []
                scores_map = {}
                for title, score in filtered_recommendations:
                    if score not in scores_map:
                        scores_map[score] = []
                    scores_map[score].append(title)
                
                sorted_scores_keys = sorted(scores_map.keys(), reverse=True)

                for score in sorted_scores_keys:
                    current_group = scores_map[score]
                    random.shuffle(current_group) 
                    for title in current_group:
                        final_recommendations_shuffled.append(title)
                        if len(final_recommendations_shuffled) >= 3: 
                            break
                    if len(final_recommendations_shuffled) >= 3:
                        break

                st.subheader("🎶 **너를 위한 마법 같은 음악!** 🎧")
                if final_recommendations_shuffled:
                    num_display_recommendations = min(3, len(final_recommendations_shuffled)) 
                    for i in range(num_display_recommendations):
                        recommended_title = final_recommendations_shuffled[i]
                        recommended_music = next((music for music in music_data if music["title"] == recommended_title), None)
                        if recommended_music:
                            st.markdown(f'<div class="recommendation-card">', unsafe_allow_html=True)
                            st.markdown(f"<h4>🌟 **{recommended_music['title']}** - {recommended_music['artist']}</h4>", unsafe_allow_html=True)
                            st.markdown(f"<p>💜 장르: <strong>{', '.join(recommended_music['genre'])}</strong></p>", unsafe_allow_html=True) 
                            st.markdown(f"<p>💫 분위기: <strong>{', '.join(recommended_music['mood'])}</strong></p>", unsafe_allow_html=True)
                            st.markdown('</div>', unsafe_allow_html=True)
                            if i < num_display_recommendations -1: 
                                st.write("---")
                else:
                    st.warning("😕 아쉽지만 너의 MBTI와 오늘의 감정에 딱 맞는 마법 같은 곡을 찾지 못했어! 다른 감정을 입력하거나, MBTI를 바꿔서 다시 시도해볼까?")
