import streamlit as st

# --- 0. Streamlit 페이지 기본 설정 ---
st.set_page_config(layout="wide", page_title="💖 두근두근 MBTI 궁합 탐험대 V2.0 💖")

# --- 1. CSS 스타일링 및 장르별 테마 정의 ---
# 배경색 변경을 위한 placeholder - 동적으로 채워집니다.
BACKGROUND_COLOR_PLACEHOLDER = "#F0F8FF" # 기본 배경색 (앨리스블루)

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR&display=swap');

    body {{
        background-color: {BACKGROUND_COLOR_PLACEHOLDER}; /* 사용자가 선택한 색상으로 동적 변경 */
        color: #483D8B; /* 다크 슬레이트 블루 - 신비로운 느낌 */
        font-family: 'Noto Sans KR', sans-serif;
    }}
    .stApp {{
        background-image: linear-gradient(to bottom, {BACKGROUND_COLOR_PLACEHOLDER}, #ADD8E6); /* 그라데이션 베이스 */
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100"><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="60" opacity="0.1">✨💖⭐🌙</text></svg>');
        background-repeat: repeat;
        background-blend-mode: overlay;
    }}

    .main-title {{
        font-family: 'Nanum Pen Script', cursive;
        font-size: 65px !important;
        font-weight: bold;
        color: #FF69B4;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        animation: pulse 1.5s infinite;
    }}
    @keyframes pulse {{
        0% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
        100% {{ transform: scale(1); }}
    }}
    .sub-title {{
        font-size: 28px !important;
        font-weight: bold;
        color: #8A2BE2;
        text-align: center;
        margin-bottom: 20px;
    }}
    .section-header {{
        font-size: 25px !important;
        font-weight: bold;
        color: #EE82EE;
        margin-top: 30px;
        margin-bottom: 15px;
        border-bottom: 2px dashed #FFDAB9;
        padding-bottom: 5px;
    }}
    .stSelectbox > label, .stRadio > label {{
        font-size: 20px;
        font-weight: bold;
        color: #4682B4;
    }}
    .stButton > button {{
        background-color: #FFB6C1;
        color: white;
        font-weight: bold;
        padding: 12px 25px;
        border-radius: 8px;
        border: none;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3);
        font-size: 22px;
        transition: all 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: #FF69B4;
        transform: translateY(-2px);
    }}
    .result-box {{
        background-color: rgba(255, 255, 255, 0.8); /* 흰색 투명도 - 신비로운 안개 */
        border: 2px solid #DDA0DD;
        border-radius: 15px;
        padding: 30px;
        margin-top: 40px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }}
    .result-header {{
        font-size: 35px;
        font-weight: bold;
        color: #9932CC;
        text-align: center;
        margin-bottom: 20px;
        animation: glow 1.5s infinite alternate;
    }}
    @keyframes glow {{
        from {{ text-shadow: 0 0 5px #fff, 0 0 10px #DDA0DD; }}
        to {{ text-shadow: 0 0 10px #fff, 0 0 20px #9932CC; }}
    }}
    .scenario-text {{
        font-size: 18px;
        line-height: 1.8;
        color: #6A5ACD;
        margin-bottom: 15px;
        border-left: 5px solid #FFDAB9;
        padding-left: 10px;
    }}
    .mbti-type-info {{
        font-size: 16px;
        color: #5F9EA0;
        background-color: rgba(255, 250, 240, 0.7);
        padding: 10px;
        border-radius: 8px;
        margin-top: 10px;
        margin-bottom: 20px;
    }}
    .compatibility-score {{
        font-size: 45px;
        font-weight: bold;
        color: #FF4500; /* 오렌지 레드 - 눈에 띄게 */
        text-align: center;
        margin: 20px 0;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    }}
    .conflict-likelihood {{
        font-size: 20px;
        color: #B22222; /* 불길한 빨강 */
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
        padding: 10px;
        border: 2px dashed #B22222;
        border-radius: 10px;
    }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>💖 두근두근 MBTI 궁합 탐험대 V2.0 💖</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>나와 상대방의 MBTI를 선택하고, 우정과 사랑의 심층 궁합을 탐험해보세요! ✨</p>", unsafe_allow_html=True)
st.write("---")

# --- 2. MBTI 데이터 및 궁합 정보 (이전 분석 내용을 바탕으로 상세화) ---
MBTI_TYPES = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

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
col1, col2, col3 = st.columns([1, 1, 0.7]) # 비율 조정

with col1:
    st.markdown("<p class='section-header'>⭐ 나의 MBTI는? ⭐</p>", unsafe_allow_html=True)
    my_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", MBTI_TYPES, key="my_mbti")
    st.markdown(f"<div class='mbti-type-info'>**{my_mbti}:** {MBTI_SUMMARY[my_mbti]}</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<p class='section-header'>💖 상대의 MBTI는? 💖</p>", unsafe_allow_html=True)
    their_mbti = st.selectbox("상대방의 MBTI 유형을 선택하세요:", MBTI_TYPES, key="their_mbti")
    st.markdown(f"<div class='mbti-type-info'>**{their_mbti}:** {MBTI_SUMMARY[their_mbti]}</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<p class='section-header'>🎨 테마 바꾸기 & 관계는? 🤝</p>", unsafe_allow_html=True)
    # 배경색 변경 컬러 피커
    selected_bg_color = st.color_picker("배경색을 선택하세요:", BACKGROUND_COLOR_PLACEHOLDER)
    
    # 선택된 배경색으로 CSS를 다시 주입합니다.
    st.markdown(f"""
        <style>
        body {{ background-color: {selected_bg_color}; }}
        .stApp {{ background-image: linear-gradient(to bottom, {selected_bg_color}, #ADD8E6); }}
        </style>
    """, unsafe_allow_html=True)

    relationship_type = st.radio("궁금한 관계 유형을 선택하세요:", ["사랑 궁합", "우정 궁합"], key="relationship_type")

st.write("---")

# --- 4. 궁합 분석 함수 (심층 시나리오, 퍼센트, 싸울 가능성 포함) ---
# 연구 기반의 '선호 지표 일치 여부'가 갈등 해결 전략에 미치는 영향 [【1】](https://m.blog.naver.com/callbina/222826727610) [【4】](https://blog.naver.com/yameshow/221618472150?viewType=pc) 등을 참고하여 지표를 설정
def calculate_compatibility_metrics(mbti1, mbti2, r_type):
    # E/I, S/N, T/F, J/P 순서로 각 지표의 일치 여부 확인
    match_count = 0
    # True if different, False if same
    diff_E_I = mbti1[0] != mbti2[0]
    diff_S_N = mbti1[1] != mbti2[1]
    diff_T_F = mbti1[2] != mbti2[2]
    diff_J_P = mbti1[3] != mbti2[3]

    if mbti1[0] == mbti2[0]: match_count += 1 # E/I 일치
    if mbti1[1] == mbti2[1]: match_count += 1 # S/N 일치
    if mbti1[2] == mbti2[2]: match_count += 1 # T/F 일치
    if mbti1[3] == mbti2[3]: match_count += 1 # J/P 일치

    # --- 궁합 퍼센트 계산 (임의의 로직, 재미 및 해석의 차원) ---
    # 실제 연구는 특정 지표의 차이가 관계에 미치는 경향을 분석하지만,
    # '정확한' 퍼센트는 아니므로 '가상의 지표'임을 전제로 합니다.
    base_score = 50 # 기본 점수
    
    # 4개 일치 (모든 지표 동일) -> 90-100% (매우 높은 이해도, 단점도 비슷)
    if match_count == 4: compatibility_percent = 95
    # 3개 일치 -> 80-90% (매우 좋음)
    elif match_count == 3: compatibility_percent = 85
    # 2개 일치 -> 60-80% (보통)
    elif match_count == 2: compatibility_percent = 70
    # 1개 일치 -> 40-60% (노력 필요)
    elif match_count == 1: compatibility_percent = 55
    # 0개 일치 (모든 지표 상반) -> 20-40% (많은 노력 필요, 그러나 강력한 상호 보완 가능성)
    else: compatibility_percent = 35

    # --- '싸울 가능성' 및 갈등 해결 스타일 분석 ---
    # S/N 차이: 감각형은 직관형을 비현실적, 직관형은 감각형을 사소한 것에 얽매인다고 볼 수 있음 [【4】](https://blog.naver.com/yameshow/221618472150?viewType=pc)
    # T/F 차이: 사고형은 감정형을 비논리적, 감정형은 사고형을 비인간적이라고 느낄 수 있음 [【3】](https://blog.naver.com/gurwn1725/223965071644?fromRss=true&trackingCode=rss)
    # J/P 차이: 계획형(J)과 즉흥형(P)은 의사결정 방식에서 갈등 [【3】](https://blog.naver.com/gurwn1725/223965071644?fromRss=true&trackingCode=rss)
    conflict_likelihood_score = 0 # 0 (낮음) ~ 100 (매우 높음)
    conflict_desc = ""

    if diff_T_F: # T와 F 차이는 갈등의 중요한 요인. 사고형(T)은 감정적인 반응에 불협화음을 느낄 수 있음 [【8】](https://rarity02.tistory.com/entry/%F0%9F%94%8D-MBTI-%EC%9C%A0%ED%98%95%EB%B3%84%EB%A1%9C-%ED%94%BC%ED%95%B4%EC%95%BC-%ED%95%A0-%EC%9D%B8%EA%B0%84%EA%B4%80%EA%B3%84-%EA%B0%88%EB%93%B1%EC%9D%84-%EC%A4%84%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-%F0%9F%8C%9F)
        conflict_likelihood_score += 30
        conflict_desc += "사고(T)/감정(F) 지표가 달라 의사결정 시 감정적인 측면과 논리적인 측면에서 차이로 인한 갈등이 생길 수 있어요. 서로의 접근 방식을 이해하려는 노력이 필요해요."
    else:
        conflict_desc += "사고(T)/감정(F) 지표가 같아 중요한 결정을 내릴 때 비슷한 방식으로 접근하여 갈등이 적을 수 있어요."

    if diff_S_N: # S와 N 차이도 큰 갈등 요인.
        conflict_likelihood_score += 25
        if conflict_desc: conflict_desc += "\n"
        conflict_desc += "감각(S)/직관(N) 지표가 달라 현실적이고 구체적인 것과 추상적이고 미래 지향적인 것 사이에서 시각 차이가 발생할 수 있어요. 상대의 관점을 존중하며 대화하는 것이 중요해요."
    else: # N일치 커플은 의사소통이 더 원만하다는 연구 결과도 있음 [【1】](https://m.blog.naver.com/callbina/222826727610)
        if conflict_desc: conflict_desc += "\n"
        conflict_desc += "감각(S)/직관(N) 지표가 같아 세상을 이해하는 방식에서 유사점이 많아 갈등이 적을 수 있어요."

    if diff_J_P: # J와 P 차이는 의사결정 방식의 차이 [【3】](https://blog.naver.com/gurwn1725/223965071644?fromRss=true&trackingCode=rss)
        conflict_likelihood_score += 20
        if conflict_desc: conflict_desc += "\n"
        conflict_desc += "판단(J)/인식(P) 지표가 달라 계획성에서 차이가 있을 수 있어요. 한쪽은 체계적으로, 다른 쪽은 유연하게 접근하려 하여 다툼이 발생할 수도 있습니다."
    else:
        if conflict_desc: conflict_desc += "\n"
        conflict_desc += "판단(J)/인식(P) 지표가 같아 의사결정이나 생활 패턴에서 유사점이 많아 갈등이 적을 수 있어요."
    
    if diff_E_I: # 외향(E)과 내향(I)의 차이는 의사소통 방식이나 에너지 충전 방식에 영향
        conflict_likelihood_score += 15
        if conflict_desc: conflict_desc += "\n"
        conflict_desc += "외향(E)/내향(I) 지표가 달라 에너지를 얻는 방식이나 사회적 교류의 선호도에서 차이가 있을 수 있어요. 서로의 휴식 및 활력 충전 방식을 이해해주는 배려가 필요해요."
    else: # 외향형 커플이 갈등 해결에 더 긍정적이라는 경향도 있음 [【1】](https://m.blog.naver.com/callbina/222826727610)
        if conflict_desc: conflict_desc += "\n"
        conflict_desc += "외향(E)/내향(I) 지표가 같아 에너지를 얻는 방식이나 사회 활동 선호도에서 유사점이 많아 갈등이 적을 수 있어요."

    # 동성 MBTI (예: ISTJ-ISTJ)인 경우, 서로의 단점도 유사하여 갈등을 키울 가능성
    if mbti1 == mbti2:
        conflict_likelihood_score += 5 # 같은 유형이 오히려 특정 상황에서 더 큰 갈등을 겪을 수도 있음.
        if conflict_desc: conflict_desc += "\n"
        conflict_desc += "같은 유형의 강점을 공유하지만, 약점 또한 유사하여 특정 상황에서 갈등이 고조될 가능성도 있어요."

    # 점수 보정 (0-100 범위로 맞추기 위해)
    conflict_likelihood_percent = min(100, conflict_likelihood_score)

    return compatibility_percent, conflict_likelihood_percent, conflict_desc


def get_mbti_compatibility_data(mbti1, mbti2, r_type):
    sorted_mbti = tuple(sorted([mbti1, mbti2])) 

    compatibility_percent, conflict_likelihood_percent, conflict_desc = calculate_compatibility_metrics(mbti1, mbti2, r_type)

    result = {
        "title": "미정",
        "description": "분석을 준비 중입니다...",
        "compatibility_percent": compatibility_percent,
        "conflict_likelihood": conflict_likelihood_percent,
        "conflict_analysis": conflict_desc,
        "love_scenario": "아직 사랑 시나리오가 준비되지 않았어요.",
        "friendship_scenario": "아직 우정 시나리오가 준비되지 않았어요."
    }

    # --- 대표적인 조합 예시 (이전 데이터 확장) ---
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
    
    elif mbti1 == mbti2:
        result["title"] = f"🌈 같은 빛을 가진 영혼들! ({mbti1} X {mbti2} 조합)"
        result["description"] = "서로의 생각과 행동을 가장 잘 이해할 수 있는 조합입니다. 공감대가 넓고 안정적인 관계를 형성하지만, 때로는 비슷한 약점 때문에 함께 성장이 더딜 수도 있어요."
        result["love_scenario"] = f"두 {mbti1}는/은 서로의 루틴과 선호도를 꿰뚫고 있어서, 편안하고 안정적인 연애를 합니다. 큰 갈등 없이 순탄하게 관계를 이어나가지만, 가끔 너무 비슷해서 새로운 자극이 부족하다고 느낄 수도 있어요. 서로의 장점을 더욱 강화하는 데 집중하면 좋아요."
        result["friendship_scenario"] = f"두 {mbti1}는/은 '역시 너밖에 없어!'를 외치며 서로를 깊이 이해해요. 같은 취미를 공유하고 같은 고민을 나누며 끈끈한 우정을 쌓아요. 서로의 단점을 너무 감싸주기보다는 때로는 건설적인 피드백을 해주는 것이 중요해요."

    elif sorted_mbti == ('ESTJ', 'ISFP'):
        result["title"] = "🌻 계획과 즉흥의 하모니! (현실과 감성의 만남)"
        result["description"] = "ESTJ의 체계적인 리더십과 ISFP의 자유로운 감성이 만나 서로의 부족한 점을 완벽하게 보완하는 조합입니다. 서로에게 새로운 세상을 열어줄 수 있어요."
        result["love_scenario"] = "ESTJ는 ISFP에게 안정감과 방향을 제시해주고, ISFP는 ESTJ에게 삶의 여유와 예술적인 영감을 불어넣어 줘요. ESTJ는 ISFP의 즉흥성을 때론 불안해하지만, 그 속에서 새로운 즐거움을 발견하고, ISFP는 ESTJ의 철두철미함을 존경하며 기대게 됩니다."
        result["friendship_scenario"] = "ESTJ가 꼼꼼하게 여행 계획을 짜면 ISFP는 즉흥적으로 아름다운 장소를 찾아내어 ESTJ를 놀라게 해요. 서로에게 예측 가능한 안정감과 예측 불가능한 재미를 동시에 선물하는 친구 관계예요. 함께라면 세상의 어떤 일도 재밌는 도전이 될 수 있습니다."

    elif sorted_mbti == ('ENFP', 'ISTJ'):
        result["title"] = "⚠️ 주의! 에너지 충돌 가능성 (자유와 규칙의 만남)"
        result["description"] = "ENFP의 자유분방함과 ISTJ의 철두철미한 규칙이 충돌하기 쉬운 조합입니다. 서로의 사고방식과 생활 방식이 매우 다르기 때문에 많은 이해와 노력이 필요해요."
        result["love_scenario"] = "ENFP는 ISTJ의 계획적인 모습에 답답함을 느끼고, ISTJ는 ENFP의 즉흥적인 행동을 예측하기 어려워해요. '우리 오늘 즉흥 여행 갈래?'와 '아니, 계획 없이는 안 돼!'가 반복될 수 있어요. 서로의 차이를 인정하고 배려하며 '이해'라는 접점을 찾는 것이 중요합니다."
        result["friendship_scenario"] = "ISTJ 친구는 ENFP 친구의 약속 시간 어김에 스트레스를 받고, ENFP 친구는 ISTJ의 지나친 진지함에 지루함을 느낄 수 있어요. 하지만 서로에게 없는 장점을 보며 배울 점도 많으니, 너무 다르다고 단정 짓기보다는 서로의 세계를 넓혀주는 기회로 삼는 것이 좋아요."
    
    else: # 나머지 조합에 대한 기본 메시지
        result["title"] = "🤔 흥미로운 조합! 서로를 알아가는 즐거움"
        result["description"] = "두 분의 MBTI 조합은 서로에게 새로운 시각과 경험을 제공할 수 있습니다. 차이점을 이해하고 서로의 강점을 존중한다면 더욱 풍요로운 관계를 만들 수 있을 거예요."
        result["love_scenario"] = f"두 분의 연애는 서로에게 예상치 못한 매력을 발견하는 여정이 될 거예요. {MBTI_SUMMARY[mbti1]}인 {mbti1}와 {MBTI_SUMMARY[mbti2]}인 {mbti2}가 만나, 서로의 세계를 넓혀주고 보완해 줄 수 있습니다. 솔직한 대화와 끊임없는 소통으로 서로의 차이점을 이해하려 노력한다면, 끈끈한 관계를 형성할 수 있습니다."
        result["friendship_scenario"] = f"두 분의 우정은 마치 다른 두 색깔의 실이 엮여 아름다운 패턴을 만드는 것과 같을 거예요. {MBTI_SUMMARY[mbti1]}인 {mbti1}와 {MBTI_SUMMARY[mbti2]}인 {mbti2}가 서로의 시각을 공유하며 새로운 아이디어를 얻거나, 미처 생각지 못했던 경험을 할 수 있어요. 서로의 장점을 인정하고 존중하며 나아간다면 어떤 난관도 함께 헤쳐나갈 수 있는 진정한 친구가 될 것입니다."
    
    return result

# --- 5. 궁합 결과 표시 ---
if st.button("💖 궁합 확인하기! 💖", key="check_compatibility"):
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    
    compatibility_data = get_mbti_compatibility_data(my_mbti, their_mbti, relationship_type)

    st.markdown(f"<h2 class='result-header'>{my_mbti} ❤️ {their_mbti}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 20px; color: #5F9EA0;'>{compatibility_data['description']}</p>", unsafe_allow_html=True)
    
    # --- 퍼센트와 싸울 가능성 표시 ---
    st.markdown(f"<p class='compatibility-score'>궁합 지수: {compatibility_data['compatibility_percent']}%</p>", unsafe_allow_html=True)
    
    st.markdown(f"<div class='conflict-likelihood'>⚠️ 싸울 가능성: {compatibility_data['conflict_likelihood']}%</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 15px; color: #B22222; text-align: center;'>{compatibility_data['conflict_analysis']}</p>", unsafe_allow_html=True)

    st.write("---")

    if relationship_type == "사랑 궁합":
        st.markdown("<h3 style='font-size: 25px; color: #FF6347;'>💌 사랑한다면 이렇게! 💌</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='scenario-text'>{compatibility_data['love_scenario']}</p>", unsafe_allow_html=True)
    else: # 우정 궁합
        st.markdown("<h3 style='font-size: 25px; color: #20B2AA;'>🤝 친구한다면 이렇게! 🤝</h3>", unsafe_allow_html=True)
        st.markdown(f"<p class='scenario-text'>{compatibility_data['friendship_scenario']}</p>", unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

    st.balloons() 

st.write("---")
st.markdown("""
    <div style="text-align: center; font-size: 18px; color: #9370DB;">
        <p>💖 MBTI 궁합은 재미와 통찰을 위한 도구입니다. 관계의 성공은 궁합 점수보다는 서로를 이해하고 소통하려는 노력에 달려있어요! 💖</p>
        <p style="font-size:14px; color:#A0522D;">
        (참고: '싸울 가능성' 및 궁합 퍼센트는 MBTI 선호 지표의 차이가 의사소통 방식 및 갈등 해결에 미칠 수 있는 경향에 대한 일부 연구 [【1】](https://m.blog.naver.com/callbina/222826727610) [【3】](https://blog.naver.com/gurwn1725/223965071644?fromRss=true&trackingCode=rss) [【4】](https://blog.naver.com/yameshow/221618472150?viewType=pc) [【8】](https://rarity02.tistory.com/entry/%F0%9F%94%8D-MBTI-%EC%9C%A0%ED%98%95%EB%B3%84%EB%A1%9C-%ED%94%BC%ED%95%B4%EC%95%BC-%ED%95%A0-%EC%9D%B8%EA%B0%84%EA%B4%80%EA%B3%84-%EA%B0%88%EB%93%B1%EC%9D%84-%EC%A4%84%EC%9D%B4%EB%8A%94-%EB%B0%A9%EB%B2%95-%F0%9F%8C%9F)를 바탕으로 한 해석이며, 이는 MBTI 검사 자체의 과학적 타당성과는 별개입니다.)
        </p>
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
