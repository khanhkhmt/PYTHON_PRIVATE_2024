import streamlit as st
import random

# Tiêu đề chính
st.title("Chúc Mừng Ngày Quốc Tế Phụ Nữ 8/3")

# Lời chúc mặc định
st.write("Chúc tất cả các chị em một ngày 8/3 tràn đầy niềm vui và hạnh phúc!")
st.write("Cảm ơn các bạn đã luôn tỏa sáng và truyền cảm hứng cho mọi người xung quanh.")

# Hiển thị hình ảnh (thay thế bằng URL hoặc tên file ảnh cục bộ)
st.image("anh1.jfif", 
         caption="Hoa dành tặng ngày 8/3")

# Danh sách lời chúc ngẫu nhiên
wishes = [
    "Chúc bạn luôn xinh đẹp, rạng rỡ như những bông hoa tươi thắm!",
    "Mong bạn có một ngày 8/3 thật đặc biệt và ý nghĩa!",
    "Chúc bạn luôn mạnh mẽ, tự tin và thành công trong mọi điều!",
    "Cảm ơn bạn vì đã là một người phụ nữ tuyệt vời!",
    "Chúc bạn một ngày 8/3 tràn đầy yêu thương và hạnh phúc!"
]

# Nút để nhận lời chúc ngẫu nhiên
if st.button("Nhấn để nhận lời chúc ngẫu nhiên"):
    st.write(random.choice(wishes))

# Ô nhập tên để cá nhân hóa lời chúc
name = st.text_input("Nhập tên người bạn muốn chúc mừng:")
if name:
    st.write(f"Chúc {name} một ngày 8/3 thật rực rỡ và đáng nhớ!")

# Hiệu ứng nhấp nháy cho tiêu đề (tùy chọn)
st.markdown("""
<style>
.blink {
    animation: blinker 1s linear infinite;
}
@keyframes blinker {
    50% { opacity: 0; }
}
</style>
<h2 class="blink">Hạnh Phúc Mãi Mãi!</h2>
""", unsafe_allow_html=True)

# Thêm ảnh nền (thay thế bằng URL hoặc tên file ảnh cục bộ)
background_image_url = "anh.jfif"  # Thay bằng URL ảnh của bạn
st.markdown(f"""
<style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
</style>
""", unsafe_allow_html=True)