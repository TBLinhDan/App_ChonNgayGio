import streamlit as st
import pandas as pd

from nam import year
from thang import stt_thangam
from thang import stt_ngay
from thang import tiet_khi
from thang import lay_thien_can
from thang import lay_dia_chi
from thang import thanggieng
from thang import Lst_thang
from thang import stt_CanChi
from thang import tim_gio_Ty
from thang import tao_ds_12_gio
from thang import quy_doi_gio_can_chi
from thang import xu_ly_thoi_gian_thuc_dia
from Funtion import doc_file
from Funtion import path_data
from Funtion import lay_thong_tin_cached
from Funtion import loc_ngay_kieng_ky
from Funtion import truy_van_du_lieu_lich
from Funtion import xac_dinh_cung_cuc
from Funtion import loc_ngay_cung_cuc_trong_thang
from Funtion import loc_Thang_cung_cuc
from Funtion import display_cung_cuc_ngay_hien_tai
from Funtion import kiem_tra_cung_cuc_ngay_hien_tai
from Funtion import loc_Gio_cung_cuc
from Funtion import tinh_logic_khong_triet
from Funtion import kiem_tra_trietkhong_ngay_hien_tai
from Funtion import check_ngay_ky_sao_2026
from Funtion import ngay_hien_tai_co_ky
from Funtion import cosodichly
from Funtion import coso_phuongphaptinh

from PhuongPhap import vong_thanh_long
from PhuongPhap import he_thong_an_que_tam_ky
from PhuongPhap import hop_nhat_lich_thang
from PhuongPhap import display_unified_calendar
from PhuongPhap import tinh_gio_quy_nhan_dang_thien_mon
from PhuongPhap import he_thong_kiem_duyet_ngay_toan_dien



