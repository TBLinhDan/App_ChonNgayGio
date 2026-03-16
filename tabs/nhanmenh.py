import streamlit as st

from nam import year # Từ file nam.py gọi hàm year(2026) chuyển đổi sang năm Can Chi
from thang import stt_thangam
from thang import stt_ngay
from thang import tiet_khi
from Funtion import doc_file2
from Funtion import doc_file
from Funtion import path_data
from Funtion import lay_thong_tin
from Funtion import nhap_CanChi_ngaysinh
from PhuongPhap import tab_moi_su_dung_bien
from thang import lay_thien_can
from thang import lay_dia_chi



def NhanMenh_trong_Thoivan():
    
    tab_moi_su_dung_bien()
    
    content = st.session_state.content 
    lich_tong_hop = st.session_state.lich_tong_hop
    ngay_tot = st.session_state.tam_ky_data
    nam_canchi = st.session_state.nam_ht
    thang_canchi = st.session_state.thang_ht
    ngay_thang_nam = st.session_state.ngay_ht
    nam_cantinh = st.session_state.nam_cantinh
    thang_cantinh= st.session_state.thang_cantinh
    ngay_cantinh= st.session_state.ngay_cantinh
    tietkhi= st.session_state.tietkhi
    ngayCanChi= st.session_state.ngayCanChi
    sao_ngay= st.session_state.sao_ngay
    truc_ngay= st.session_state.truc_ngay
    gio_cantinh= st.session_state.gio_cantinh
    phut_cantinh= st.session_state.phut_cantinh
    gio_can_chi_thuc= st.session_state.gio_can_chi_thuc
      
    st.markdown(f'<span style="color: darkgreen;">Hôm nay **{ngay_thang_nam}**</span>', unsafe_allow_html=True)
    st.write(f"\nNăm {nam_cantinh}: **{nam_canchi}**")
    st.write(f"Tháng {thang_cantinh:02d}: **{thang_canchi}** _ Tiết Khí: **{tietkhi}**")
    st.write(f"Ngày {ngay_cantinh:02d}: **{ngayCanChi}** _ Sao: **{sao_ngay}** _ Trực: **{truc_ngay}**")
    st.write(f"{gio_cantinh:02d} giờ {phut_cantinh:02d} phút: **{gio_can_chi_thuc}**")
    st.info("HỆ THỐNG KIỂM ĐỊNH KHÍ VẬN cho Ngày Hiện Tại. Vui lòng Mở Xem chi tiết ở Tab trước.")
    st.divider()

    st.write("**Thông tin THAM KHẢO chung Hôm Nay:**")

    thongtin_sao = lay_thong_tin(sao_ngay, "28Sao")
    st.write(f"Ngày **{ngayCanChi}** có {thongtin_sao[1]}")

    thongtin_truc = lay_thong_tin(truc_ngay, "12Truc")
    st.write(f"Ngày **{ngayCanChi}** có {thongtin_truc[1]}")

    canngay_ht = lay_thien_can(ngayCanChi)
    #chingay_ht = lay_dia_chi(ngayCanChi)
    thongtin_canngay = lay_thong_tin(canngay_ht, "ViecPhuhop_CanNgay")
    st.write(f"Ngày **{canngay_ht}** _ {thongtin_canngay[1]}")

    st.divider()
    st.markdown('<span style="color: darkgreen; font-size: 20px;">**👤 THỜI VẬN Tác Động CÁ NHÂN?**</span>', unsafe_allow_html=True)

    nhap_CanChi = nhap_CanChi_ngaysinh()
    #st.write(nhap_CanChi)
    nhap_canngaysinh = nhap_CanChi[0]
    nhap_chingaysinh = nhap_CanChi[1]

    """
    if st.button("**TIẾP TỤC**"):
        st.balloons()
        st.warning("**Hẹn gặp lại Bạn ở phiên bản nâng cấp**\n\n **XIN CẢM ƠN !!!**")
        # Tùy chọn: st.session_state.show_answer = False (để đóng lại sau khi cảm ơn)
    """

if __name__ == "__NhanMenh_trong_Thoivan__":
  NhanMenh_trong_Thoivan()
