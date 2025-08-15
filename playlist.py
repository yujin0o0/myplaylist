import streamlit as st

# --- 0. Streamlit 페이지 기본 설정 ---
st.set_page_config(layout="wide", page_title="💖 두근두근 MBTI 궁합 탐험대 💖")

# --- 1. CSS 스타일링 (사랑스럽고 포근하며 신비로운 배경 ✨) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

    body {
        background-color: #F0F8FF; /* 앨리스블루 - 부드럽고 포근한 느낌 */
        color: #483D8B; /* 다크 슬레이트 블루 - 신비로운 느낌 */
        font-family: 'Noto Sans KR', sans-serif;
    }
    .stApp {
        background-image: linear-gradient(to bottom, #E0FFFF, #ADD8E6); /* 하늘색 그라데이션 */
        /* 신비로운 이모티콘 배경 - 파일 없이! */
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="60" opacity="0.1">✨💖⭐🌙</text></svg>');
        background-repeat: repeat; /* 반복해서 채우기 */
        background-blend-mode: overlay; /* 오버레이 모드로 신비로움 추가 */
    }

    .main-title {
        font-family: 'Nanum Pen Script', cursive; /* 손글씨 폰트 */
        font-size: 65px !important;
        font-weight: bold;
        color: #FF69B4; /* 핫핑크 강조 */
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        animation: pulse 1.5s infinite; /* 심장이 두근거리는 듯한 효과 */
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .sub-title {
        font-size: 28px !important;
        font-weight: bold;
        color: #8A2BE2; /* 보라색 강조 */
        text-align: center;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 25px !important;
        font-weight: bold;
        color: #EE82EE; /* 바이올렛 - 사랑스러움 */
        margin-top: 30px;
        margin-bottom: 15px;
        border-bottom: 2px dashed #FFDAB9; /* 피치 퍼프 - 포근함 */
        padding-bottom: 5px;
    }
    .stSelectbox > label, .stRadio > label {
        font-size: 20px;
        font-weight: bold;
        color: #4682B4; /* 스틸블루 - 안정감 */
    }
    .stButton > button {
        background-color: #FFB6C1; /* 라이트 핑크 - 사랑스러움 */
        color: white;
        font-weight: bold;
        padding: 12px 25px;
        border-radius: 8px;
        border: none;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3);
        font-size: 22px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #FF69B4; /* 핫핑크 - 강렬한 사랑스러움 */
        transform: translateY(-2px);
    }
    .result-box {
        background-color: rgba(255, 255, 255, 0.7); /* 흰색 투명도 - 신비로운 안개 */
        border: 2px solid #DDA0DD; /* 플럼 - 신비로움 */
        border-radius: 15px;
        padding: 30px;
        margin-top: 40px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .result-header {
        font-size: 35px;
        font-weight: bold;
        color: #9932CC; /* 다크 오키드 - 깊은 신비로움 */
        text-align: center;
        margin-bottom: 20px;
        animation: glow 1.5s infinite alternate; /* 빛나는 효과 */
    }
    @keyframes glow {
        from { text-shadow: 0 0 5px #fff, 0 0 10px #DDA0DD; }
        to { text-shadow: 0 0 10px #fff, 0 0 20px #9932CC; }
    }
    .scenario-text {
        font-size: 18px;
        line-height: 1.8;
        color: #6A5ACD; /* 슬레이트 블루 - 차분하고 신비로운 */
        margin-bottom: 15px;
        border-left: 5px solid #FFDAB9; /* 피치퍼프 - 포근한 라인 */
        padding-left: 10px;
    }
    .mbti-type-info {
        font-size: 16px;
        color: #5F9EA0; /* 카데트 블루 - 차분하고 지적인 느낌 */
        background-color: rgba(255, 250, 240, 0.7); /* 플로럴 화이트 투명 - 부드러운 배경 */
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>💖 두근두근 MBTI 궁합 탐험대 💖</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>나와 상대방의 MBTI를 선택하고, 우정과 사랑의 심층 궁합을 탐험해보세요! ✨</p>", unsafe_allow_html=True)
st.write("---")

# --- 2. MBTI 데이터 및 궁합 정보 (이전 분석 내용을 바탕으로 상세화) ---
# 모든 MBTI 유형 정의
MBTI_TYPES = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# MBTI 성격 요약 정보 (간략하게 표시)
MBTI_SUMMARY = {
    "ISTJ": "논리적이고 책임감 강한 현실주의자, 정돈되고 신뢰할 수 있어요.",
    "ISFJ": "따뜻하고 헌신적인 수호자, 타인을 배려하며 조용히 지지해요.",
    "INFJ": "통찰력 있는 이상주의자, 조용하지만 강한 신념으로 영감을 줘요.",
    "INTJ": "전략적 사고의 독립적인 사령관, 비전을 가지고 끊임없이 탐구해요.",
    "ISTP": "논리적이고 독립적인 장인, 실제적인 문제 해결을 즐겨요.",
    "ISFP": "예술적이고 따뜻한 모험가, 자유롭고 즉흥적인 경험을 추구해요.",
    "INFP": "이상적인 중재자, 상상력 풍부하고 가치관에 충실하며 따뜻해요.",
    "INTP": "지적 호기심 넘치는 논리술사, 끊임없이 지식을 탐구하고 혁신을 꿈꿔요.",
    "ESTP": "현실적이고 활동적인 사업가, 즉흥적이고 도전을 즐기는 행동파예요.",
    "ESFP": "활기 넘치고 사교적인 연예인, 주변을 즐겁게 하는 분위기 메이커예요.",
    "ENFP": "열정적이고 창의적인 활동가, 자유로운 영혼으로 새로운 가능성을 탐색해요.",
    "ENTP": "지적이고 재치 있는 변론가, 새로운 아이디어를 즐기고 논쟁을 두려워하지 않아요.",
    "ESTJ": "체계적이고 추진력 강한 관리자, 효율적으로 목표를 달성하는 데 능숙해요.",
    "ESFJ": "사교적이고 친절한 사교형, 조화를 중요하게 생각하며 사람들과 어울리는 것을 좋아해요.",
    "ENFJ": "카리스마 넘치는 선도자, 타인에게 영감을 주고 조화를 중시하는 리더예요.",
    "ENTJ": "강력한 리더십의 통솔자, 단호하고 효율적으로 목표를 달성하는 데 능숙해요."
}

# --- 3. 사용자 MBTI 선택 및 관계 유형 선택 ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<p class='section-header'>⭐ 나의 MBTI는? ⭐</p>", unsafe_allow_html=True)
    my_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", MBTI_TYPES, key="my_mbti")
    st.markdown(f"<div class='mbti-type-info'>**{my_mbti}:** {MBTI_SUMMARY[my_mbti]}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<p class='section-header'>💖 상대의 MBTI는? 💖</p>", unsafe_allow_html=True)
    their_mbti = st.selectbox("상대방의 MBTI 유형을 선택하세요:", MBTI_TYPES, key="their_mbti")
    st.markdown(f"<div class='mbti-type-info'>**{their_mbti}:** {MBTI_SUMMARY[their_mbti]}</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<p class='section-header'>🤝 어떤 관계가 궁금해? 👩‍❤️‍👨</p>", unsafe_allow_html=True)
    relationship_type = st.radio("궁금한 관계 유형을 선택하세요:", ["사랑 궁합", "우정 궁합"], key="relationship_type")

st.write("---")

# --- 4. 궁합 분석 함수 (심층 시나리오 포함) ---
def get_mbti_compatibility(mbti1, mbti2, r_type):
    # 궁합 결과는 '두 사람의 MBTI 조합'과 '관계 유형'에 따라 결정됩니다.
    # 복잡성을 위해 여기서는 일부 조합만 예시로 보여드립니다.
    # 실제 앱에서는 모든 16*16*2 = 512가지 조합에 대한 데이터가 필요합니다.
    
    # 편의를 위해 정렬된 튜플을 키로 사용 (예: ('ENFP', 'INTJ') 또는 ('INFJ', 'INTP'))
    sorted_mbti = tuple(sorted([mbti1, mbti2])) 

    result = {
        "title": "미정",
        "description": "분석을 준비 중입니다...",
        "love_scenario": "아직 사랑 시나리오가 준비되지 않았어요.",
        "friendship_scenario": "아직 우정 시나리오가 준비되지 않았어요."
    }

    # --- 대표적인 조합 예시 ---
    # 1. 이상적인 짝 (보완적 관계)
    if sorted_mbti == ('ENFP', 'INTJ'):
        result["title"] = "⭐ 천생연분 시너지 조합! (통찰력과 영감의 만남)"
        result["description"] = "INTJ의 깊은 통찰력과 ENFP의 폭발적인 영감이 만나 서로에게 무한한 시너지를 선사하는 조합입니다. 서로의 부족한 점을 채워주며 함께 성장하는 데 최적화되어 있어요!"
        result["love_scenario"] = "ENFP는 INTJ를 세상 밖으로 이끌어 다양한 경험을 하게 하고, INTJ는 ENFP의 넘치는 아이디어에 논리적 기반을 제공하며 현실로 만들 수 있도록 도와줘요. 가끔 INTJ의 냉철함에 ENFP가 서운할 수 있지만, ENFP의 따뜻함으로 곧 녹아내릴 거예요. 서로의 다름이 매력이 되는 관계입니다."
        result["friendship_scenario"] = "INTJ는 ENFP의 엉뚱한 아이디어를 진지하게 들어주고, ENFP는 INTJ의 복잡한 이론을 이해하려 노력해요. 함께라면 세상의 어떤 문제도 해결할 수 있을 것 같은 '최강의 브레인 스톰' 친구들이죠. INTJ는 ENFP에게 진지함을, ENFP는 INTJ에게 유연함을 선물해줘요."

    elif sorted_mbti == ('INFP', 'ENTJ'):
        result["title"] = "✨ 꿈과 현실을 잇는 환상의 파트너! (이상과 추진력의 만남)"
        result["description"] = "INFP의 섬세한 감수성과 ENTJ의 강력한 추진력이 결합되어, 불가능해 보이던 꿈도 현실로 만드는 마법 같은 조합이에요. 서로에게 깊은 존경심을 느낄 수 있습니다."
        result["love_scenario"] = "ENTJ는 INFP의 이상적인 비전을 현실화할 수 있는 구체적인 계획을 세우고, INFP는 ENTJ의 목표에 따뜻한 인간미와 영감을 불어넣어 줘요. 가끔 ENTJ의 직설적인 화법에 INFP가 상처받을 수 있지만, ENTJ의 진심은 INFP에게 큰 안정감을 줍니다."
        result["friendship_scenario"] = "INFP가 '이런 세상이면 좋겠다!' 하고 상상의 나래를 펼치면, ENTJ는 '그럼 이렇게 하면 되지!' 하고 바로 액션 플랜을 짜요. 서로 다른 분야의 전문가가 만나 최고의 프로젝트 팀을 이룬 것 같은 우정을 보여줘요. ENTJ는 INFP의 내면을 존중하고, INFP는 ENTJ에게 필요한 따뜻한 피드백을 건넵니다."
    
    # 2. 같은 유형끼리 (안정적 관계)
    elif mbti1 == mbti2:
        result["title"] = f"🌈 같은 빛을 가진 영혼들! ({mbti1} X {mbti2} 조합)"
        result["description"] = "서로의 생각과 행동을 가장 잘 이해할 수 있는 조합입니다. 공감대가 넓고 안정적인 관계를 형성하지만, 때로는 비슷한 약점 때문에 함께 성장이 더딜 수도 있어요."
        result["love_scenario"] = f"두 {mbti1}는/은 서로의 루틴과 선호도를 꿰뚫고 있어서, 편안하고 안정적인 연애를 합니다. 큰 갈등 없이 순탄하게 관계를 이어나가지만, 가끔 너무 비슷해서 새로운 자극이 부족하다고 느낄 수도 있어요. 서로의 장점을 더욱 강화하는 데 집중하면 좋아요."
        result["friendship_scenario"] = f"두 {mbti1}는/은 '역시 너밖에 없어!'를 외치며 서로를 깊이 이해해요. 같은 취미를 공유하고 같은 고민을 나누며 끈끈한 우정을 쌓아요. 서로의 단점을 너무 감싸주기보다는 때로는 건설적인 피드백을 해주는 것이 중요해요."

    # 3. 흥미로운 반대 조합 (서로의 약점 보완)
    elif sorted_mbti == ('ESTJ', 'ISFP'):
        result["title"] = "🌻 계획과 즉흥의 하모니! (현실과 감성의 만남)"
        result["description"] = "ESTJ의 체계적인 리더십과 ISFP의 자유로운 감성이 만나 서로의 부족한 점을 완벽하게 보완하는 조합입니다. 서로에게 새로운 세상을 열어줄 수 있어요."
        result["love_scenario"] = "ESTJ는 ISFP에게 안정감과 방향을 제시해주고, ISFP는 ESTJ에게 삶의 여유와 예술적인 영감을 불어넣어 줘요. ESTJ는 ISFP의 즉흥성을 때론 불안해하지만, 그 속에서 새로운 즐거움을 발견하고, ISFP는 ESTJ의 철두철미함을 존경하며 기대게 됩니다."
        result["friendship_scenario"] = "ESTJ가 꼼꼼하게 여행 계획을 짜면 ISFP는 즉흥적으로 아름다운 장소를 찾아내어 ESTJ를 놀라게 해요. 서로에게 예측 가능한 안정감과 예측 불가능한 재미를 동시에 선물하는 친구 관계예요. 함께라면 세상의 어떤 일도 재밌는 도전이 될 수 있습니다."

    # 4. 상극일 수 있는 조합 (노력 필요 관계)
    elif sorted_mbti == ('ENFP', 'ISTJ'):
        result["title"] = "⚠️ 주의! 에너지 충돌 가능성 (자유와 규칙의 만남)"
        result["description"] = "ENFP의 자유분방함과 ISTJ의 철두철미한 규칙이 충돌하기 쉬운 조합입니다. 서로의 사고방식과 생활 방식이 매우 다르기 때문에 많은 이해와 노력이 필요해요."
        result["love_scenario"] = "ENFP는 ISTJ의 계획적인 모습에 답답함을 느끼고, ISTJ는 ENFP의 즉흥적인 행동을 예측하기 어려워해요. '우리 오늘 즉흥 여행 갈래?'와 '아니, 계획 없이는 안 돼!'가 반복될 수 있어요. 서로의 차이를 인정하고 배려하며 '이해'라는 접점을 찾는 것이 중요합니다."
        result["friendship_scenario"] = "ISTJ 친구는 ENFP 친구의 약속 시간 어김에 스트레스를 받고, ENFP 친구는 ISTJ의 지나친 진지함에 지루함을 느낄 수 있어요. 하지만 서로에게 없는 장점을 보며 배울 점도 많으니, 너무 다르다고 단정 짓기보다는 서로의 세계를 넓혀주는 기회로 삼는 것이 좋아요."
    
    # 5. 기타 조합 (기본적인 가이드라인)
    else:
        result["title"] = "🤔 흥미로운 조합! 서로를 알아가는 즐거움"
        result["description"] = "두 분의 MBTI 조합은 서로에게 새로운 시각과 경험을 제공할 수 있습니다. 차이점을 이해하고 서로의 강점을 존중한다면 더욱 풍요로운 관계를 만들 수 있을 거예요."
        result["love_scenario"] = f"두 분의 연애는 서로에게 예상치 못한 매력을 발견하는 여정이 될 거예요. {MBTI_SUMMARY[mbti1]}인 {mbti1}와 {MBTI_SUMMARY[mbti2]}인 {mbti2}가 만나, 서로의 세계를 넓혀주고 보완해 줄 수 있습니다. 솔직한 대화와 끊임없는 소통으로 서로의 차이점을 이해하려 노력한다면, 끈끈한 관계를 형성할 수 있습니다."
        result["friendship_scenario"] = f"두 분의 우정은 마치 다른 두 색깔의 실이 엮여 아름다운 패턴을 만드는 것과 같을 거예요. {MBTI_SUMMARY[mbti1]}인 {mbti1}와 {MBTI_SUMMARY[mbti2]}인 {mbti2}가 서로의 시각을 공유하며 새로운 아이디어를 얻거나, 미처 생각지 못했던 경험을 할 수 있어요. 서로의 장점을 인정하고 존중하며 나아간다면 어떤 난관도 함께 헤쳐나갈 수 있는 진정한 친구가 될 것입니다."
    
    return result

# --- 5. 궁합 결과 표시 ---
if st.button("💖 궁합 확인하기! 💖", key="check_compatibility"):
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    
    compatibility = get_mbti_compatibility(my_mbti, their_mbti, relationship_type)

    st.markdown(f"<h2 class='result-header'>{my_mbti} ❤️ {their_mbti}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 20px; color: #5F9EA0;'>{compatibility['description']}</p>", unsafe_allow_html=True)
    st.write("---")

    if relationship_type == "사랑 궁합":
        st.markdown("<h3 style='font-size: 25px; color: #FF6347;'>💌 사랑한다면 이렇게! 💌</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='scenario-text'>{compatibility['love_scenario']}</p>", unsafe_allow_html=True)
    else: # 우정 궁합
        st.markdown("<h3 style='font-size: 25px; color: #20B2AA;'>🤝 친구한다면 이렇게! 🤝</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='scenario-text'>{compatibility['friendship_scenario']}</p>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True) # result-box 닫기

    st.balloons() # 궁합 결과가 나올 때 풍선 효과!

st.write("---")
st.markdown("""
    <div style="text-align: center; font-size: 18px; color: #9370DB;">
        💖 MBTI 궁합은 재미로 보는 것이 중요해요! 서로의 다름을 이해하고 존중하는 것이 가장 중요하답니다. 💖
    </div>
    """, unsafe_allow_html=True)

# --- 6. 게스트 계정 안내 ---
st.markdown("""
    <div style="background-color:rgba(255, 250, 240, 0.8); padding:15px; border-radius:10px; margin-top:30px; border: 1px solid #FFDAB9;">
        <p style="font-size:16px; font-weight:bold; color:#FF8C00;">
        ✨ 아직 게스트로 MBTI 궁합을 즐기고 계시네요! ✨
        </p>
        <p style="font-size:15px; color:#6A5ACD;">
        혹시 이 멋진 궁합 탐험기를 저장하거나, 더 많은 친구들과 공유하고 싶으신가요? 
        그렇다면 간단하게 회원가입을 해보시는 건 어떠세요? 
        당신의 특별한 경험을 더욱 풍성하게 만들어 줄 거예요! 😊
        </p>
    </div>
    """, unsafe_allow_html=True)