def DoiLich():
  st.subheader("CAN CHI Kim Cang Lịch")
  st.markdown('<span style="color: darkgreen; font-size: 20px;">**Năm BÍNH NGỌ_2026**</span>', unsafe_allow_html=True)
  st.markdown('<span style="color: darkgreen; font-size: 18px;">**[22/12/2025 - 22/12/2026]**</span>', unsafe_allow_html=True)
  st.subheader("📊 Phân tích Khí Vận")
  #st.subheader(" Năm BÍNH NGỌ_2026")
  #st.subheader("[22/12/2025 - 22/12/2026]")
  nam_cantinh = st.number_input("Nhập Năm Dương Lịch:", min_value =2026, max_value =2026)
  thang_cantinh = st.number_input("Nhập Tháng Dương Lịch:", min_value =1, max_value =12)
  ngay_cantinh = st.number_input("Nhập Ngày Dương Lịch:", min_value =1, max_value =31)
  gio_cantinh = st.number_input("Nhập Giờ (1-24):", min_value =1, max_value =24)
  phut_cantinh = st.number_input("Nhập Phút (1-60):", min_value =1, max_value =60)

  data_kinh_do = {
                    "An Giang": 105.11, "Bà Rịa - Vũng Tàu": 107.16, "Bạc Liêu": 105.72, "Bắc Giang": 106.20, "Bắc Kạn": 105.82,
                    "Bắc Ninh": 106.07, "Bến Tre": 106.37, "Bình Dương": 106.67, "Bình Định": 109.22, "Bình Phước": 106.88,
                    "Bình Thuận": 108.10, "Cà Mau": 104.91, "Cao Bằng": 106.25, "Cần Thơ": 105.78, "Đà Nẵng": 108.20,
                    "Đắk Lắk": 108.04, "Đắk Nông": 107.69, "Điện Biên": 103.01, "Đồng Nai": 106.84, "Đồng Tháp": 105.63,
                    "Gia Lai": 108.00, "Hà Giang": 104.98, "Hà Nam": 105.92, "Hà Nội": 105.85, "Hà Tĩnh": 105.90,
                    "Hải Dương": 106.31, "Hải Phòng": 106.68, "Hậu Giang": 105.47, "Hòa Bình": 105.33, "Hưng Yên": 106.05,
                    "Khánh Hòa": 109.19, "Kiên Giang": 105.08, "Kon Tum": 108.00, "Lai Châu": 103.46, "Lạng Sơn": 106.76,
                    "Lào Cai": 103.97, "Lâm Đồng": 108.44, "Long An": 106.40, "Nam Định": 106.16, "Nghệ An": 105.68,
                    "Ninh Bình": 105.98, "Ninh Thuận": 108.99, "Phú Thọ": 105.21, "Phú Yên": 109.30, "Quảng Bình": 106.62,
                    "Quảng Nam": 108.33, "Quảng Ngãi": 108.80, "Quảng Ninh": 107.06, "Quảng Trị": 107.19, "Sóc Trăng": 105.97,
                    "Sơn La": 103.91, "Tây Ninh": 106.10, "Thái Bình": 106.33, "Thái Nguyên": 105.84, "Thanh Hóa": 105.77,
                    "Thừa Thiên Huế": 107.59, "Tiền Giang": 106.36, "TP. Hồ Chí Minh": 106.66, "Trà Vinh": 106.34, "Tuyên Quang": 105.21,
                    "Vĩnh Long": 105.97, "Vĩnh Phúc": 105.60, "Yên Bái": 104.89
                }
  #st.subheader("📍 Thông tin địa phương")

  # Người dùng chọn tên tỉnh từ danh sách
  # Biến 'tinh_thanh_chon' sẽ lưu tên tỉnh (String)
  tinh_thanh_chon = st.selectbox("Vui lòng chọn Tỉnh/Thành phố nơi bạn đang đứng:", 
                                options=list(data_kinh_do.keys()),
                                index=57  # Mặc định chọn TP. Hồ Chí Minh
                                )
  #st.write(tinh_thanh_chon)
 
  # Định nghĩa màu sắc vàng đồng theo phong cách Kinh Dịch/Tử Vi
  style_nut_vang_dong = """
                          <style>
                            div.stButton > button:first-child {
                                background-color: #D4AF37; /* Màu vàng đồng (Gold) */
                                color: #000000;            /* Màu chữ đen cho rõ nét */
                                font-weight: bold;         /* Chữ in đậm */
                                border-radius: 10px;        /* Bo góc nhẹ */
                                border: 2px solid #B8860B; /* Viền vàng đậm hơn */
                                width: 35%;               /* Nút dài hết khung (tùy chọn) */
                                height: 2.5em;               /* Độ cao của nút */
                                transition: all 0.3s;      /* Hiệu ứng mượt mà */
                            }

                            /* Hiệu ứng khi đưa chuột vào (Hover) */
                            div.stButton > button:first-child:hover {
                                background-color: #FFD700; /* Vàng sáng hơn */
                                color: #000000;
                                border: 1px solid #D4AF37;
                                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Tạo đổ bóng */
                            }
                            
                            /* Hiệu ứng khi nhấn vào (Active) */
                            div.stButton > button:first-child:active {
                                transform: scale(0.98);    /* Nhấn lún xuống một chút */
                            }
                        </style>
                        """

  # Chèn CSS vào ứng dụng
  st.markdown(style_nut_vang_dong, unsafe_allow_html=True)

  # Tạo nút bấm
  if st.button("CHUYỂN ĐỔI"):
    #st.write("🔄 Đang tiến hành tính toán...")

  #if st.button("CHUYỂN ĐỔI", type="primary"):
    stt = stt_ngay(ngay_cantinh, thang_cantinh, nam_cantinh)
    #st.write("stt_ngày: ", stt)
    if stt == 0:
      st.write("VUI LÒNG NHẬP LẠI NGÀY THÁNG")
    else:
      nam_canchi = year(nam_cantinh) #  Gọi hàm year() ra Can Chi của Năm, dạng string gán vào biến result
      ngay_thang_nam = f"{ngay_cantinh:02d}/{thang_cantinh:02d}/{nam_cantinh}"
      st.markdown(f'<span style="color: green;">**{ngay_thang_nam}**</span>', unsafe_allow_html=True)
      #st.write(f"**{ngay_thang_nam}:**")
      st.write(f"\nNăm {nam_cantinh}: **{nam_canchi}**")
      st.balloons()

      #tách riêng Thiên Can ra khỏi tên Can Chi năm
      can_nam = lay_thien_can(nam_canchi)
      #st.write(can_nam)
      
      #Xác định được Can Chi Tháng Dần
      thang_gieng = thanggieng(can_nam) 
      #st.write(thang_gieng)
      #Xác định DS 12 tháng trong năm
      ds = Lst_thang(thang_gieng)
      #st.write(ds)

      # Từ ngày tháng năm DL tính ra tháng âm 
      stt_thang_am = stt_thangam(ngay_cantinh, thang_cantinh, nam_cantinh)
      #st.write(stt_thang_am)
      thang_canchi = ds[stt_thang_am-1]
      tietkhi=tiet_khi(ngay_cantinh, thang_cantinh, nam_cantinh)
    
      st.write(f"Tháng {thang_cantinh:02d}: **{thang_canchi}** _ Tiết Khí: **{tietkhi}**")

