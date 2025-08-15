import streamlit as st
import random
import time # 로딩 메시지를 위한 시간 지연

# --- 0. Streamlit 페이지 기본 설정 ---
st.set_page_config(layout="wide", page_title="🌟 내맘대로 이야기 생성기 V3.0 🌟")

# --- CSS 스타일링 및 장르별 테마 정의 ---
# 장르별로 다른 배경, 색상, 이모티콘 조합
GENRE_THEMES = {
    "코믹 😂": {
        "primary_color": "#FFD700", # 황금색 (주황 계열)
        "secondary_color": "#FFA500", # 주황색
        "text_color": "#36454F", # 차콜 그레이
        "font_family": "cursive", # 손글씨
        "background_emojis": "🤡🎉😂✨",
        "loading_messages": ["코믹한 이야기가 생각나는 중...", "개그 코드를 찾는 중...", "배꼽 잡을 준비! 🤣"]
    },
    "판타지 🧙‍♀️": {
        "primary_color": "#8A2BE2", # 보라색
        "secondary_color": "#DA70D6", # 오키드
        "text_color": "#F8F8FF", # 고스트 화이트
        "font_family": "serif", # 고전적 느낌
        "background_emojis": "✨🧚‍♀️🦄🐉🌟",
        "loading_messages": ["마법 잉크를 제조하는 중...", "신비로운 주문을 외는 중...", "전설이 시작됩니다! 🔮"]
    },
    "미스터리 🕵️‍♂️": {
        "primary_color": "#36454F", # 차콜 그레이
        "secondary_color": "#696969", # 어두운 회색
        "text_color": "#FFFAFA", # 스노우 화이트
        "font_family": "monospace", # 고정폭 (터미널 느낌)
        "background_emojis": "🔎 shadowy 🕯️🤫",
        "loading_messages": ["수수께끼를 푸는 중...", "단서를 조합하는 중...", "진실은 저 너머에... 🤯"]
    },
    "로맨스 💖": {
        "primary_color": "#FF69B4", # 핫핑크
        "secondary_color": "#FFC0CB", # 핑크
        "text_color": "#5C4033", # 코코아 브라운
        "font_family": "sans-serif", # 부드러운 느낌
        "background_emojis": "💖💞💕💌🌸",
        "loading_messages": ["두근두근 설레는 중...", "운명을 짜는 중...", "사랑이 피어납니다... 🥰"]
    },
    "스릴 😱": {
        "primary_color": "#B22222", # 불길한 빨강
        "secondary_color": "#8B0000", # 다크 레드
        "text_color": "#F5F5DC", # 베이지
        "font_family": "sans-serif", # 직관적
        "background_emojis": "💀🔪🩸⛓️‍💥",
        "loading_messages": ["심장을 조여오는 중...", "숨 막히는 추격전 준비 중...", "절대 뒤돌아보지 마세요... 😨"]
    }
}

# 기본 테마 (선택 없을 시)
DEFAULT_THEME = GENRE_THEMES["판타지 🧙‍♀️"] 

