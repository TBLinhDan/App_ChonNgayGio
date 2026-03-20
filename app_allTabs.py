import streamlit as st
from tabs import DoiLich, nhanmenh

st.title("NGÀY GIỜ CÁT/HUNG")
#tab1, tab2, tab3 = st.tabs(["**KHÍ VẬN NGÀY/GIỜ**","**NHÂN MỆNH**","**DỊCH LÝ & TIÊU CHÍ**"])

# Đoạn mã CSS nâng cao để đổi màu từng Tab theo thứ tự
st.markdown("""
    <style>
    /* 1. Phóng to chữ và làm đậm cho tất cả các Tab */
    button[data-baseweb="tab"] p {
        font-size: 21px !important;
        font-weight: bold !important;
    }

    /* 2. Màu sắc riêng cho Tab 1 (KHÍ VẬN) - Màu Xanh Lá */
    button[data-baseweb="tab"]:nth-child(1) p {
        color: #2E7D32 !important;
    }

    /* 3. Màu sắc riêng cho Tab 2 (NHÂN MỆNH) - Màu Đỏ Đậm */
    button[data-baseweb="tab"]:nth-child(2) p {
        color: #C62828 !important;
    }

    /* 4. Màu sắc riêng cho Tab 3 (DỊCH LÝ) - Màu Xanh Dương */
    button[data-baseweb="tab"]:nth-child(3) p {
        color: #1565C0 !important;
    }

    /* 5. Hiệu ứng khi Tab được chọn (Highlight) */
    button[data-baseweb="tab"][aria-selected="true"] {
        background-color: #f0f2f6 !important; /* Đổi màu nền nhẹ khi chọn */
        border-bottom: 3px solid brown !important; /* Đường gạch chân màu nâu */
    }
    </style>
    """, unsafe_allow_html=True)

# Khởi tạo các Tab
tab1, tab2, tab3 = st.tabs(["**KHÍ VẬN**","**NHÂN MỆNH**","**DỊCH LÝ**"])


with tab1:
    DoiLich.DoiLich()
    st.markdown('<span style="color: blue; font-size: 20px;">**XEM XÉT KHÍ VẬN NGÀY HÔM NAY**</span>', unsafe_allow_html=True)
    DoiLich.cosodichly()

with tab2:
    #st.subheader(f'**NGÀY/GIỜ TỐT ĐỐI VỚI NHÂN MỆNH**')
    #st.subheader("👤 Xem vận hạn cá nhân")
    #st.markdown('<span style="color: darkred; font-size: 20px;">**NHÂN MỆNH với NGÀY/GIỜ**</span>', unsafe_allow_html=True)
    
    #nhanmenh.he_thong_kiem_duyet_ngay_toan_dien(ngay_thang_nam, thang_canchi, nam_canchi, content, lich_tong_hop, ngay_tot)
    nhanmenh.NhanMenh_trong_Thoivan()

with tab3:
    #st.info('''Đổi Dương Lịch sang Kim Cang CAN CHI Lịch''')

    st.markdown('<span style="color: darkblue; font-size: 22px;">**TIÊU CHÍ CHỌN NGÀY/GIỜ**</span>', unsafe_allow_html=True)
    #DoiLich.coso_phuongphaptinh()
    DoiLich.hien_thi_nội_dung_file_expander("I. LuatBuTruTuongQuan", "LUẬT BÙ TRỪ TƯƠNG QUAN:")
    DoiLich.hien_thi_nội_dung_file_expander("I-1.TranhKhiCungCuc", "I-1. TRÁNH KHÍ CÙNG CỰC (Đại Kỵ Tuyệt Đối)")
    DoiLich.hien_thi_nội_dung_file_expander("I-2.24NgayKy_va_SaoHung", "I-2. TRÁNH 24 NGÀY KỴ và SAO HUNG theo Nhị Thập Bát Tú")
    DoiLich.hien_thi_nội_dung_file_expander("I-3.BatTietTamKy", "I-3. BÁT TIẾT TAM KỲ")
    DoiLich.hien_thi_nội_dung_file_expander("I-4.VongSaoThanhLong", "I-4. VÒNG SAO THANH LONG (Ngày/Giờ Hoàng Đạo)")
    DoiLich.hien_thi_nội_dung_file_expander("I-5.TrietLoKhongVong", "I-5. TRIỆT LỘ - KHÔNG VONG")
    DoiLich.hien_thi_nội_dung_file_expander("I-6.GioQuyNhan", "I-6. Giờ QUÝ NHÂN ĐĂNG THIÊN MÔN")
    DoiLich.hien_thi_nội_dung_file_expander("I-7.TinhChatNguHanhThienCan", "I-7. TÍNH CHẤT NGŨ HÀNH THIÊN CAN")
    DoiLich.hien_thi_nội_dung_file_expander("II.TuDaiSatThoi", "II. Tránh TỨ ĐẠI SÁT THỜI Vận cá nhân")

    st.subheader(f'**TIÊU CHÍ CHỌN NGÀY/GIỜ**')
    st.markdown('<span style="color: darkblue; font-size: 20px;">**LUẬT BÙ TRỪ TƯƠNG QUAN:**</span>', unsafe_allow_html=True)
    DoiLich.coso_phuongphaptinh()

