import streamlit as st

# --- 0. Streamlit 페이지 기본 설정 (이번엔 이모티콘으로 문제 없도록!) ---
st.set_page_config(layout="centered", page_title="🌟 이모티콘 드레스업 스튜디오 🌟")

# --- 1. CSS 스타일링 (화려하고 예쁘게!) ---
st.markdown("""
    <style>
    .main-title {
        font-size: 40px !important;
        font-weight: bold;
        color: #FF1493; /* 핫핑크 강조 */
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .section-header {
        font-size: 25px !important;
        font-weight: bold;
        color: #8A2BE2; /* 보라색 강조 */
        margin-top: 30px;
        margin-bottom: 15px;
        border-bottom: 3px solid #EE82EE; /* 보라색 밑줄 */
        padding-bottom: 5px;
    }
    .stRadio > label, .stSelectbox > label {
        font-size: 18px;
        font-weight: bold;
        color: #4682B4; /* 스틸블루 강조 */
    }
    .emoji-display-area {
        background-color: #F8F8FF; /* 배경색으로 구분 */
        border: 2px solid #FFC0CB; /* 연핑크 테두리 */
        border-radius: 15px;
        padding: 20px;
        margin-top: 30px;
        margin-bottom: 30px;
        text-align: center;
        min-height: 250px; /* 최소 높이 설정 */
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column; /* 세로 정렬 */
    }
    .character-container {
        font-size: 150px; /* 캐릭터 이모티콘을 더 크게! */
        line-height: 1.2; /* 줄간격 조절 */
    }
    .small-text {
        font-size: 18px;
        color: #6A5ACD; /* 보라색 계열 */
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='main-title'>🌟 이모티콘 드레스업 스튜디오 🌟</p>", unsafe_allow_html=True)
st.write("✨ 파일 없이, 이모티콘의 마법으로! 캐릭터에게 옷을 입히고 배경을 꾸며보세요! ✨")
st.write("---")

# --- 2. 이모티콘 에셋 준비 (✨ 마법의 옷장과 배경!) ---
# 이모티콘으로 옷 입는 느낌을 내기 위해, 미리 '조합된' 이모티콘을 사용합니다.
# 캐릭터 기본 이모티콘 (얼굴 포함!)
CHARACTER_BASES = {
    "👩🏻‍🦰 여자 캐릭터": "👩🏻‍🦰", # 얼굴이 포함된 이모티콘 사용
    "👨🏻‍🦱 남자 캐릭터": "👨🏻‍🦱"  # 얼굴이 포함된 이모티콘 사용
}

# 배경 이모티콘
BACKGROUND_EMOJIS = {
    "화려한 도시 🏙️": "🏙️",
    "아늑한 해변 🏖️": "🏖️",
    "푸른 공원 🌳": "🌳",
    "신나는 파티장 🎉": "🎉",
    "카페에서 ☕": "☕"
}

# 옷장 (상의, 하의, 전체 룩 개념으로 조합)
# 캐릭터 이모티콘은 기본 몸통 역할, 옷 이모티콘은 그 위에 덮이는 역할 (심볼릭하게)
# 실제 겹쳐지진 않지만, 선택에 따라 캐릭터 이모티콘과 조합되는 형태
CLOTHING_STYLES = {
    "캐주얼 룩": { # 티셔츠 + 청바지 스타일
        "여성": "👚👖", # 상의와 하의를 이모티콘으로 표현 (실제로는 안겹쳐짐, 옆에 배치)
        "남성": "👕👖"
    },
    "오피스 룩": { # 셔츠/블라우스 + 슬랙스/스커트 스타일
        "여성": "👔👗", # 원피스 느낌으로
        "남성": "🤵‍♂️👔" # 슈트 입은 남성 이모티콘 활용 (새로운 시도!)
    },
    "스포티 룩": { # 운동복 + 운동화 스타일
        "여성": "🏃‍♀️👟", # 달리는 여성 + 운동화
        "남성": "🏃‍♂️👟" # 달리는 남성 + 운동화
    },
    "드레스업 룩": { # 드레스/정장 + 구두 스타일
        "여성": "💃👠", # 춤추는 여성 + 하이힐
        "남성": "🕺👞" # 춤추는 남성 + 구두 (심볼릭한 고급 슈트 느낌)
    }
}

# 액세서리 이모티콘 (캐릭터 옆에 추가될 예정)
ACCESSORY_EMOJIS = {
    "선택 안함": "",
    "멋진 모자 🧢": "🧢",
    "선글라스 😎": "😎",
    "가방 👜": "👜",
    "목걸이 💎": "💎",
    "우산 ☔": "☔"
}

# --- 3. 사이드바 - 설정 컨트롤 (옷장 구현!) ---
with st.sidebar:
    st.header("✨ 이모티콘 옷장 ✨")
    
    st.markdown("<p class='section-header'>1. 내 캐릭터는?</p>", unsafe_allow_html=True)
    selected_char_gender_key = st.radio("성별을 선택하세요:", list(CHARACTER_BASES.keys()), key="char_gender")
    
    st.markdown("<p class='section-header'>2. 배경 선택</p>", unsafe_allow_html=True)
    selected_background_key = st.selectbox("어떤 배경으로 갈까요?", list(BACKGROUND_EMOJIS.keys()), key="bg_select")
    
    st.markdown("<p class='section-header'>3. 오늘의 스타일! 🛍️</p>", unsafe_allow_html=True)
    selected_style_key = st.selectbox("오늘의 룩은?", list(CLOTHING_STYLES.keys()), key="style_select")

    st.markdown("<p class='section-header'>4. 액세서리 추가 ✨</p>", unsafe_allow_html=True)
    selected_accessory_key = st.selectbox("어떤 액세서리를 착용할까요?", list(ACCESSORY_EMOJIS.keys()), key="acc_select")
    
    st.write("---")
    st.info("💡 **이모티콘 옷 입히기 팁:** 이모티콘은 실제 이미지처럼 겹쳐지지는 않지만, 선택하신 스타일에 맞춰 캐릭터와 옷 이모티콘이 조합되어 '옷 입는 느낌'을 상징적으로 연출해 드려요!")

# --- 4. 메인 화면 - 이모티콘 코디 결과 보여주기 ---
st.markdown("<p class='section-header'>💖 짜잔! 당신의 이모티콘 코디 완성! 💖</p>", unsafe_allow_html=True)

st.markdown("""
    <div class="emoji-display-area">
        <div class="character-container">
            <!-- 배경 이모티콘 -->
            <span style="font-size: 80px; margin-right: 15px;">%s</span> 
            <!-- 캐릭터 및 옷 스타일 이모티콘 -->
            <span style="font-size: 120px;">%s%s</span>
            <!-- 액세서리 이모티콘 -->
            <span style="font-size: 80px; margin-left: 15px;">%s</span>
        </div>
        <p class="small-text">클릭해서 드래그하면 이모티콘 코드를 복사할 수 있어요!</p>
    </div>
""" % (
    BACKGROUND_EMOJIS[selected_background_key],
    # 캐릭터 성별에 따라 기본 캐릭터 이모티콘과 옷 스타일 이모티콘 조합
    CHARACTER_BASES[selected_char_gender_key], # 기본 캐릭터 (얼굴+몸)
    CLOTHING_STYLES[selected_style_key]["여성"] if "여자" in selected_char_gender_key else CLOTHING_STYLES[selected_style_key]["남성"],
    ACCESSORY_EMOJIS[selected_accessory_key]
), unsafe_allow_html=True)


st.success("💖 세상에 하나뿐인 나만의 이모티콘 패션 스타일 완성! 💖")
st.write(f"👉 **선택 장소:** {selected_background_key}")
st.write(f"👉 **캐릭터:** {selected_char_gender_key}")
st.write(f"👉 **선택 스타일:** {selected_style_key}")
st.write(f"👉 **액세서리:** {selected_accessory_key if selected_accessory_key != '' else '없음'}")

st.write("---")
st.balloons() # 화려한 풍선 효과는 빠질 수 없죠! 🎉

# --- 5. 게스트 계정 안내 ---
st.markdown("""
    <div style="background-color:#E0FFFF; padding:15px; border-radius:10px; margin-top:30px;">
        <p style="font-size:16px; font-weight:bold; color:#008B8B;">
        🎁 아직 게스트로 이용 중이시네요! 🎁
        </p>
        <p style="font-size:15px; color:#483D8B;">
        이 재미있는 이모티콘 드레스업 게임처럼 나만의 멋진 프로젝트를 만들고 저장하거나, 
        다른 친구들과 아이디어를 공유하고 싶으시다면
        간단하게 회원가입을 해보시는 건 어떠세요? 
        더욱 많은 즐거움을 경험하실 수 있을 거예요! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