def get_css(theme):
    return f"""
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR&display=swap');

    body {{
        background-color: {theme['primary_color']}; /* 배경색 */
        color: {theme['text_color']}; /* 기본 텍스트 색상 */
        font-family: {theme['font_family']};
    }}
    .main-title {{
        font-family: 'Nanum Pen Script', cursive; /* 메인 제목 폰트 */
        font-size: 60px !important;
        font-weight: bold;
        color: {theme['secondary_color']}; /* 보조 색상 */
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        animation: neon 1.5s ease-in-out infinite alternate;
    }}
    @keyframes neon {{
        from {{
            text-shadow:
                0 0 10px #fff,
                0 0 20px #fff,
                0 0 30px #fff,
                0 0 40px {theme['secondary_color']},
                0 0 70px {theme['secondary_color']},
                0 0 80px {theme['secondary_color']},
                0 0 100px {theme['secondary_color']},
                0 0 150px {theme['secondary_color']};
        }}
        to {{
            text-shadow:
                0 0 5px #fff,
                0 0 10px #fff,
                0 0 15px #fff,
                0 0 20px {theme['primary_color']},
                0 0 35px {theme['primary_color']},
                0 0 40px {theme['primary_color']},
                0 0 50px {theme['primary_color']},
                0 0 75px {theme['primary_color']};
        }}
    }}
    .section-header {{
        font-size: 30px !important;
        font-weight: bold;
        color: {theme['secondary_color']};
        margin-top: 35px;
        margin-bottom: 20px;
        border-bottom: 4px dashed {theme['primary_color']};
        padding-bottom: 8px;
    }}
    .stTextInput > label, .stSelectbox > label, .stSlider > label, .stRadio > label {{
        font-size: 20px;
        font-weight: bold;
        color: {theme['text_color']};
    }}
    .stButton > button {{
        background-color: {theme['secondary_color']};
        color: {theme['text_color']};
        font-weight: bold;
        padding: 12px 25px;
        border-radius: 8px;
        border: none;
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3);
        font-size: 22px;
        transition: all 0.3s ease;
    }}
    .stButton > button:hover {{
        background-color: {theme['primary_color']};
        transform: translateY(-2px);
    }}
    .story-output-box {{
        background-color: {theme['text_color']};
        border: 2px solid {theme['secondary_color']};
        border-radius: 15px;
        padding: 25px;
        margin-top: 40px;
        min-height: 400px;
        display: flex;
        flex-direction: column;
        justify-content: flex-start; /* 텍스트가 위에서 시작 */
        align-items: center;
        text-align: center;
        overflow-y: auto; /* 내용이 길어지면 스크롤 가능 */
    }}
    .story-text {{
        font-family: 'Nanum Pen Script', cursive; /* 이야기 본문 폰트 */
        font-size: 30px;
        line-height: 1.8;
        color: #333; /* 검정색 */
        text-align: left; /* 좌측 정렬 */
    }}
    .sparkle {{
        animation: sparkle 1s infinite alternate;
    }}
    @keyframes sparkle {{
        from {{" opacity: 0.5; "}}
        to {{" opacity: 1; "}}
    }}
    </style>
    """

# --- 2. 이야기의 재료 입력 받기 ---
st.markdown("<p class='main-title'>✍️✨ 나만의 이야기 만들기 ✨✍️</p>", unsafe_allow_html=True)
st.write("당신이 던지는 단어들이 환상적인 이야기가 되는 마법을 경험하세요! ✨")
st.write("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<p class='section-header'>1. 이야기의 장르를 골라봐! 🎭</p>", unsafe_allow_html=True)
    selected_genre = st.selectbox(
        "어떤 분위기의 이야기를 원하시나요?",
        list(GENRE_THEMES.keys()),
        key="genre_select"
    )
    
    current_theme = GENRE_THEMES.get(selected_genre, DEFAULT_THEME)
    st.markdown(get_css(current_theme), unsafe_allow_html=True) # 선택된 장르에 따라 CSS 적용

    st.markdown("<p class='section-header'>2. 주인공은 누구? ✨</p>", unsafe_allow_html=True)
    protagonist = st.text_input(
        "주인공의 이름 또는 특징을 입력하세요:",
        value="호기심 많은 탐험가 렐라",
        help="예: '용감한 로봇 알로', '소심한 마법사 엘리나', '장난꾸러기 고양이 야옹'"
    )
    protagonist_personality = st.text_input(
        "주인공의 성격이나 특징 (선택 사항):",
        value="",
        help="예: '솔직한', '영리한', '게으른', '사교적인'"
    )

with col2:
    st.markdown("<p class='section-header'>3. 이야기가 펼쳐질 곳은? 🗺️</p>", unsafe_allow_html=True)
    setting = st.text_input(
        "이야기가 시작될 장소를 입력하세요:",
        value="하늘을 나는 마법의 섬",
        help="예: '버려진 고성', '미래 도시의 뒷골목', '달콤한 과자로 가득 찬 숲'"
    )
    setting_atmosphere = st.text_input(
        "장소의 분위기 (선택 사항):",
        value="",
        help="예: '으스스한', '반짝이는', '시끌벅적한', '평화로운'"
    )

    st.markdown("<p class='section-header'>4. 핵심 아이템/인물은? 💎</p>", unsafe_allow_html=True)
    key_element = st.text_input(
        "이야기의 중심이 될 핵심 아이템이나 인물을 입력하세요:",
        value="시간을 멈추는 마법 회중시계",
        help="예: '수수께끼의 오래된 일기장', '말하는 꽃', '잃어버린 용의 알'"
    )

st.write("---")

