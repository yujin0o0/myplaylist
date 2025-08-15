import streamlit as st

# --- 1. 페이지 설정 (심플하게 이모티콘 문제 없도록!) ---
st.set_page_config(layout="centered", page_title="💖 이모티콘 패션왕 챌린지 💖")

st.markdown("""
    <style>
    .big-font {
        font-size:35px !important;
        font-weight: bold;
        color: #FF1493; /* 찐한 핫핑크! */
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-font {
        font-size:22px !important;
        font-weight: bold;
        color: #4682B4; /* 시원한 스틸블루! */
        margin-top: 25px;
        margin-bottom: 10px;
    }
    .emoji-display {
        font-size: 100px; /* 캐릭터 이모티콘을 왕 크게! */
        text-align: center;
        margin-top: 30px;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='big-font'>💖 이모티콘 패션왕 챌린지! 💖</p>", unsafe_allow_html=True)
st.write("✨ 파일 없이, 설치 없이, 오직 이모티콘으로만! ✨")
st.write("---")

# --- 2. 이모티콘 에셋 준비 (✨ 마법의 이모티콘들 ✨) ---

# 기본 캐릭터 이모티콘
CHARACTER_EMOJIS = {
    "👩‍🦰 여성 캐릭터": "👩‍🦰",
    "👨‍🦱 남성 캐릭터": "👨‍🦱",
    "👧 귀요미 소녀": "👧",
    "👦 장난꾸러기 소년": "👦",
    "🐈‍⬛ 신비한 고양이": "🐈‍⬛" # 이모티콘 고양이 캐릭터도 가능!
}

# 상의 이모티콘
TOP_EMOJIS = {
    "선택 안함": "",
    "캐주얼 티셔츠 👕": "👕",
    "우아한 블라우스 👚": "👚",
    "따뜻한 스웨터 🧣": "🧣",
    "힙한 후드티  Hoody": " Hoody", # 이모티콘이 없으면 텍스트로!
    "정장 자켓 👔": "👔"
}

# 하의/원피스 이모티콘
BOTTOM_EMOJIS = {
    "선택 안함": "",
    "시크한 바지 👖": "👖",
    "예쁜 스커트 👗": "👗",
    "반바지 🩳": "🩳"
}

# 신발 이모티콘
SHOES_EMOJIS = {
    "선택 안함": "",
    "운동화 👟": "👟",
    "하이힐 👠": "👠",
    "샌들 🩴": "🩴",
    "부츠 👢": "👢"
}

# 액세서리 이모티콘
ACCESSORY_EMOJIS = {
    "선택 안함": "",
    "멋진 모자 🧢": "🧢",
    "선글라스 😎": "😎",
    "목걸이 💎": "💎",
    "백팩 🎒": "🎒",
    "우산 ☔": "☔"
}

# 배경/장소 이모티콘 (캐릭터 앞에 붙을 예정!)
LOCATION_EMOJIS = {
    "화창한 해변 🏖️": "🏖️",
    "고요한 숲길 🌳": "🌳",
    "활기찬 도시 🏙️": "🏙️",
    "아늑한 카페 ☕": "☕",
    "신나는 파티 🎉": "🎉"
}

# --- 3. 사이드바 - 설정 컨트롤 (선택의 재미!) ---
with st.sidebar:
    st.header("✨ 나만의 코디 만들기 ✨")
    
    st.markdown("<p class='sub-font'>1. 나만의 캐릭터는?</p>", unsafe_allow_html=True)
    selected_char = st.radio("어떤 캐릭터로 꾸밀까요?", list(CHARACTER_EMOJIS.keys()), key="char_select")
    
    st.markdown("<p class='sub-font'>2. 어떤 장소로 떠날까요?</p>", unsafe_allow_html=True)
    selected_location = st.selectbox("캐릭터가 갈 장소를 골라주세요!", list(LOCATION_EMOJIS.keys()), key="location_select")
    
    st.markdown("<p class='sub-font'>3. 의상 쇼핑 타임! 🛍️</p>", unsafe_allow_html=True)
    selected_top = st.selectbox("상의", list(TOP_EMOJIS.keys()), key="top_select")
    selected_bottom = st.selectbox("하의/원피스", list(BOTTOM_EMOJIS.keys()), key="bottom_select")
    selected_shoes = st.selectbox("신발", list(SHOES_EMOJIS.keys()), key="shoes_select")
    selected_accessory = st.selectbox("액세서리", list(ACCESSORY_EMOJIS.keys()), key="accessory_select")
    
    st.write("---")
    st.info("💡 **이모티콘 꿀팁:** 선택하신 이모티콘들이 옆으로 주르륵 나열돼요! 실제 이미지처럼 겹쳐지진 않지만, 조합하는 재미가 쏠쏠하답니다! 😉")


# --- 4. 메인 화면 - 이모티콘 코디 결과 보여주기 ---
st.markdown("<p class='sub-font'>✨ 짜잔! 당신의 이모티콘 코디 완성! ✨</p>", unsafe_allow_html=True)

# 선택된 이모티콘들 조합
char_emoji = CHARACTER_EMOJIS[selected_char]
top_emoji = TOP_EMOJIS[selected_top]
bottom_emoji = BOTTOM_EMOJIS[selected_bottom]
shoes_emoji = SHOES_EMOJIS[selected_shoes]
accessory_emoji = ACCESSORY_EMOJIS[selected_accessory]
location_emoji = LOCATION_EMOJIS[selected_location]

# 이모티콘을 조합하여 하나의 문자열로 만듭니다.
# 장소 이모티콘이 캐릭터 앞에 오고, 캐릭터 다음에 옷들이 주르륵 붙게!
# 실제 이미지처럼 겹쳐지지는 않지만, 선택 조합을 볼 수 있습니다.
combined_emojis = f"{location_emoji} {char_emoji}{top_emoji}{bottom_emoji}{shoes_emoji}{accessory_emoji}"

st.markdown(f"<p class='emoji-display'>{combined_emojis}</p>", unsafe_allow_html=True)

st.success("💖 세상에 하나뿐인 나만의 이모티콘 패션 완성! 💖")
st.write(f"👉 장소: **{selected_location}**")
st.write(f"👉 캐릭터: **{selected_char}**")
st.write(f"👉 오늘의 코디: **{selected_top}, {selected_bottom}, {selected_shoes}, {selected_accessory}**")

# 결과 텍스트 복사 버튼 (편의성!)
st.text_input("복사하고 싶다면 여기에서 복사!", value=combined_emojis)


st.write("---")
st.balloons() # 풍선 파티로 화려하게 마무리!

# --- 5. 게스트 계정 안내 ---
st.markdown("""
    <div style="background-color:#E0FFFF; padding:15px; border-radius:10px; margin-top:30px;">
        <p style="font-size:16px; font-weight:bold; color:#008B8B;">
        🎁 혹시 모르셨다면? 🎁
        </p>
        <p style="font-size:15px; color:#483D8B;">
        지금은 게스트로 이 재미있는 이모티콘 게임을 즐기고 계세요! 🥳
        나중에 이 멋진 아이디어를 더 발전시키거나,
        친구들과 코드를 공유하고 싶으시다면
        간단하게 회원가입을 해보시는 건 어떠세요?
        더 많은 가능성이 열릴 거예요! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
