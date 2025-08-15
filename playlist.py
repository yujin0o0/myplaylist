import streamlit as st
import random

# --- 0. Streamlit 페이지 기본 설정 ---
st.set_page_config(layout="wide", page_title="✍️ 내맘대로 이야기 생성기 ✍️")

# --- 1. CSS 스타일링 (화려함과 재미를 동시에! ✨) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap'); /* 손글씨 폰트 */

    .main-title {
        font-family: 'Nanum Pen Script', cursive; /* 손글씨 느낌 */
        font-size: 55px !important;
        font-weight: bold;
        color: #8A2BE2; /* 파란색 보라색 계열 */
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        animation: neon 1.5s ease-in-out infinite alternate; /* 네온사인 효과 */
    }
    @keyframes neon {
        from {
            text-shadow:
                0 0 10px #fff,
                0 0 20px #fff,
                0 0 30px #fff,
                0 0 40px #FFD700, /* 황금색 빛 */
                0 0 70px #FFD700,
                0 0 80px #FFD700,
                0 0 100px #FFD700,
                0 0 150px #FFD700;
        }
        to {
            text-shadow:
                0 0 5px #fff,
                0 0 10px #fff,
                0 0 15px #fff,
                0 0 20px #8A2BE2, /* 보라색 빛 */
                0 0 35px #8A2BE2,
                0 0 40px #8A2BE2,
                0 0 50px #8A2BE2,
                0 0 75px #8A2BE2;
        }
    }
    .section-header {
        font-size: 28px !important;
        font-weight: bold;
        color: #FF69B4; /* 핫핑크 강조 */
        margin-top: 35px;
        margin-bottom: 20px;
        border-bottom: 4px dashed #FFD700; /* 황금색 점선 */
        padding-bottom: 8px;
    }
    .stTextInput > label, .stSelectbox > label, .stSlider > label {
        font-size: 20px;
        font-weight: bold;
        color: #4B0082; /* 인디고 색상 */
    }
    .stButton > button {
        background-color: #FF4500; /* 주황색 버튼 */
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
        background-color: #FF8C00; /* 오렌지색으로 호버 효과 */
        transform: translateY(-2px);
    }
    .story-output-box {
        background-color: #FFFACD; /* 밝은 노란색 배경 */
        border: 2px solid #FFC0CB; /* 연핑크 테두리 */
        border-radius: 15px;
        padding: 25px;
        margin-top: 40px;
        min-height: 300px; /* 최소 높이 */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    .story-text {
        font-family: 'Nanum Pen Script', cursive; /* 손글씨 폰트 */
        font-size: 32px;
        line-height: 1.6;
        color: #333;
    }
    .sparkle {
        animation: sparkle 1s infinite alternate;
    }
    @keyframes sparkle {
        from { opacity: 0.5; }
        to { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='main-title'>✍️✨ 내맘대로 이야기 생성기 ✨✍️</p>", unsafe_allow_html=True)
st.write("당신이 던지는 단어들이 환상적인 이야기가 되는 마법을 경험하세요! ✨")
st.write("---")

# --- 2. 이야기의 재료 입력 받기 ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<p class='section-header'>1. 이야기의 주인공을 정해봐! 🎭</p>", unsafe_allow_html=True)
    protagonist = st.text_input("누가 이야기의 주인공인가요?", value="용감한 탐험가 레오", help="예: 신비한 마법사, 개구쟁이 요정, 외로운 로봇")
    
    st.markdown("<p class='section-header'>2. 이야기가 펼쳐질 곳은? 🗺️</p>", unsafe_allow_html=True)
    setting = st.text_input("어떤 배경에서 이야기가 시작될까요?", value="신비로운 숲 속 깊은 동굴", help="예: 미래 도시의 높은 빌딩, 바다 밑 고대 유적, 꿈 속의 과자 집")
    
with col2:
    st.markdown("<p class='section-header'>3. 이야기에 어떤 일이 벌어질까? ❓</p>", unsafe_allow_html=True)
    key_event = st.text_input("이야기의 중요한 사건이나 위기는 무엇인가요?", value="잠들어 있던 고대 용을 깨우는 일", help="예: 예상치 못한 보물을 발견, 이상한 저주에 걸림, 시간 여행을 시작함")

    st.markdown("<p class='section-header'>4. 비밀 무기? 핵심 아이템! 💎</p>", unsafe_allow_html=True)
    magic_item = st.text_input("이야기를 해결할 핵심 아이템은 무엇인가요?", value="반짝이는 마법 거울", help="예: 오래된 지팡이, 노래하는 검, 시간 되돌리는 시계")
    
    st.markdown("<p class='section-header'>5. 이야기의 분위기는? 😄</p>", unsafe_allow_html=True)
    mood = st.select_slider(
        "이야기의 분위기를 선택하세요:",
        options=["😂 코믹", "🤩 환상", "🤫 미스터리", "💘 로맨스", "😱 스릴"],
        value="🤩 환상"
    )

st.write("---")

# --- 3. 이야기 생성 함수 (마법의 공식!) ---
def generate_story(protagonist, setting, key_event, magic_item, mood):
    story_parts = []

    # 오프닝 (mood에 따라 다양한 시작!)
    openings = {
        "😂 코믹": [
            f"옛날 옛적, 세상에 {protagonist} 만큼 어리바리한 이는 없었습니다. 어느 날 {setting}에 도착한 그/그녀는 어처구니없게도 {key_event} 벌였고...",
            f"{protagonist}는 매일 아침 {setting}에서 이상한 춤을 추는 것으로 하루를 시작했습니다. 그러던 중 {key_event} 라는 기상천외한 소식을 듣게 되는데...",
        ],
        "🤩 환상": [
            f"별들이 속삭이는 밤, {setting}에서 {protagonist}는 오래된 예언의 조각을 발견했습니다. 그리고 예언은 바로 {key_event} 를 가리키고 있었죠.",
            f"{protagonist}는 요정과 마법이 살아 숨쉬는 {setting}에 살고 있었습니다. 하지만 평화는 오래가지 못했으니, 전설 속의 {key_event} 가 현실이 되어 나타난 것이었습니다!",
        ],
        "🤫 미스터리": [
            f"안개가 자욱한 {setting}, 아무도 없는 그곳에 {protagonist}의 발걸음만이 울려 퍼졌습니다. 그/그녀는 오랫동안 잊혀진 {key_event} 의 진실을 파헤치기 위해 온 것이었죠.",
            f"{protagonist}는 기이한 꿈에 시달리다 {setting}에 숨겨진 비밀을 찾기 시작했습니다. 그 비밀은 바로 {key_event} 와 깊이 연관되어 있었습니다.",
        ],
        "💘 로맨스": [
            f"{protagonist}는 {setting}에서 우연히 운명적인 상대를 만났습니다. 그/그녀는 {key_event} 를 겪으며 점차 서로에게 마음을 열기 시작했습니다.",
            f"아름다운 {setting}에서 {protagonist}의 이야기는 시작됩니다. 잔잔했던 일상에 파동을 일으킨 것은 다름 아닌 {key_event} 와 함께 찾아온 새로운 인연이었습니다.",
        ],
        "😱 스릴": [
            f"어둠이 깔린 {setting}, {protagonist}는 심장을 조여오는 공포를 느꼈습니다. 바로 그 순간 {key_event} 가 시작되었고, 이제 남은 건 살아남는 것 뿐...",
            f"{protagonist}는 소름 돋는 {setting}에서 깨어났습니다. 마지막으로 기억나는 건 {key_event} 뿐, 과연 그/그녀는 이 미스터리한 상황에서 벗어날 수 있을까요?",
        ]
    }
    story_parts.append(random.choice(openings[mood]))

    # 전개 (조금 더 깊이 파고들기)
    developments = [
        f"이를 해결하기 위해 {protagonist}는 수많은 난관과 마주쳤고, {magic_item} 의 숨겨진 힘을 깨닫게 됩니다.",
        f"알고 보니 {key_event} 뒤에는 거대한 음모가 숨겨져 있었고, {protagonist}는 {magic_item} 의 도움으로 그 음모의 실마리를 찾기 시작했습니다.",
        f"{protagonist}는 {setting} 구석구석을 탐색하며 {key_event} 에 대한 단서를 모았습니다. 결정적인 순간, {magic_item} 이 뜻밖의 도움을 주었습니다.",
        f"위기의 순간, {protagonist}는 우연히 발견한 {magic_item} 이 사실은 {key_event} 를 해결할 열쇠라는 것을 알게 됩니다.",
        f"모두가 불가능하다고 했지만, {protagonist}는 {magic_item} 하나만을 믿고 {key_event} 의 원인이 된 곳으로 향했습니다.",
        f"사랑하는 이/소중한 것을 지키기 위해 {protagonist}는 {key_event} 라는 거대한 시련에 맞서 싸워야 했습니다. 다행히 {magic_item} 이 그/그녀의 곁에 있었습니다."
    ]
    story_parts.append(random.choice(developments))

    # 클라이맥스 (점점 고조되는 분위기)
    climaxes = [
        f"마침내 {key_event} 의 원흉과 마주한 {protagonist}는 {magic_item} 이 가진 최후의 힘을 발휘하여 모든 것을 역전시켰습니다!",
        f"{setting}을 뒤흔드는 거대한 소용돌이 속에서 {protagonist}는 {magic_item} 을 사용해 {key_event} 를 영원히 잠재웠습니다.",
        f"숨 막히는 대치 끝에, {protagonist}는 {magic_item} 의 빛으로 {key_event} 를 일으킨 자들의 어둠을 물리쳤습니다.",
        f"모든 수수께끼가 풀리고, {protagonist}는 {magic_item} 으로 {key_event} 와 관련된 운명을 바꾸었습니다.",
        f"최후의 선택의 순간, {protagonist}는 {magic_item} 이 이끄는 대로 {key_event} 에 뛰어들었고, 기적처럼 성공했습니다!"
    ]
    story_parts.append(random.choice(climaxes))

    # 결말 (새로운 시작 또는 평화)
    endings = {
        "😂 코믹": [
            f"그리고 {protagonist}는 {magic_item} 과 함께 다시 {setting}으로 돌아와, 더 이상 이상한 춤을 추지 않게 되었... 지는 않고 더 화려하게 췄다고 합니다.😂",
            f"결국 {protagonist}는 {magic_item} 덕분에 엉망진창인 상황을 수습하고, 배고파서 라면을 끓여 먹으며 평범한 일상으로 돌아왔습니다. 메데타시 메데타시!",
        ],
        "🤩 환상": [
            f"세상은 {protagonist}와 {magic_item} 의 이야기로 빛났고, {setting}은 영원히 평화를 되찾았습니다. 새로운 전설이 시작된 것이죠.",
            f"{protagonist}는 {magic_item} 의 힘으로 {setting}을 더욱 아름다운 곳으로 만들고, 영원히 행복하게 살았답니다. 오래오래도록 기억될 이야기가 되었습니다.",
        ],
        "🤫 미스터리": [
            f"하지만 {key_event} 의 그림자는 완전히 사라지지 않았습니다. {protagonist}는 {magic_item} 을 들고 다음 미스터리를 찾아 {setting} 너머로 사라졌습니다.",
            f"모든 것이 해결된 듯 보였지만, {magic_item} 은 여전히 풀리지 않는 의문을 남겼습니다. {protagonist}는 {setting}의 밤하늘을 바라보며 깊은 생각에 잠겼습니다.",
        ],
        "💘 로맨스": [
            f"{protagonist}는 {magic_item} 이 맺어준 인연과 함께 {setting}에서 새로운 사랑을 꽃피웠습니다. 그들의 사랑은 영원히 지속될 전설이 되었습니다.",
            f"{key_event} 를 극복한 {protagonist}는 {magic_item} 과 함께 영원한 사랑을 약속하며 {setting}에서 행복한 날들을 보냈습니다. 모두가 부러워하는 커플이 탄생했습니다!",
        ],
        "😱 스릴": [
            f"{protagonist}는 간신히 {key_event} 에서 살아남았지만, {magic_item} 은 사라지고 없었습니다. {setting}은 다시금 평화를 찾은 듯 보였지만, 그날의 악몽은 {protagonist}를 평생 따라다녔습니다.",
            f"긴 싸움이 끝나고 {protagonist}는 {magic_item} 을 꼭 쥐고 {setting}을 떠났습니다. 하지만 언제 다시 {key_event} 같은 일이 일어날지 아무도 알 수 없었습니다. 이야기는 계속된다...",
        ]
    }
    story_parts.append(random.choice(endings[mood]))

    return " ".join(story_parts)

# --- 4. '이야기 만들기' 버튼 ---
st.write("---")
if st.button("✨ 이야기가 만들어지는 마법! ✨", key="generate_btn"):
    with st.spinner('이야기가 스르륵 만들어지고 있어요... 잠시만 기다려 주세요!'):
        # 사용자 입력에 따라 이야기 생성
        story = generate_story(protagonist, setting, key_event, magic_item, mood)
        
        st.markdown("<p class='story-output-box'><span class='story-text sparkle'>%s</span></p>" % story, unsafe_allow_html=True)
        st.balloons() # 이야기가 만들어질 때마다 풍선 터트리기!
        st.snow() # 눈도 펑펑 내리기!

st.write("---")
st.success("🌟 당신의 상상력이 새로운 이야기를 만들었어요! 🌟")

# --- 5. 게스트 계정 안내 ---
st.markdown("""
    <div style="background-color:#E6E6FA; padding:15px; border-radius:10px; margin-top:30px;">
        <p style="font-size:16px; font-weight:bold; color:#6A5ACD;">
        🎉 잠깐! 혹시 아직 게스트이신가요? 🎉
        </p>
        <p style="font-size:15px; color:#483D8B;">
        이렇게 재미있는 '내맘대로 이야기 생성기'처럼, 나만의 창의적인 프로젝트를 만들고 
        나중에 저장하거나 친구들에게 자랑하고 싶으시다면,
        간단하게 회원가입을 해보시는 건 어떠세요? 
        당신의 멋진 아이디어들이 더욱 빛날 수 있도록 도와드릴게요! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