# --- 3. 이야기 생성 함수 (더욱 다양하고 문맥에 맞게!) ---
def generate_story_v3(protagonist, personality, setting, atmosphere, key_element, genre):
    
    story_parts = []
    
    # 템플릿 데이터 (장르별, 플롯 단계별 문장들)
    # 훨씬 더 많은 문장들을 추가하여 다양성을 확보할 수 있습니다.
    story_templates = {
        "발단": {
            "코믹 😂": [
                f"{atmosphere} {setting}에서, {personality if personality else ''} {protagonist}는/은 오늘도 어김없이 황당한 하루를 보내고 있었습니다. 그러다 엉뚱하게도 {key_element}를 발견하게 되죠.",
                f"세상에 {protagonist}만큼 사건 사고를 몰고 다니는 이가 있을까요? {setting}에서 그/그녀는 어처구니없게도 {key_element}와 얽히게 됩니다.",
            ],
            "판타지 🧙‍♀️": [
                f"고대 마법이 살아 숨 쉬는 {atmosphere} {setting}의 깊은 곳에서, {personality if personality else ''} {protagonist}는/은 잊혀진 {key_element}의 힘에 이끌리게 됩니다.",
                f"별빛이 쏟아지는 {atmosphere} {setting}에서, {protagonist}는/은 예언 속에 등장하는 {key_element}를 마주하며 새로운 운명을 예감합니다.",
            ],
            "미스터리 🕵️‍♂️": [
                f"{atmosphere} {setting}에 드리운 어둠 속에서, {personality if personality else ''} {protagonist}는/은 의문의 {key_element}에 대한 단서를 찾기 시작합니다. 모든 것이 미궁에 빠져들고 있습니다.",
                f"어느 날, {protagonist}는/은 {setting}에서 믿을 수 없는 {key_element}를 발견합니다. 그 순간, 주변의 모든 것이 수상해 보이기 시작합니다.",
            ],
            "로맨스 💖": [
                f"{atmosphere} {setting}의 한적한 오후, {personality if personality else ''} {protagonist}는/은 우연히 {key_element}를 통해 운명적인 인연을 만나게 됩니다.",
                f"꽃잎이 흩날리는 {atmosphere} {setting}에서, {protagonist}는/은 {key_element}와 얽히며 가슴 설레는 사랑을 시작하게 됩니다. 모든 순간이 꿈만 같습니다.",
            ],
            "스릴 😱": [
                f"피가 마를 듯한 {atmosphere} {setting}에 홀로 남겨진 {personality if personality else ''} {protagonist}는/은 정체불명의 {key_element}와 마주합니다. 이제 도망칠 곳은 없습니다.",
                f"고요한 {atmosphere} {setting}에 불길한 기운이 감돌기 시작합니다. {protagonist}의 눈앞에 나타난 {key_element}는 숨 막히는 위기의 전조였습니다.",
            ]
        },
        "전개": {
            "코믹 😂": [
                f"{protagonist}는/은 {key_element}를 가지고 이리 뛰고 저리 구르며 사건을 해결하려 했지만, 모든 시도는 실패로 돌아갔고 오히려 상황만 더 우스꽝스러워졌습니다.",
                f"상상치도 못한 기상천외한 방법으로 {protagonist}는/은 {key_element}를 다루려 했고, 그 과정에서 주변의 모든 것을 난장판으로 만들며 배꼽 빠지는 상황을 연출했습니다.",
            ],
            "판타지 🧙‍♀️": [
                f"{key_element}에 담긴 비밀을 파헤치기 위해 {protagonist}는/은 {setting} 곳곳을 탐험하며 수많은 시험과 모험을 겪습니다. 마법의 지식과 숨겨진 힘을 깨닫게 되죠.",
                f"전설 속의 {key_element}를 찾아 {protagonist}는/은 신비로운 존재들의 도움을 받거나, 때로는 강력한 적과 마주하며 영웅적인 면모를 보였습니다.",
            ],
            "미스터리 🕵️‍♂️": [
                f"{protagonist}는/은 {key_element}를 둘러싼 미스터리를 풀기 위해 {setting}의 어두운 진실을 파헤쳐 나갑니다. 드러나는 사실들은 예상보다 훨씬 충격적이었습니다.",
                f"단서들을 조합하고 추리하며 {protagonist}는/은 {key_element}와 관련된 음모의 핵심에 다가섭니다. 한 발짝 한 발짝 진실에 가까워질수록 위험은 더욱 커졌습니다.",
            ],
            "로맨스 💖": [
                f"{protagonist}는/은 {key_element} 덕분에 맺어진 인연과 {setting}에서 설레는 시간들을 보냅니다. 서로를 알아가며 특별한 감정을 키워나가죠.",
                f"{key_element}로 인해 두 사람은 {setting} 곳곳에서 우연히 만나게 되고, 여러 사건을 함께 겪으며 자연스럽게 사랑에 빠져듭니다.",
            ],
            "스릴 😱": [
                f"{key_element}에 쫓기거나 그것의 저주에 갇힌 {protagonist}는/은 {setting}을 벗어나려 필사적으로 노력합니다. 한시도 마음을 놓을 수 없는 긴장감이 계속됩니다.",
                f"{protagonist}는/은 {key_element}가 드리운 위협 속에서 생존하기 위한 지독한 사투를 벌입니다. 숨어든 곳마다 {key_element}의 그림자가 덮쳐옵니다.",
            ]
        },
        "위기": {
            "코믹 😂": [
                f"하지만 상황은 꼬일 대로 꼬여 {protagonist}는/은 {key_element} 때문에 사상 초유의 대형 사고를 치고 말았고, 이제 모든 이들이 그/그녀를 이상한 눈으로 바라봅니다.",
                f"{protagonist}는/은 {key_element}로 인해 예상치 못한 함정에 빠져 버렸고, 여기서 벗어나기 위한 해법은 오직 더 큰 바보짓 뿐인 것 같습니다.",
            ],
            "판타지 🧙‍♀️": [
                f"거대한 악의 세력이 {key_element}를 노리고 {setting}을 침공해왔습니다. {protagonist}는/은 이 모든 운명에 맞서야 하는 절체절명의 위기에 놓입니다.",
                f"{key_element}가 폭주하거나 예상치 못한 부작용을 일으키며 {protagonist}는/은 감당할 수 없는 시련에 직면합니다. 이제 세상은 멸망의 위기에 처했습니다.",
            ],
            "미스터리 🕵️‍♂️": [
                f"진실에 너무 가까이 다가간 {protagonist}는/은 {key_element}의 진짜 주인을 알게 되면서 예상치 못한 인물에게 위협을 받게 됩니다. 목숨이 위태롭습니다.",
                f"{protagonist}가 {key_element}를 파헤치려 할수록, {setting}은 더욱 혼란에 빠져들고, 주변 사람들은 하나둘 사라지거나 수상하게 행동하기 시작합니다.",
            ],
            "로맨스 💖": [
                f"{protagonist}와/과 사랑하는 사람 사이에 {key_element}로 인한 오해가 생겨나고, 관계는 최악의 상황으로 치닫습니다. 이대로 사랑이 끝날 수도 있습니다.",
                f"행복했던 순간도 잠시, {key_element}가 원인이 되어 예상치 못한 장벽이 두 사람을 가로막습니다. {setting}을 떠나야 할지도 모르는 상황에 직면합니다.",
            ],
            "스릴 😱": [
                f"{key_element}가 {protagonist}를 벼랑 끝으로 몰아붙입니다. 탈출구는 없으며, {setting}의 어두운 그림자는 {protagonist}의 숨통을 조여옵니다. 이제는 마지막 싸움입니다.",
                f"점점 미쳐가는 {key_element}의 존재 앞에서 {protagonist}는/은 이성이 마비되는 공포를 느낍니다. 이제 아무도 믿을 수 없으며, 모든 것이 함정인 듯합니다.",
            ]
        },
        "절정": {
            "코믹 😂": [
                f"웃음과 눈물, 그리고 실소를 유발하는 대소동 끝에, {protagonist}는/은 어쩌다 보니 {key_element}를 (아주 기상천외한 방식으로) 사용해 상황을 더욱 복잡하게 만든 후 해결 아닌 해결을 했습니다!",
                f"모든 오해가 절정에 달했을 때, {protagonist}의 허당미가 폭발하며 {key_element}를 이용해 오히려 상황을 더 엉망진창으로 만든 후, 의도치 않게 해피엔딩이 되어버렸습니다!",
            ],
            "판타지 🧙‍♀️": [
                f"결단의 순간, {protagonist}는/은 {key_element}에 담긴 진정한 힘을 각성하고, {setting}의 운명을 바꿀 최후의 마법을 시전합니다! 모든 것이 {protagonist}의 손에 달렸습니다.",
                f"빛과 어둠의 대결 속에서 {protagonist}는/은 {key_element}를 이용해 전설적인 존재와 맞서 싸웁니다. {setting}에 희망의 빛이 스며들기 시작합니다.",
            ],
            "미스터리 🕵️‍♂️": [
                f"모든 퍼즐 조각이 맞춰지고, {protagonist}는/은 {key_element}를 이용해 {setting}에 감춰진 거대한 진실을 세상에 폭로합니다! 충격적인 반전이 기다리고 있습니다.",
                f"범인/원흉과의 최종 대면에서, {protagonist}는/은 {key_element}에 얽힌 모든 의문을 풀고, {setting}을 다시 평화롭게 만듭니다. 하지만 그 대가는 컸습니다.",
            ],
            "로맨스 💖": [
                f"오해와 시련을 넘어, {protagonist}는/은 {key_element}를 통해 진정한 사랑의 의미를 깨닫고, 잃어버릴 뻔했던 인연과 다시 만나 영원한 사랑을 맹세합니다!",
                f"서로의 진심을 확인한 {protagonist}와 사랑하는 이/사람은 {key_element}의 도움으로 모든 장애물을 극복하고, {setting}의 가장 아름다운 순간을 함께합니다.",
            ],
            "스릴 😱": [
                f"숨 막히는 추격 끝에, {protagonist}는/은 {key_element}와 최후의 일전을 벌입니다. 생사를 건 처절한 싸움 끝에 모든 것이 결정됩니다!",
                f"희미한 불빛 속에서 {protagonist}는/은 {key_element}의 정체를 밝히지만, 그 순간 더 큰 공포가 {setting}을 덮칩니다. 이 모든 것이 거대한 함정이었습니다!",
            ]
        },
        "결말": {
            "코믹 😂": [
                f"그리하여 {personality if personality else ''} {protagonist}는/은 {setting}의 전설적인 바보(?) 영웅이 되었고, {key_element}는 박물관에 전시되어 사람들에게 끝없는 웃음을 선사했다고 합니다.",
                f"모든 사건이 해결된 후, {protagonist}는/은 {key_element}를 들고 {setting}을 떠났습니다. 하지만 그/그녀가 가는 곳마다 또 다른 대형 사고가 터졌다는 소문이... 메데타시, 메데타시!",
            ],
            "판타지 🧙‍♀️": [
                f"{protagonist}의 용기로 {setting}에는 새로운 평화와 번영이 찾아왔습니다. {key_element}는 대대손손 이어져 내려오며 영원한 희망의 상징이 되었습니다.",
                f"오랜 여정 끝에 {protagonist}는/은 {key_element}와 함께 고향인 {setting}으로 돌아와 모두의 축복을 받습니다. 이야기는 해피엔딩으로 마무리되고, 새로운 시대가 열렸습니다.",
            ],
            "미스터리 🕵️‍♂️": [
                f"결국 {protagonist}는/은 {key_element}를 둘러싼 미스터리를 완벽하게 해결했지만, 그 진실은 너무나도 충격적이어서 {setting}에는 영원히 잊히지 않을 그림자를 드리웠습니다.",
                f"사건은 종결되었지만, {protagonist}는/은 {key_element}에 얽힌 또 다른 의문을 품고 {setting}의 어딘가로 사라졌습니다. 진정한 미스터리는 지금부터 시작될지도 모릅니다.",
            ],
            "로맨스 💖": [
                f"{protagonist}와 사랑하는 이는 {key_element}가 가져다준 행복 속에서 {setting}의 아름다운 배경을 뒤로 하고 영원히 함께하게 됩니다. 그들의 사랑은 모두의 부러움을 삽니다.",
                f"모든 어려움을 이겨낸 {protagonist}와 그/그녀의 연인은 {key_element}의 축복 아래 {setting}에서 가장 빛나는 순간을 맞이합니다. 이야기는 영원한 사랑의 전설로 남게 됩니다.",
            ],
            "스릴 😱": [
                f"가까스로 {key_element}의 위협에서 벗어난 {protagonist}는/은 상처뿐인 몸으로 {setting}을 떠났습니다. 하지만 그날의 악몽은 영원히 {protagonist}의 심장에 남게 될 것입니다.",
                f"공포의 밤이 지나고 {setting}에는 다시 해가 떠올랐지만, {key_element}로 인한 상흔은 영원히 지워지지 않았습니다. {protagonist}는/은 다음 위기에 대비하며 밤늦게까지 경계를 늦추지 않았습니다.",
            ]
        }
    }

    # 이야기 제목 생성 (주요 키워드와 장르 기반)
    titles = {
        "코믹 😂": [f"좌충우돌 {protagonist}의 {key_element} 대소동", f"{setting}의 웃픈 전설, {protagonist}와 {key_element}", f"엉뚱 발랄 {protagonist}의 코믹 어드벤처"],
        "판타지 🧙‍♀️": [f"{setting}에 피어난 {key_element}의 전설", f"{protagonist}와 마법의 {key_element}", f"별빛 아래 {setting}의 숨겨진 비밀"],
        "미스터리 🕵️‍♂️": [f"{key_element}와 {protagonist}의 위험한 추리", f"{setting}의 그림자: 사라진 {key_element}의 미스터리", f"어둠 속 {setting}에서 펼쳐진 {protagonist}의 비밀스러운 여정"],
        "로맨스 💖": [f"{setting}에서 만난 {key_element} 같은 사랑", f"{protagonist}와 {key_element}의 운명적인 재회", f"사랑의 마법, {protagonist}와 {key_element}가 엮어가는 이야기"],
        "스릴 😱": [f"공포의 {setting}: {protagonist}를 쫓는 {key_element}", f"탈출! {key_element}가 잠든 {setting}의 밤", f"숨 막히는 {setting}의 추격전, {protagonist}의 최후의 생존기"],
    }
    story_title = random.choice(titles[genre])

    # 각 플롯 단계에서 문장 선택
    full_story = []
    full_story.append(random.choice(story_templates["발단"][genre]))
    full_story.append(random.choice(story_templates["전개"][genre]))
    full_story.append(random.choice(story_templates["위기"][genre]))
    full_story.append(random.choice(story_templates["절정"][genre]))
    full_story.append(random.choice(story_templates["결말"][genre]))

    return story_title, "\n\n".join(full_story)