# chuyển đổi một con số (số thứ tự ngày) thành tên Can Chi tương ứng.
      stt = stt_ngay(ngay_cantinh, thang_cantinh, nam_cantinh)
      #st.write("stt_ngày: ", stt)
      ngayCanChi= stt_CanChi(stt)
      #st.write(f"Ngày {ngay_cantinh:02d}: {ngayCanChi}")
      can_ngay = lay_thien_can(ngayCanChi)
      #st.write(can)
      chi_ngay = lay_dia_chi(ngayCanChi)
      #st.write(chi)

      gioTy = tim_gio_Ty(can_ngay)
      #st.write(gioTy)
      ds_12_gio_hom_nay = tao_ds_12_gio(gioTy)
      #st.write(ds_12_gio_hom_nay)

      #Mốc giờ Tý theo toạ đọ Kinh tuyến gôc của múi giờ thay đổi theo Ngày

      file_path = path_data("data_2026")
      #st.write(file_path)  
      content = doc_file(file_path, delimiter=',')
      #if content:
      # Hiển thị dữ liệu lên giao diện web
        #st.write("Dữ liệu đã đọc thành công:")
      #st.write(content[19])
      #st.dataframe(content)
      thong_tin = lay_thong_tin_cached(ngay_thang_nam, "data_2026",0)
      #st.write(thong_tin)
      sao_ngay = thong_tin[7]
      truc_ngay= thong_tin[9]
      st.write(f"Ngày {ngay_cantinh:02d}: **{ngayCanChi}** _ Sao: **{sao_ngay}** _ Trực: **{truc_ngay}**")

      gio_Ty_Thuc = thong_tin[1]
      #st.write(f"Giờ Tý Thực của Ngày {ngay_thang_nam} bắt đầu khởi từ {gio_Ty_Thuc}")
      parts = gio_Ty_Thuc.split(':')
      mocgioTy_thuc = int(parts[0]) 
      mocphutTy_thuc = int(parts[1])

      # Tính Giờ TÝ thực theo kinh độ địa phương lệch so với Kinh độ gôc(Múi Giờ)
      gioTy_thuc, phutTy_thuc = xu_ly_thoi_gian_thuc_dia(tinh_thanh_chon, mocgioTy_thuc, mocphutTy_thuc, data_kinh_do)                                                      
      #Quy đổi giờ phút thực tế sang giờ Can Chi dựa trên mốc khởi Tý thực theo kinh độ địa phương
      gio_can_chi_thuc = quy_doi_gio_can_chi(gio_cantinh, phut_cantinh, gioTy_thuc, phutTy_thuc, ds_12_gio_hom_nay)
      #st.write(f"\n(Ngày {can} có giờ đầu khởi {gioTy})")
      st.write(f"{gio_cantinh:02d} giờ {phut_cantinh:02d} phút: **{gio_can_chi_thuc}**")
      
      st.success(f"📍 Địa điểm: **{tinh_thanh_chon}** (Kinh độ: **{data_kinh_do[tinh_thanh_chon]}°**). \n\n"
                 f"☯️ Giờ Thực **{gioTy}** bắt đầu khởi từ **{gioTy_thuc:02d}:{phutTy_thuc:02d}**" )


      st.divider()
      #st.subheader("**Data_2026**")
      #st.dataframe(content)

      #Tránh Khí Cùng Cực (Đại Kỵ Tuyệt Đối)
      #st.markdown('<span style="color: blue;">**LỰA CHỌN NGÀY GIỜ TỐT THEO THÁNG:**</span>', unsafe_allow_html=True)

      st.markdown(f" 🛑 **Tránh Khí Cùng Cực (Đại Kỵ Tuyệt Đối)**")

      # 1. Cảnh báo Tháng trong Năm
      ds_thang_ky = loc_Thang_cung_cuc(content, can_nam)
      if ds_thang_ky:
        with st.expander(f"📅 Cảnh báo Tháng kỵ trong năm **{nam_canchi}**"):
          for t in ds_thang_ky:
            st.error(f"Tháng **{t['Tháng']}**: Phạm {t['Loại']} ({t['Can vi phạm']})")
      else:
          st.success(f"Năm {nam_canchi} không có Tháng nào vi phạm nguyên lý Khí Cùng Cực.")

      # 2. Cảnh báo Ngày trong Tháng
      thang_dang_xem = thang_canchi
      # Gọi hàm lọc
      ds_canh_bao = loc_ngay_cung_cuc_trong_thang(content, thang_dang_xem)

      #st.markdown(f"### 🛑 Cảnh báo 'Khí Cùng Cực' - Tháng {thang_dang_xem}")
      #st.dataframe(ds_canh_bao)

      if ds_canh_bao:
        with st.expander(f"📅 Cảnh báo Ngày kỵ trong tháng **{thang_canchi}**"):
          for t in ds_canh_bao:
            st.error(f"Ngày {t[0]} **{t[4]}**: {t[13]}")
      else:
          st.success(f"Tháng {thang_dang_xem} không có ngày nào vi phạm nguyên lý Khí Cùng Cực.")
      
      nam_ht = nam_canchi
      thang_ht = thang_canchi
      ngay_canchi = ngayCanChi
      thang_gieng_ht = thang_gieng

      display_cung_cuc_ngay_hien_tai(nam_canchi, thang_canchi, ngay_canchi)

       # 3. Cảnh báo Giờ trong Ngày
      # ds_12_gio_hom_nay là list 12 giờ Can Chi bạn đã tính từ Ngũ Tý Độn
      ds_gio_ky = loc_Gio_cung_cuc(can_ngay, ds_12_gio_hom_nay)
      if ds_gio_ky:
        st.warning(f"⏰ Hôm nay **{ngay_thang_nam}** ngày **{ngayCanChi}**, Giờ kỵ: **{', '.join(ds_gio_ky)}**")
      else:
          st.success(f"Ngày hôm nay {ngayCanChi} không có Giờ nào vi phạm nguyên lý Khí Cùng Cực.")

      st.divider()
      # danh sach các ngày kiêng kỵ trong tháng Tránh 24 Ngày Kỵ và Sao Hung theo Nhị Thập Bát Tú:
      danh_sach_loc = loc_ngay_kieng_ky(content, thang_canchi )
      st.markdown(f" 🛑 **Tránh 24 Ngày Kỵ và Sao Hung theo Nhị Thập Bát Tú trong tháng {thang_canchi}**")
      if danh_sach_loc:
        with st.expander(f"📅 Cảnh báo Ngày kỵ trong tháng **{thang_canchi}**"):
          for t in danh_sach_loc:
            st.error(f"Ngày {t[0]} **{t[4]}**: {t[11]} (Sao {t[7]})" )
      else:
          st.info(f"Tháng {thang_canchi} không có ngày nào ghi chú kiêng kỵ.")

      check_ngay_ky_sao_2026(ngay_thang_nam, content)

      st.divider()
      #BÁT TIẾT TAM KỲ
      st.markdown(f"✨ **BÁT TIẾT TAM KỲ**")
      ngay_tot, debug = he_thong_an_que_tam_ky(nam_ht, thang_ht, thang_gieng_ht, content)
      
      # Expander 1: Thông tin phân tích logic
      with st.expander("🧩 Phân tích Logic Cửu Cung"):
          c1, c2, c3 = st.columns(3)
          with c1:
              st.write("**Gốc tọa độ:**")
              st.markdown(f"- Khởi Giáp Tý: `{debug['Cung khởi Giáp Tý']}`")
              st.markdown(f"- Chiều: `{debug['Chiều vận hành'].upper()}`")
          with c2:
              st.write("**Vị trí an:**")
              st.markdown(f"- Thái Tuế: `{debug['Cung Thái Tuế']}`")
              st.markdown(f"- Cung Tháng: `{debug['Cung Tháng hiện tại']}`")
          with c3:
              st.write("**Tọa độ Kỳ:**")
              for c, s in debug['Tọa độ Tam Kỳ'].items():
                  st.markdown(f"- Cung {c}: Sao {s}")

      # Expander 2: Kết quả ngày tốt (Mặc định mở)
      with st.expander(f"📅 Danh sách ngày hội tụ Tam Kỳ: Tháng {thang_ht}", expanded=True):
          if ngay_tot:
              import pandas as pd
              df = pd.DataFrame(ngay_tot)
              # Chỉnh sửa hiển thị bảng
              st.dataframe(df, use_container_width=True, hide_index=True)
              st.success(f"Đã tìm thấy {len(ngay_tot)} ngày Cát tường hội tụ Tam kỳ, đây là Thanh Khí tối thượng không bị cách bức hoặc ngăn cản bởi bất kỳ hung sát nào, có thể đè bẹp Hắc Đạo hoặc Tuần Triệt.")
          else:
              st.warning("Không có ngày nào hội tụ Tam Kỳ trong tháng này.")
      
      ngay_hien_tai_co_ky(ngay_thang_nam, ngay_tot)
      


      st.divider()
      # VÒNG SAO THANH LONG
      vong_thanh_long (thang_canchi, ngayCanChi, ngay_thang_nam)

      st.divider()
      # TRIỆT LỘ KHÔNG VONG
      kiem_tra_trietkhong_ngay_hien_tai(ngay_canchi, thang_canchi)
      
      st.divider()
      # GIỜ QUÝ NHÂN ĐĂNG THIÊN MÔN
      tinh_gio_quy_nhan_dang_thien_mon(ngay_canchi, ngay_thang_nam, content)
      
      

      #ngay_tot, debug = he_thong_an_que_tam_ky(nam_ht, thang_ht, thang_gieng_ht, content)
      st.divider()
      # Hàm hiển thị bảng lịch thống nhất, tập hợp mọi phương pháp tính toán.
      lich_tong_hop = display_unified_calendar(nam_canchi, thang_canchi, thang_gieng, content)

      st.divider()
      he_thong_kiem_duyet_ngay_toan_dien(ngay_thang_nam, thang_canchi, nam_canchi, content, lich_tong_hop, ngay_tot)

      #lưu các biến vào bộ nhớ tạm của Session để gọi bên Tab khác
      # LƯU VÀO KHO (Dùng Key để định danh)
      st.session_state.content = content
      st.session_state.lich_tong_hop = lich_tong_hop
      st.session_state.tam_ky_data = ngay_tot
      st.session_state.nam_ht = nam_canchi
      st.session_state.thang_ht = thang_canchi
      st.session_state.ngay_ht = ngay_thang_nam
      st.session_state.nam_cantinh = nam_cantinh
      st.session_state.thang_cantinh = thang_cantinh
      st.session_state.ngay_cantinh = ngay_cantinh
      st.session_state.tietkhi = tietkhi
      st.session_state.ngayCanChi = ngayCanChi
      st.session_state.sao_ngay = sao_ngay
      st.session_state.truc_ngay = truc_ngay
      st.session_state.gio_cantinh = gio_cantinh
      st.session_state.phut_cantinh = phut_cantinh
      st.session_state.gio_can_chi_thuc = gio_can_chi_thuc



if __name__ == "__DoiLich__":
  DoiLich()
