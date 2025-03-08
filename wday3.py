import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Chúc Mừng 8/3",
    page_icon="🌸",
    layout="centered",
)

# Custom CSS for background and styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://24hstore.vn/upload_images/images/hinh-nen-mau-hong/hinh-nen-mau-hong-cute_(4).jpg");
        background-size: cover;
    }
    .title {
        color: #ff69b4;
        font-size: 48px;
        text-align: center;
        text-shadow: 2px 2px 4px #ffffff;
    }
    .poem {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Main content
st.markdown('<h1 class="title">🌸 Happy International Women\'s Day 🌸</h1>', unsafe_allow_html=True)

# Add flowers animation
st.markdown(
    """
    <div style="text-align: center">
        <p>🌹🌹🌹🌹🌹🌹🌹</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Poem container
st.markdown(
    """
    <div class="poem">
        <h3 style="text-align:center; color:#e75480">Gửi đến những người phụ nữ tuyệt vời</h3>
        <p style="text-align:center; font-style:italic">
        Ngày 8/3 đến rồi đây<br>
        Chúc cho tất cả những người phụ nữ xinh tươi<br>
        Luôn xinh đẹp rạng ngời tỏa nắng<br>
        Hạnh phúc ngập tràn, ấm áp quanh năm!<br><br>
        
        Cảm ơn những hy sinh thầm lặng
        Cảm ơn tình yêu dịu ngọt đong đầy
        Bạn xứng đáng được trân trọng
        Hôm nay và cả những ngày sau này!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# Add images
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.image("https://www.upsieutoc.com/images/2020/03/08/hoa-8-3.png", caption="Hoa tươi sắc thắm")

# with col2:
#     st.image("https://img.upanh.tv/2023/03/07/8-3-2.png", caption="Ngày của bạn")

# with col3:
#     st.image("https://img.upanh.tv/2023/03/07/8-3-3.jpg", caption="Trao yêu thương")

# Add interactive button
# if st.button("🎁 Nhấn để nhận quà"):
#     st.balloons()
#     st.success("🎀 Bạn xứng đáng nhận được: Một bó hoa hồng, một hộp chocolate và vô số cái ôm ấm áp!")
    # st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
# Add interactive button

if st.button("🌸 Nhận Hoa May Mắn 🌸", key="flower_button"):
    # Hiệu ứng hoa rơi
    st.markdown("""
    <script>
    function createFlower() {
        const flower = document.createElement('div');
        flower.innerHTML = '🌸';
        flower.style.left = Math.random() * 100 + 'vw';
        flower.style.animationDuration = Math.random() * 3 + 2 + 's';
        flower.classList.add('petal');
        document.body.appendChild(flower);
        
        setTimeout(() => { flower.remove() }, 5000);
    }
    setInterval(createFlower, 300);
    </script>
    """, unsafe_allow_html=True)
    
    st.success("💐 Bạn nhận được: 1000 bông hồng tươi thắm, nụ cười rạng rỡ và những lời yêu thương ngọt ngào!")
    
    # Hiển thị ảnh hoa nở
    st.image("https://i.pinimg.com/originals/6b/6d/9c/6b6d9c23f3c1d3eb417a9e6094535b2b.gif", 
             caption="Hoa nở rộ dành cho bạn")

# Footer
st.markdown(
    """
    <div style="text-align: center; margin-top: 30px; color: #ffffff">
        <p>💖 Made with Love | 8/3/2025 💖</p>
        <p>Bạn là điều tuyệt vời nhất thế gian!</p>
    </div>
    """,
    unsafe_allow_html=True
)
