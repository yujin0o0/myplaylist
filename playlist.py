import streamlit as st
from PIL import Image, ImageDraw, ImageFont # ImageFont 추가
import io # 이미지 저장에 필요

# --- 1. 페이지 설정 및 제목 ---
st.set_page_config(layout="wide", page_title="🌟 나의 드림 코디네이터 (더미 이미지 버전) 🌟", icon="👗")

st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #FF69B4; /* 핑크색으로 화려하게! */
    }
    .stSelectbox label, .stRadio label {
        font-size: 18px;
        font-weight: bold;
        color: #4CAF50; /* 초록색으로 포인트를! */
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='big-font'>✨ 장소 맞춤! 나만의 코디를 완성해봐! (더미 이미지로 체험!) ✨</p>", unsafe_allow_html=True)
st.write("---")

# --- 2. 이미지 에셋 생성 함수 (이제 파일 준비는 NO!) ---
# 이제 모든 이미지를 코드에서 직접 그립니다.
# 실제 캐릭터 꾸미기 게임을 만들 때는 이 부분을 여러분이 직접 그리신 PNG 파일로 교체하시면 됩니다.

# 이미지의 기본 크기를 설정합니다.
IMG_WIDTH = 500
IMG_HEIGHT = 700

# 배경 이미지 생성 함수
def create_dummy_background(name):
    img = Image.new("RGBA", (IMG_WIDTH + 200, IMG_HEIGHT + 100), "lightgray") # 배경은 좀 더 크게
    draw = ImageDraw.Draw(img)
    color = "skyblue" if "해변" in name else \
            "forestgreen" if "숲" in name else \
            "darkslategray" if "도시" in name else \
            "tan" if "카페" in name else \
            "darkviolet"
    draw.rectangle([0, 0, img.width, img.height], fill=color)
    try:
        font = ImageFont.truetype("arial.ttf", 30) # 폰트가 시스템에 없으면 오류날 수 있음
    except IOError:
        font = ImageFont.load_default() # 기본 폰트 사용
    draw.text((50, 50), name, fill="white", font=font)
    return img

# 캐릭터 몸통 이미지 생성 함수
def create_dummy_character_base(name):
    img = Image.new("RGBA", (IMG_WIDTH, IMG_HEIGHT), (0, 0, 0, 0)) # 투명 배경
    draw = ImageDraw.Draw(img)
    # 간단한 몸통 그림
    body_color = "peachpuff"
    if "남" in name:
        body_color = "peru"
        draw.ellipse([IMG_WIDTH*0.3, IMG_HEIGHT*0.1, IMG_WIDTH*0.7, IMG_HEIGHT*0.3], fill=body_color) # 머리
        draw.rectangle([IMG_WIDTH*0.35, IMG_HEIGHT*0.3, IMG_WIDTH*0.65, IMG_HEIGHT*0.7], fill=body_color) # 몸통
    else:
        draw.ellipse([IMG_WIDTH*0.3, IMG_HEIGHT*0.1, IMG_WIDTH*0.7, IMG_HEIGHT*0.3], fill=body_color) # 머리
        draw.rectangle([IMG_WIDTH*0.35, IMG_HEIGHT*0.3, IMG_WIDTH*0.65, IMG_HEIGHT*0.6], fill=body_color) # 몸통
        draw.polygon([(IMG_WIDTH*0.35, IMG_HEIGHT*0.6), (IMG_WIDTH*0.65, IMG_HEIGHT*0.6), (IMG_WIDTH*0.5, IMG_HEIGHT*0.75)], fill=body_color) # 하체
    
    # 텍스트 오버레이
    try:
        font = ImageFont.truetype("arial.ttf", 25)
    except IOError:
        font = ImageFont.load_default()
    draw.text((IMG_WIDTH*0.35, IMG_HEIGHT*0.45), name, fill="darkblue", font=font)
    return img

# 의상 아이템 생성 함수
def create_dummy_clothing_item(category_name, item_name):
    img = Image.new("RGBA", (IMG_WIDTH, IMG_HEIGHT), (0, 0, 0, 0)) # 투명 배경
    draw = ImageDraw.Draw(img)
    color = "red"
    if category_name == "상의":
        color = "skyblue" if "티셔츠" in item_name else "pink" if "블라우스" in item_name else "orange"
        draw.rectangle([IMG_WIDTH*0.3, IMG_HEIGHT*0.25, IMG_WIDTH*0.7, IMG_HEIGHT*0.55], fill=color)
        if "니트" in item_name:
             draw.ellipse([IMG_WIDTH*0.4, IMG_HEIGHT*0.28, IMG_WIDTH*0.6, IMG_HEIGHT*0.35], fill="dark"+color) # 목 부분
    elif category_name == "하의":
        color = "darkblue" if "진" in item_name else "purple" if "스커트" in item_name else "gray"
        draw.rectangle([IMG_WIDTH*0.35, IMG_HEIGHT*0.5, IMG_WIDTH*0.65, IMG_HEIGHT*0.75], fill=color)
        if "스커트" in item_name:
            draw.polygon([(IMG_WIDTH*0.35, IMG_HEIGHT*0.65), (IMG_WIDTH*0.65, IMG_HEIGHT*0.65), (IMG_WIDTH*0.5, IMG_HEIGHT*0.75)], fill=color)
    elif category_name == "신발":
        color = "brown" if "부츠" in item_name else "lightgray" if "운동화" in item_name else "gold"
        draw.rectangle([IMG_WIDTH*0.38, IMG_HEIGHT*0.75, IMG_WIDTH*0.48, IMG_HEIGHT*0.8], fill=color)
        draw.rectangle([IMG_WIDTH*0.52, IMG_HEIGHT*0.75, IMG_WIDTH*0.62, IMG_HEIGHT*0.8], fill=color)
    elif category_name == "액세서리":
        color = "yellow" if "모자" in item_name else "green" if "백" in item_name else "black"
        if "모자" in item_name:
            draw.ellipse([IMG_WIDTH*0.3, IMG_HEIGHT*0.05, IMG_WIDTH*0.7, IMG_HEIGHT*0.2], fill=color)
        elif "백" in item_name:
            draw.rectangle([IMG_WIDTH*0.6, IMG_HEIGHT*0.4, IMG_WIDTH*0.75, IMG_HEIGHT*0.55], fill=color)
        
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    draw.text((IMG_WIDTH*0.4, IMG_HEIGHT*0.6), item_name, fill="white", font=font)
    return img

# --- 2.1. 이미지 딕셔너리 구성 (함수 호출로 이미지 객체 저장) ---

# 배경 이미지 딕셔너리
BACKGROUNDS = {
    "화창한 해변": create_dummy_background("화창한 해변"),
    "고요한 숲길": create_dummy_background("고요한 숲길"),
    "활기찬 도시 거리": create_dummy_background("활기찬 도시 거리"),
    "아늑한 카페": create_dummy_background("아늑한 카페"),
    "반짝이는 파티장": create_dummy_background("반짝이는 파티장")
}

# 캐릭터 몸통 이미지 딕셔너리
CHARACTER_BASES = {
    "기본 체형 (여)": create_dummy_character_base("기본 체형 (여)"),
    "기본 체형 (남)": create_dummy_character_base("기본 체형 (남)")
    # 날씬한 체형, 건강한 체형은 더미 이미지라 큰 차이 없이 복사본으로 만듭니다.
    , "날씬한 체형": create_dummy_character_base("날씬한 체형"), 
    "건강한 체형": create_dummy_character_base("건강한 체형")
}

# 의상 아이템 딕셔너리
CLOTHING_ITEMS = {
    "상의": {
        "선택 안함": None,
        "캐주얼 티셔츠": create_dummy_clothing_item("상의", "캐주얼 티셔츠"),
        "우아한 블라우스": create_dummy_clothing_item("상의", "우아한 블라우스"),
        "따뜻한 니트": create_dummy_clothing_item("상의", "따뜻한 니트"),
        "정장 셔츠": create_dummy_clothing_item("상의", "정장 셔츠")
    },
    "하의": {
        "선택 안함": None,
        "스키니진": create_dummy_clothing_item("하의", "스키니진"),
        "A라인 스커트": create_dummy_clothing_item("하의", "A라인 스커트"),
        "슬랙스": create_dummy_clothing_item("하의", "슬랙스"),
        "반바지": create_dummy_clothing_item("하의", "반바지")
    },
    "신발": {
        "선택 안함": None,
        "운동화": create_dummy_clothing_item("신발", "운동화"),
        "하이힐": create_dummy_clothing_item("신발", "하이힐"),
        "샌들": create_dummy_clothing_item("신발", "샌들"),
        "부츠": create_dummy_clothing_item("신발", "부츠")
    },
    "액세서리": {
        "선택 안함": None,
        "볼캡": create_dummy_clothing_item("액세서리", "볼캡"),
        "크로스백": create_dummy_clothing_item("액세서리", "크로스백"),
        "선글라스": create_dummy_clothing_item("액세서리", "선글라스"),
        "목걸이": create_dummy_clothing_item("액세서리", "목걸이")
    }
}


# --- 3. 사이드바 - 설정 컨트롤 ---
with st.sidebar:
    st.header("나의 코디네이션! 👚👗")
    
    st.write("---")
    st.subheader("1. 캐릭터 선택")
    selected_base_name = st.radio("캐릭터의 기본 체형을 골라주세요!", list(CHARACTER_BASES.keys()), key="char_base")
    st.write("---")

    st.subheader("2. 장소 선택")
    selected_bg_name = st.selectbox("어떤 장소로 떠나볼까요?", list(BACKGROUNDS.keys()), key="location")
    st.write("---")

    st.subheader("3. 의상 선택")
    # 각 카테고리별로 선택 박스를 만듭니다.
    selected_clothes = {}
    for category, items in CLOTHING_ITEMS.items():
        selected_clothes[category] = st.selectbox(f"{category} 고르기", list(items.keys()), key=f"clothes_{category}")
    
    st.write("---")
    st.info("📌 **더미 이미지 가이드:** 현재는 내부에서 생성된 더미 이미지로 작동합니다. 실제 게임에서는 투명 배경의 예쁜 PNG 파일들로 교체하여 사용하세요!")

# --- 4. 캐릭터 코디 합성 로직 ---

def create_outfit_image(base_img_obj, bg_img_obj, selected_clothing_img_objs):
    try:
        # 배경 이미지 (객체 사용)
        background = bg_img_obj.convert("RGBA") 
        
        # 캐릭터 몸통 이미지 (객체 사용)
        character_base = base_img_obj.convert("RGBA")

        # 배경이 캐릭터보다 크다고 가정하고, 캐릭터를 배경 위에 적절히 배치
        # 배경을 복사하여 최종 이미지 캔버스로 사용
        final_image = background.copy() 
        
        # 캐릭터 이미지를 배경 중앙 하단에 배치 (adjust_for_base_and_clothes는 더미 이미지라서 필요 없습니다)
        # 캐릭터를 최종 이미지의 중앙 아래쪽에 배치합니다.
        char_x = (final_image.width - character_base.width) // 2
        char_y = final_image.height - character_base.height # 바닥에 붙여서

        # 캐릭터를 배경 위에 합성 (character_base의 알파 채널 활용)
        # 이 부분이 중요! character_base의 투명도를 그대로 살려서 합성
        final_image = Image.alpha_composite(final_image, Image.new("RGBA", final_image.size, (0,0,0,0))) # 투명 레이어 추가
        final_image.paste(character_base, (char_x, char_y), character_base)

        # 선택된 의상들을 순서대로 캐릭터 위에 합성 (PIL의 paste 기능은 투명한 PNG를 잘 처리합니다)
        # 각 옷 이미지도 캐릭터 몸통 이미지와 동일한 위치에 합성 (이미 더미 생성시 맞춰졌다고 가정)
        for clothing_obj in selected_clothing_img_objs:
            if clothing_obj: # '선택 안함'이 아닐 경우
                clothing_item = clothing_obj.convert("RGBA")
                final_image.paste(clothing_item, (char_x, char_y), clothing_item)

        return final_image
    except Exception as e:
        st.error(f"이미지 처리 중 오류가 발생했어요: {e}")
        st.warning("⚠️ 이미지 생성 및 합성 과정에서 문제가 발생했습니다. 브라우저를 새로고침해보거나 개발자에게 문의해주세요.")
        return None

# --- 5. 메인 화면 - 꾸미기 결과 보여주기 ---
st.subheader("짜잔! 오늘의 코디 미리보기 📸")

# 선택된 이미지 '객체' 가져오기 (경로가 아님!)
base_image_obj = CHARACTER_BASES[selected_base_name]
bg_image_obj = BACKGROUNDS[selected_bg_name]

selected_clothing_img_objs = [CLOTHING_ITEMS[cat][item_name] 
                              for cat, item_name in selected_clothes.items()]

# 이미지 합성 및 표시
outfit_image = create_outfit_image(base_image_obj, bg_image_obj, selected_clothing_img_objs)

if outfit_image:
    st.image(outfit_image, caption="✨ 당신의 멋진 코디 완성! ✨", use_column_width=True)

    # 이미지 저장 버튼 (여전히 PNG로 저장 가능)
    buf = io.BytesIO()
    outfit_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="💖 나만의 코디 저장하기 (더미 이미지)",
        data=byte_im,
        file_name="my_dummy_outfit.png",
        mime="image/png"
    )

st.write("---")
st.success("이제 당신의 상상력을 발휘해서 세상에 하나뿐인 멋진 코디를 만들어보세요! 😊")

# --- 6. 게스트 계정 안내 ---
st.markdown("""
    <div style="background-color:#FFFACD; padding:15px; border-radius:10px; margin-top:30px;">
        <p style="font-size:16px; font-weight:bold; color:#FF8C00;">
        💡 아직 게스트로 이용 중이시네요! 💡
        </p>
        <p style="font-size:15px; color:#696969;">
        나중에 직접 만드신 멋진 코디를 웹에서 저장하고, 다른 친구들과 공유하거나,
        나만의 특별한 기능들을 더 추가하고 싶으시다면,
        간단하게 회원가입을 해보시는 건 어떠세요? 
        당신의 창의력을 더 활짝 펼칠 수 있을 거예요! ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