# --- 4. '이야기 만들기' 버튼 ---
st.write("---")
# 버튼 클릭 시 CSS 업데이트 (전역적으로 바로 반영되도록)
if st.button("✨ 이야기가 만들어지는 마법! ✨", key="generate_btn"):
    
    # 로딩 메시지 다이나믹하게 표시
    placeholder = st.empty()
    random_loading_message = random.choice(current_theme["loading_messages"])
    placeholder.info(f"💫 {random_loading_message} 💫")
    time.sleep(random.uniform(1.5, 2.5)) # 생성 시간 시뮬레이션

    # 사용자 입력에 따라 이야기 생성
    title, story_text = generate_story_v3(
        protagonist, 
        protagonist_personality, 
        setting, 
        setting_atmosphere, 
        key_element, 
        selected_genre
    )
    
    placeholder.empty() # 로딩 메시지 지우기

    # 배경 이모티콘 추가 (장르에 따라)
    st.markdown(f"<div style='text-align: center; font-size: 40px; margin-bottom: 20px;'>{current_theme['background_emojis']}</div>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align: center; color: {current_theme['secondary_color']}; font-size: 35px;'>{title}</h3>", unsafe_allow_html=True)
    
    # 이야기 본문 출력
    st.markdown("<div class='story-output-box'><span class='story-text sparkle'>%s</span></div>" % story_text, unsafe_allow_html=True)
    
    # 🎉 화려한 효과 🎉
    st.balloons()
    if selected_genre == "판타지 🧙‍♀️":
        st.snow()
    elif selected_genre == "로맨스 💖":
        st.write("") # 공간 확보용
    elif selected_genre == "코믹 😂":
        st.info("🤣 피식하셨나요? 🤣") # 코믹용 메시지
    
    st.success("🌟 당신의 상상력이 새로운 이야기를 만들었어요! 🌟")

st.write("---")

# --- 5. 게스트 계정 안내 ---
st.markdown("""
    <div style="background-color:{}; padding:15px; border-radius:10px; margin-top:30px;">
        <p style="font-size:16px; font-weight:bold; color:{};">
        🎉 아직 게스트로 이용 중이신가요? 🎉
        </p>
        <p style="font-size:15px; color:{};">
        이렇게 재미있는 '내맘대로 이야기 생성기'처럼, 나만의 창의적인 프로젝트를 만들고 
        나중에 저장하거나 친구들에게 자랑하고 싶으시다면,
        간단하게 회원가입을 해보시는 건 어떠세요? 
        당신의 멋진 아이디어들이 더욱 빛날 수 있도록 도와드릴게요! ✨
        </p>
    </div>
    """.format(current_theme['text_color'], current_theme['secondary_color'], current_theme['primary_color']), unsafe_allow_html=True)
