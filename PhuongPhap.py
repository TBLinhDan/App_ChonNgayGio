import streamlit as st
import pandas as pd

from nam import year
from thang import stt_thangam
from thang import stt_ngay
from thang import tiet_khi
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
from Funtion import loc_Gio_cung_cuc

from thang import lay_thien_can
from thang import lay_dia_chi

from Funtion import kiem_tra_cung_cuc_ngay_hien_tai
from Funtion import check_ngay_ky_sao_2026
from Funtion import check_ngay_ky_2026
from Funtion import tinh_logic_khong_triet
from Funtion import kiem_tra_ngay_hien_tai_co_ky
from Funtion import tinh_gio_quy_nhan_tu_content

def tinh_ngu_ty_don(can_ngay, chi_gio):
    """
    Tìm Thiên can của giờ dựa trên Thiên can của ngày (Ngũ Tý Độn).
    - can_ngay: Thiên can của ngày (Giáp, Ất, Bính...)
    - chi_gio: Địa chi của giờ (Tý, Sửu, Dần...)
    """
    lst_can = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    lst_chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

    # 1. Xác định can khởi giờ Tý dựa trên can ngày
    # Giáp, Kỷ -> khởi Giáp Tý (0)
    # Ất, Canh -> khởi Bính Tý (2)
    # Bính, Tân -> khởi Mậu Tý (4)
    # Đinh, Nhâm -> khởi Canh Tý (6)
    # Mậu, Quý -> khởi Nhâm Tý (8)
    
    mapping_khoi_ty = {
        "Giáp": 0, "Kỷ": 0,
        "Ất": 2, "Canh": 2,
        "Bính": 4, "Tân": 4,
        "Đinh": 6, "Nhâm": 6,
        "Mậu": 8, "Quý": 8
    }
    
    index_can_khoi = mapping_khoi_ty.get(can_ngay)
    
    if index_can_khoi is None:
        return "Không xác định"

    # 2. Tính khoảng cách từ chi Tý đến chi hiện tại
    index_chi = lst_chi.index(chi_gio)
    
    # 3. Tìm can của giờ tương ứng
    # Công thức: (Index Can Khởi + Khoảng cách Chi) % 10
    index_can_gio = (index_can_khoi + index_chi) % 10
    
    return lst_can[index_can_gio]

def an_vong_thanh_long(dia_chi_nhap):
    DIA_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    # 12 Sao theo thứ tự chuẩn
    DANH_SACH_12_SAO = [
        ("Thanh Long", "Hoàng Đạo"), ("Minh Đường", "Hoàng Đạo"), ("Thiên Hình", "Hắc Đạo"),
        ("Chu Tước", "Hắc Đạo"),     ("Kim Quỷ", "Hoàng Đạo"),    ("Bảo Quang", "Hoàng Đạo"),
        ("Bạch Hổ", "Hắc Đạo"),      ("Ngọc Đường", "Hoàng Đạo"), ("Thiên Lao", "Hắc Đạo"),
        ("Huyền Vũ", "Hắc Đạo"),     ("Tư Mệnh", "Hoàng Đạo"),    ("Câu Trần", "Hắc Đạo")
    ]
    BANG_KHOI_THANH_LONG = {
        "Dần": "Tý", "Thân": "Tý", "Mão": "Dần", "Dậu": "Dần",
        "Thìn": "Thìn", "Tuất": "Thìn", "Tỵ": "Ngọ", "Hợi": "Ngọ",
        "Tý": "Thân", "Ngọ": "Thân", "Sửu": "Tuất", "Mùi": "Tuất"
    }
    
    chi_chuan = dia_chi_nhap.split()[-1]
    cung_khoi_ten = BANG_KHOI_THANH_LONG.get(chi_chuan)
    if not cung_khoi_ten: return None

    idx_khoi = DIA_CHI.index(cung_khoi_ten)
    vong_sao = {}
    
    # Duyệt qua 12 cung địa chi từ Tý đến Hợi
    for i in range(12):
        ten_cung = DIA_CHI[i]
        # Tính xem cung hiện tại cách cung khởi bao nhiêu bước
        khoang_cach = (i - idx_khoi) % 12
        vong_sao[ten_cung] = DANH_SACH_12_SAO[khoang_cach]
        
    return vong_sao

def lay_ds_gio_hoang_dao(dia_chi_ngay):
    """
    Sử dụng kết quả từ hàm an_vong_thanh_long để trích xuất 
    danh sách các giờ Hoàng Đạo trong ngày.
    """
    # 1. Gọi hàm an_vong_thanh_long để lấy toàn bộ vòng sao của ngày
    vong_sao_ngay = an_vong_thanh_long(dia_chi_ngay)
    
    if not vong_sao_ngay:
        return []

    # 2. Lọc danh sách các giờ có tính chất là "Hoàng Đạo"
    # vong_sao_ngay có dạng: {"Tý": ("Thanh Long", "Hoàng Đạo"), ...}
    ds_gio_hoang_dao = [
        chi for chi, (ten_sao, tinh_chat) in vong_sao_ngay.items() 
        if tinh_chat == "Hoàng Đạo"
    ]
    
    # 3. Sắp xếp lại danh sách theo thứ tự thời gian (Tý -> Hợi)
    # Vì Dictionary trong Python từ 3.7+ giữ thứ tự chèn, 
    # nhưng để chắc chắn ta đối chiếu với bảng DIA_CHI chuẩn.
    DIA_CHI_CHUAN = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    ds_gio_hoang_dao.sort(key=lambda x: DIA_CHI_CHUAN.index(x))
    
    return ds_gio_hoang_dao

# --- VÍ DỤ SỬ DỤNG ---
# chi_ngay = "Hợi"
# ds_gio_hd = lay_ds_gio_hoang_dao(chi_ngay)
# print(f"Giờ Hoàng Đạo ngày {chi_ngay}: {', '.join(ds_gio_hd)}")


# VÒNG SAO THANH LONG
def vong_thanh_long (thang_canchi, ngayCanChi, ngay_thang_nam):
    # Vòng Sao Thanh Long
    # Giả sử ta muốn tính Giờ Hoàng Đạo cho ngày hiện tại
    st.markdown(f"✨ **Vòng Sao Hoàng Đạo**")
      
    chi_thang = lay_dia_chi(thang_canchi)
    chi_ngay = lay_dia_chi(ngayCanChi)

    def an_vong_thanh_long(dia_chi_nhap):
        DIA_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        # 12 Sao theo thứ tự chuẩn
        DANH_SACH_12_SAO = [
            ("Thanh Long", "Hoàng Đạo"), ("Minh Đường", "Hoàng Đạo"), ("Thiên Hình", "Hắc Đạo"),
            ("Chu Tước", "Hắc Đạo"),     ("Kim Quỹ", "Hoàng Đạo"),    ("Bảo Quang", "Hoàng Đạo"),
            ("Bạch Hổ", "Hắc Đạo"),      ("Ngọc Đường", "Hoàng Đạo"), ("Thiên Lao", "Hắc Đạo"),
            ("Huyền Vũ", "Hắc Đạo"),     ("Tư Mệnh", "Hoàng Đạo"),    ("Câu Trần", "Hắc Đạo")
        ]
        BANG_KHOI_THANH_LONG = {
            "Dần": "Tý", "Thân": "Tý", "Mão": "Dần", "Dậu": "Dần",
            "Thìn": "Thìn", "Tuất": "Thìn", "Tỵ": "Ngọ", "Hợi": "Ngọ",
            "Tý": "Thân", "Ngọ": "Thân", "Sửu": "Tuất", "Mùi": "Tuất"
        }
        
        chi_chuan = dia_chi_nhap.split()[-1]
        cung_khoi_ten = BANG_KHOI_THANH_LONG.get(chi_chuan)
        if not cung_khoi_ten: return None

        idx_khoi = DIA_CHI.index(cung_khoi_ten)
        vong_sao = {}
        
        # Duyệt qua 12 cung địa chi từ Tý đến Hợi
        for i in range(12):
            ten_cung = DIA_CHI[i]
            # Tính xem cung hiện tại cách cung khởi bao nhiêu bước
            khoang_cach = (i - idx_khoi) % 12
            vong_sao[ten_cung] = DANH_SACH_12_SAO[khoang_cach]
            
        return vong_sao

    def kiem_tra_ngay_hoang_dao(chi_thang, chi_ngay):
        # 1. An vòng sao Thanh Long dựa trên Chi Tháng
        vong_sao_thang = an_vong_thanh_long(chi_thang)
        
        if not vong_sao_thang:
            return None
        
        # 2. Lấy thông tin sao của Chi Ngày hiện tại
        # Vì chi_ngay có thể là "Giáp Tý", ta dùng .split()[-1] để lấy "Tý"
        ten_chi_ngay = chi_ngay.split()[-1]
        sao_cua_ngay, loai_dao = vong_sao_thang.get(ten_chi_ngay, (None, None))
        
        return sao_cua_ngay, loai_dao
    
    sao_ngay, loai_ngay = kiem_tra_ngay_hoang_dao(chi_thang, chi_ngay)
    if sao_ngay:
        # Hiển thị tiêu đề nhanh
        status_icon = "⏰" if loai_ngay == "Hoàng Đạo" else "🌑"
        st.markdown(f"{status_icon}Hôm Nay {ngay_thang_nam} _ {ngayCanChi} là ngày: **{loai_ngay}**")

        with st.expander(f"🔍 Chi tiết Ngày {chi_ngay} _ Tháng {chi_thang}"):
            col1, col2 = st.columns(2)
              
            with col1:
                st.write(f"Địa Chi Tháng: **{chi_thang}**")
                st.write(f"Địa Chi Ngày: **{chi_ngay}**")
              
            with col2:
                if loai_ngay == "Hoàng Đạo":
                    st.success(f"**Sao chủ:** {sao_ngay}")
                    st.info("Đây là ngày Cát lành, thuận lợi cho các việc khởi sự, ký kết.")
                else:
                    st.error(f"Sao chủ: **{sao_ngay}**")
                    st.warning("Đây là ngày Hắc đạo, nên thận trọng trong các việc đại sự.")

            # Hiển thị thêm bảng tra nhanh 12 ngày trong tháng này (Tùy chọn)
            st.divider()
            st.caption(f"**Bảng tra sao 12 địa chi trong tháng {thang_canchi}:**")
            vong_full = an_vong_thanh_long(chi_thang)
              
            # Hiển thị dạng dòng ngang gọn gàng
            hc_cols = st.columns(6)
            for i, (c, info) in enumerate(vong_full.items()):
                with hc_cols[i % 6]:
                    color = "green" if info[1] == "Hoàng Đạo" else "gray"
                    st.markdown(f"**{c}**\n:{color}[{info[0]}]")

    vong_sao_gio = an_vong_thanh_long(chi_ngay)
    #st.write(vong_sao_gio)
    if vong_sao_gio:
        with st.expander(f"🔍 Giờ Hoàng Đạo / Hắc Đạo (Ngày {ngayCanChi})"):
            # Tạo 2 cột bên trong expander để tối ưu không gian
            col_trai, col_phai = st.columns(2)
              
            for idx, (cung, info) in enumerate(vong_sao_gio.items()):
                ten_sao, loai_dao = info
                  
                # Định dạng nội dung hiển thị
                if loai_dao == "Hoàng Đạo":
                    text_hien_thi = f"✅ **Giờ {cung}**: {ten_sao} (Hoàng Đạo)"
                    # Chọn cột để in
                    target_col = col_trai if idx < 6 else col_phai
                    target_col.success(text_hien_thi)
                else:
                    text_hien_thi = f"❌ Giờ {cung}: {ten_sao} (Hắc Đạo)"
                    target_col = col_trai if idx < 6 else col_phai
                    target_col.text(text_hien_thi)



def he_thong_an_que_tam_ky(nam_cc, thang_cc, thang_gieng_cc, data_list):

    #st.markdown(f"✨ **BÁT TIẾT TAM KỲ**")
    # --- PHẦN 1: DỮ LIỆU NỀN TẢNG ---
    LST_CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
    LST_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    HOA_GIAP = [f"{LST_CAN[i%10]} {LST_CHI[i%12]}" for i in range(60)]
    TEN_CUNG = {1: "Khảm", 2: "Khôn", 3: "Chấn", 4: "Tốn", 5: "Trung cung", 6: "Càn", 7: "Đoài", 8: "Cấn", 9: "Ly"}
    
    chi_thang_ht = thang_cc.split()[-1]
    can_thang_gieng = thang_gieng_cc.split()[0]

    # --- PHẦN 2: XÁC ĐỊNH CUNG KHỞI GIÁP TÝ VÀ CHIỀU (Quy luật của bạn) ---
    # Bảng cấu hình: Chi tháng -> (Cung khởi Giáp Tý, Chiều)
    config_he_thong = {
        "Tý": (1, "thuận"),
        "Sửu": (8, "thuận"), "Dần": (8, "thuận"),
        "Mão": (3, "thuận"),
        "Thìn": (4, "thuận"), "Tỵ": (4, "thuận"),
        "Ngọ": (9, "nghịch"),
        "Mùi": (2, "nghịch"), "Thân": (2, "nghịch"),
        "Dậu": (7, "nghịch"),
        "Tuất": (6, "nghịch"), "Hợi": (6, "nghịch")
    }
    
    cung_khoi_giap_ty, chieu = config_he_thong.get(chi_thang_ht, (1, "thuận"))
    huong = 1 if chieu == "thuận" else -1

    # --- PHẦN 3: TÌM CUNG AN THÁI TUẾ ---
    # Tính số bước nhảy từ Giáp Tý (0) đến Năm hiện tại
    idx_nam = HOA_GIAP.index(nam_cc)
    cung_thai_tue = (cung_khoi_giap_ty + (idx_nam * huong) - 1) % 9 + 1
    if cung_thai_tue <= 0: cung_thai_tue += 9

    # --- PHẦN 4: AN TAM KỲ (ẤT-BÍNH-ĐINH) TỪ CUNG THÁI TUẾ ---
    # Can tháng Giêng khởi tại cung Thái Tuế
    idx_can_gieng = LST_CAN.index(can_thang_gieng)
    cung_tam_ky = {}
    for can_target in ["Ất", "Bính", "Đinh"]:
        buoc_can = (LST_CAN.index(can_target) - idx_can_gieng) % 10
        c_so = (cung_thai_tue + (buoc_can * huong) - 1) % 9 + 1
        if c_so <= 0: c_so += 9
        cung_tam_ky[int(c_so)] = can_target

    # --- PHẦN 5: XÁC ĐỊNH CUNG THÁNG HIỆN TẠI (Tịnh tiến từ Thái Tuế) ---
    # Tháng Dần (tháng 1) khởi tại Thái Tuế
    idx_thang_ht = LST_CHI.index(chi_thang_ht)
    buoc_thang = (idx_thang_ht - 2) % 12 
    cung_thang_ht = (cung_thai_tue + (buoc_thang * huong) - 1) % 9 + 1
    if cung_thang_ht <= 0: cung_thang_ht += 9

    # --- PHẦN 6: QUÉT LỊCH VÀ KẾT QUẢ ---
    ngay_trong_thang = [row for row in data_list if len(row) > 3 and row[3].strip() == thang_cc]
    ket_qua_ngay = []
    for i, row in enumerate(ngay_trong_thang):
        mông = i + 1
        c_ngay = (cung_thang_ht + ((mông - 1) * huong) - 1) % 9 + 1
        if c_ngay <= 0: c_ngay += 9
        
        c_ngay = int(c_ngay)
        if c_ngay in cung_tam_ky:
            ket_qua_ngay.append({
                "Mồng": mông, "Ngày DL": row[0], 
                "Can Chi": row[4],
                "Cung": f"{c_ngay}.{TEN_CUNG[c_ngay]}", 
                "Gặp Kỳ": cung_tam_ky[c_ngay]
            })

    debug_info = {
        "Cung khởi Giáp Tý": cung_khoi_giap_ty,
        "Chiều vận hành": chieu,
        "Cung Thái Tuế": int(cung_thai_tue),
        "Cung Tháng hiện tại": int(cung_thang_ht),
        "Tọa độ Tam Kỳ": cung_tam_ky
    }

    return ket_qua_ngay, debug_info

# GIỜ QUÝ NHÂN ĐĂNG THIÊN MÔN
def tinh_gio_quy_nhan_dang_thien_mon(ngay_canchi, ngay_thang_nam, content):

    def tinh_gio_quy_nhan_tu_content(ngay_dl_hien_tai, content_data):

        """
        ngay_dl_hien_tai: chuỗi định dạng "dd/mm/yyyy" khớp với cột 0
        content_data: mảng dữ liệu lịch từ file
        """
        lst_chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        
        # Bảng mapping Nguyệt Tướng (Dựa theo ảnh bạn cung cấp)
        map_nguyet_tuong = {
            "Vũ Thuỷ": "Hợi", "Kinh Trập": "Hợi",
            "Xuân Phân": "Tuất", "Thanh Minh": "Tuất",
            "Cốc Vũ": "Dậu", "Lập Hạ": "Dậu",
            "Tiểu Mãn": "Thân", "Mang Chủng": "Thân",
            "Hạ Chí": "Mùi", "Tiểu Thử": "Mùi",
            "Đại Thử": "Ngọ", "Lập Thu": "Ngọ",
            "Xử Thử": "Tỵ", "Bạch Lộ": "Tỵ",
            "Thu Phân": "Thìn", "Hàn Lộ": "Thìn",
            "Sương Giáng": "Mão", "Lập Đông": "Mão",
            "Tiểu Tuyết": "Dần", "Đại Tuyết": "Dần",
            "Đông Chí": "Sửu", "Tiểu Hàn": "Sửu",
            "Đại Hàn": "Tý", "Lập Xuân": "Tý"
        }

        # Bảng Quý Nhân (Dương/Âm)
        map_quy_nhan = {
            "Giáp": {"D": "Mùi", "A": "Sửu"}, "Ất": {"D": "Thân", "A": "Tý"},
            "Bính": {"D": "Dậu", "A": "Hợi"}, "Đinh": {"D": "Hợi", "A": "Dậu"},
            "Mậu": {"D": "Sửu", "A": "Mùi"}, "Kỷ": {"D": "Tý", "A": "Thân"},
            "Canh": {"D": "Sửu", "A": "Mùi"}, "Tân": {"D": "Dần", "A": "Ngọ"},
            "Nhâm": {"D": "Mão", "A": "Tỵ"}, "Quý": {"D": "Tỵ", "A": "Mão"}
        }

        # Bước 1 & 2: Tìm dòng dữ liệu và trích xuất thông tin
        row_hien_tai = None
        for row in content_data:
            if str(row[0]).strip() == ngay_dl_hien_tai:
                row_hien_tai = row
                break
        
        if not row_hien_tai:
            return "Không tìm thấy dữ liệu cho ngày này trong content."

        # Lấy thông tin từ cột index
        can_chi_ngay = str(row_hien_tai[4]).strip() # Can Chi Ngày
        can_ngay = can_chi_ngay.split()[0]          # Lấy Thiên Can
        tiet_khi = str(row_hien_tai[5]).strip()     # Tiết Khí (Index 5)

        # Bước 3: Xác định Nguyệt Tướng
        tuong_chi = map_nguyet_tuong.get(tiet_khi)
        if not tuong_chi:
            return f"Tiết khí '{tiet_khi}' không nằm trong bảng Nguyệt Tướng."

        # Bước 4: Tính toán logic Thiên Môn (Hợi = 11)
        T = lst_chi.index(tuong_chi)
        H = 11
        
        Q_duong = lst_chi.index(map_quy_nhan[can_ngay]["D"])
        Q_am = lst_chi.index(map_quy_nhan[can_ngay]["A"])

        gio_duong = lst_chi[(H - Q_duong + T) % 12]
        gio_am = lst_chi[(H - Q_am + T) % 12]

        return {
            "Ngày": ngay_dl_hien_tai,
            "Can Chi": can_chi_ngay,
            "Tiết Khí": tiet_khi,
            "Nguyệt Tướng": tuong_chi,
            "Giờ Dương Quý": gio_duong,
            "Giờ Âm Quý": gio_am
        }

    res_quy_nhan = tinh_gio_quy_nhan_tu_content(ngay_thang_nam, content)
    st.markdown("☀️ **GIỜ QUÝ NHÂN ĐĂNG THIÊN MÔN**")
    st.markdown(f"Ngày **{ngay_thang_nam} _ {ngay_canchi}:**")


    if isinstance(res_quy_nhan, dict):
        st.info(f"Dựa trên Tiết khí **{res_quy_nhan['Tiết Khí']}** (Tướng {res_quy_nhan['Nguyệt Tướng']})")
        
        col1, col2 = st.columns(2)
        with col1:
            st.success(f"**Giờ Dương Quý:** {res_quy_nhan['Giờ Dương Quý']}")
            #st.caption("Dương Quý nhân đăng thiên môn chỉ Quý khi gia ở giờ ban ngày (từ giờ Mão đến giờ Thân). Ngoài dải không dùng")
        with col2:
            st.success(f"**Giờ Âm Quý:** {res_quy_nhan['Giờ Âm Quý']}")
            #st.caption("Âm Quý Nhân đăng thiên môn chỉ Quý khi gia ở giờ ban đêm (từ giờ Dậu đến giờ Dần). Ngoài dải không dùng")
        
        st.markdown("> **Lưu ý:** Đây là giờ TỐI THƯỢNG CÁT KHÁNH có thể HOÁ GIẢI HUNG SÁT, dùng để Khởi hành Khai trương hoặc thực hiện các việc quan trọng. Dương Quý Nhân chỉ Quý khi gia ở giờ ban ngày (giờ Mão đến Thân). Âm Quý Nhân chỉ Quý khi gia ở giờ ban đêm (giờ Dậu đến Dần)")
    else:
        st.error(res_quy_nhan)



# ==========================================
# 2. HÀM HỢP NHẤT DỮ LIỆU (AGGREGATOR)
# ==========================================
#Tập hợp tất cả dữ liệu các phương pháp chon Ngày Giờ vào 1 danh sách duy nhất.

def hop_nhat_lich_thang(thang_cc, content, ngay_tam_ky_list):

    # 1. Lấy danh sách ngày thô từ content
    ngay_trong_thang = [row for row in content if len(row) > 3 and row[3].strip() == thang_cc]
    
    # 2. Khởi tạo danh bạ ngày (Key là mồng)
    lich_tong_hop = {}
    for i, row in enumerate(ngay_trong_thang):
        m = i + 1
        lich_tong_hop[m] = {
            "mồng": m,
            "ngay_dl": row[0],
            "can_chi": row[4],
            "cat": [],    # Danh sách các sao/điểm tốt
            "hung": [],   # Danh sách các sao/điểm xấu
            "28sao": row[7],
            "truc": row [9],
            "ghi_chu": [] # Thông tin bổ trợ (cung vị, giải nghĩa)
        }
    #st.write(lich_tong_hop)
    # 3. THU THẬP THÔNG TIN TỪ TAM KỲ
    for item in ngay_tam_ky_list:
        m = item['Mồng']
        if m in lich_tong_hop:
            lich_tong_hop[m]["cat"].append(f"Tam Kỳ ({item['Gặp Kỳ']})")
            lich_tong_hop[m]["ghi_chu"].append(f"Cung {item['Cung']}")

    # 4. (MỞ RỘNG) THU THẬP TỪ CÁC PHƯƠNG PHÁP KHÁC Ở ĐÂY
    # THU THẬP VÒNG THANH LONG (HOÀNG ĐẠO / HẮC ĐẠO) ---
    # Bước này tính xem các địa chi ngày trong tháng rơi vào sao nào dựa trên Chi tháng
    def an_vong_thanh_long(dia_chi_nhap):
        DIA_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        # 12 Sao theo thứ tự chuẩn
        DANH_SACH_12_SAO = [
            ("Thanh Long", "Hoàng Đạo"), ("Minh Đường", "Hoàng Đạo"), ("Thiên Hình", "Hắc Đạo"),
            ("Chu Tước", "Hắc Đạo"),     ("Kim Quỹ", "Hoàng Đạo"),    ("Thiên Đức", "Hoàng Đạo"),
            ("Bạch Hổ", "Hắc Đạo"),      ("Ngọc Đường", "Hoàng Đạo"), ("Thiên Lao", "Hắc Đạo"),
            ("Huyền Vũ", "Hắc Đạo"),     ("Tư Mệnh", "Hoàng Đạo"),    ("Câu Trần", "Hắc Đạo")
        ]
        BANG_KHOI_THANH_LONG = {
            "Dần": "Tý", "Thân": "Tý", "Mão": "Dần", "Dậu": "Dần",
            "Thìn": "Thìn", "Tuất": "Thìn", "Tỵ": "Ngọ", "Hợi": "Ngọ",
            "Tý": "Thân", "Ngọ": "Thân", "Sửu": "Tuất", "Mùi": "Tuất"
        }
        
        chi_chuan = dia_chi_nhap.split()[-1]
        cung_khoi_ten = BANG_KHOI_THANH_LONG.get(chi_chuan)
        if not cung_khoi_ten: return None

        idx_khoi = DIA_CHI.index(cung_khoi_ten)
        vong_sao = {}
        
        # Duyệt qua 12 cung địa chi từ Tý đến Hợi
        for i in range(12):
            ten_cung = DIA_CHI[i]
            # Tính xem cung hiện tại cách cung khởi bao nhiêu bước
            khoang_cach = (i - idx_khoi) % 12
            vong_sao[ten_cung] = DANH_SACH_12_SAO[khoang_cach]
            
        return vong_sao

    vong_sao_thang = an_vong_thanh_long(thang_cc) # Gọi hàm logic đã viết ở utils
    
    if vong_sao_thang:
        for m in lich_tong_hop:
            # 1. Lấy Địa Chi của ngày (Ví dụ: "Giáp Tý" lấy "Tý")
            chi_ngay = lich_tong_hop[m]["can_chi"].split()[-1]
            
            # 2. Tra cứu sao tương ứng trong vòng 12 sao của tháng
            sao_ten, dao_loai = vong_sao_thang.get(chi_ngay, (None, None))
            
            if sao_ten:
                if dao_loai == "Hoàng Đạo":
                    # Đưa vào danh sách Cát nếu là ngày tốt
                    lich_tong_hop[m]["cat"].append(f"Hoàng Đạo ({sao_ten})")
                else:
                    # Đưa vào danh sách Hung nếu là ngày xấu (Hắc Đạo)
                    lich_tong_hop[m]["hung"].append(f"Hắc Đạo ({sao_ten})")
  

    # E. Thu thập thông tin Tránh Khí Cùng Cực (Đại Kỵ)
    # Gọi hàm lọc ngày cùng cực để lấy danh sách các ngày vi phạm trong tháng
    ds_cung_cuc = loc_ngay_cung_cuc_trong_thang(content, thang_cc)
    for row_ky in ds_cung_cuc:
        # row_ky[0] là ngày Dương lịch, ta tìm mồng tương ứng bằng cách duyệt lich_tong_hop
        for m in lich_tong_hop:
            if lich_tong_hop[m]["ngay_dl"] == row_ky[0]:
                # Nạp vào danh sách Hung (Đại kỵ)
                noi_dung_pham = row_ky[13] # "Phạm Khí Cùng (Can...)" hoặc "Phạm Khí Cực"
                lich_tong_hop[m]["hung"].append(f"🔴 {noi_dung_pham}")
                break

    # Nạp Sao và Trực (Trực cột 9, Sao cột 7)
    for m in lich_tong_hop:
        row = ngay_trong_thang[m-1]
        if len(row) > 9:
            truc = row[9].strip()
            nguhanh_truc = row[10].strip()
            sao = row[7].strip()
            nguhanh_sao = row[8].strip()
            # Ghi vào chú thích
            lich_tong_hop[m]["ghi_chu"].append(f"Trực {truc} ({nguhanh_truc}) | Sao {sao} ({nguhanh_sao})")
            #lich_tong_hop[m]["28sao"].append(f"Sao {sao}")
            #lich_tong_hop[m]["truc"].append(f"Trực {truc}")

    # F. Thu thập thông tin 24 Ngày Kỵ & Sao Hung (Từ ghi chú file dữ liệu)
    ds_kieng_ky_file = loc_ngay_kieng_ky(content, thang_cc)
    for row_k in ds_kieng_ky_file:
        for m in lich_tong_hop:
            if lich_tong_hop[m]["ngay_dl"] == row_k[0]:
                # Nạp nội dung kiêng kỵ (Cột 11) vào danh sách Hung
                noi_dung_k = row_k[11]
                lich_tong_hop[m]["hung"].append(f"🛑 Kỵ: {noi_dung_k}")
                
                # Nếu sao đó là sao Hung (bạn có thể thêm logic lọc sao ở đây)
                # Tạm thời ghi chú tên sao vào phần chi tiết
                lich_tong_hop[m]["ghi_chu"].append(f"Ngày Sao xấu_2026")
                break
    
    # TRIỆT LỘ KHÔNG VONG:
    def tinh_logic_khong_triet(can_chi_input):
        LST_CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
        LST_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        
        can_ht, chi_ht = can_chi_input.split()
        idx_can, idx_chi = LST_CAN.index(can_ht), LST_CHI.index(chi_ht)

        # 1. Tính Không Vong (Tuần Giáp)
        idx_chi_giap = (idx_chi - idx_can) % 12
        idx_kv = [(idx_chi_giap - 2) % 12, (idx_chi_giap - 1) % 12]
        list_kv = [LST_CHI[i] for i in idx_kv]

        # 2. Tính Triệt Lộ (Theo Can - Ngũ Tý Độn)
        map_triet_lo = {
            "Giáp": ["Thân", "Dậu"], "Kỷ": ["Thân", "Dậu"],
            "Ất": ["Ngọ", "Mùi"], "Canh": ["Ngọ", "Mùi"],
            "Bính": ["Thìn", "Tỵ"], "Tân": ["Thìn", "Tỵ"],
            "Đinh": ["Dần", "Mão"], "Nhâm": ["Dần", "Mão"],
            "Mậu": ["Tý", "Sửu"], "Quý": ["Tý", "Sửu"]
        }
        list_tl = map_triet_lo.get(can_ht, [])
        
        return list_kv, list_tl

    # --- TRONG HÀM hop_nhat_lich_thang(thang_cc, ...) ---
    # Lấy quy luật của THÁNG trước
    kv_thang, tl_thang = tinh_logic_khong_triet(thang_cc)

    for m in lich_tong_hop:
        chi_ngay = lich_tong_hop[m]["can_chi"].split()[-1]
        
        # Kiểm tra ngày đó có phạm quy luật của THÁNG không
        is_kv = chi_ngay in kv_thang
        is_tl = chi_ngay in tl_thang
        
        if is_kv and is_tl:
            lich_tong_hop[m]["hung"].append("💀 ĐẠI KỴ: KHÔNG VONG TRÙNG TRIỆT")
            lich_tong_hop[m]["khi_status"] = "❌ Khí Tuyệt"
        elif is_kv:
            lich_tong_hop[m]["hung"].append("🔴 Phạm Nguyệt Không")
            lich_tong_hop[m]["khi_status"] = "😶 Vô định"
        elif is_tl:
            lich_tong_hop[m]["hung"].append("🔴 Phạm Triệt Lộ Tháng")
            lich_tong_hop[m]["khi_status"] = "🚧 Bị chặn"



    
    # Trả về kết quả cuối cùng đã được bồi đắp đầy đủ thông tin
    return lich_tong_hop

    
def display_unified_calendar(nam_canchi, thang_canchi, thang_gieng, content):
    """
    Hàm hiển thị bảng lịch thống nhất, tập hợp mọi phương pháp tính toán.
    """
    st.markdown(f"**📅 LỊCH TRÌNH CÁT HUNG - THÁNG {thang_canchi.upper()}**")

    # --- BƯỚC 1: TRIỆU HỒI DỮ LIỆU TỪ CÁC PHƯƠNG PHÁP ---
    # Gọi hàm Tam Kỳ (Hàm v4 chúng ta đã xây dựng)
    ngay_tot_tk, debug_tk = he_thong_an_que_tam_ky(nam_canchi, thang_canchi, thang_gieng, content)
    
    # (Bạn có thể gọi thêm các hàm khác ở đây trong tương lai)
    # ngay_cung_cuc = ham_tinh_cung_cuc(thang_canchi, content)
    # ngay_28_tu = ham_tinh_28_tu(content)

    # --- BƯỚC 2: HỢP NHẤT DỮ LIỆU VÀO DANH BẠ THÁNG ---
    # Gọi hàm hợp nhất đã phân tích
    lich_tong_hop = hop_nhat_lich_thang(thang_canchi, content, ngay_tot_tk)


    # --- BƯỚC 3: TRÌNH BÀY GIAO DIỆN ---
    
    # Tab 1: Bảng tổng hợp (Giao diện chính)
    with st.expander(f"📊 Bảng tra cứu tổng hợp mồng 1 - 30", expanded=True):
        data_rows = []
        for m, info in lich_tong_hop.items():
            # Xử lý hiển thị dấu chấm màu cho danh sách Cát/Hung
            cat_display = "  \n".join([f"🟢 {c}" for c in info["cat"]]) if info["cat"] else "-"
            hung_display = "  \n".join([f"🔴 {h}" for h in info["hung"]]) if info["hung"] else "-"
            ghi_chu_display = " | ".join(info["ghi_chu"]) if info["ghi_chu"] else "-"
            
            data_rows.append({
                "Mồng": f"{m}",
                "Ngày Dương": info["ngay_dl"],
                "Can Chi": info["can_chi"],
                "Điểm Cát (Tốt)": cat_display,
                "Điểm Hung (Xấu)": hung_display,
                "Chi tiết": ghi_chu_display
            })
        
        df = pd.DataFrame(data_rows)
        
        # Sử dụng st.dataframe với tính năng hiển thị Markdown (nếu cần) hoặc st.table
        # Ở đây dùng st.dataframe để người dùng có thể lọc/tìm kiếm ngày
        st.dataframe(
            df, 
            use_container_width=True, 
            hide_index=True
        )

    # --- BƯỚC 4: LỜI KHUYÊN TỔNG QUAN ---
    so_ngay_tot = len([m for m, v in lich_tong_hop.items() if v["cat"]])
    if so_ngay_tot > 0:
        st.toast(f"Tháng {thang_canchi} có {so_ngay_tot} ngày hội tụ khí Tam Kỳ!", icon="✨")
    
    return lich_tong_hop # Trả về để các Tab khác có thể dùng lại nếu cần



# KIỂM DUYỆT THÔNG TIN VÀ ĐƯA RA KẾT LUẬN NGÀY:

def he_thong_kiem_duyet_ngay_toan_dien(ngay_dl_chon, thang_cc, nam_cc, content, lich_tong_hop, ngay_tot_tk):
    """
    Duyệt toàn bộ hạng mục tính chất của ngày.
    Phân loại kỵ nặng (Ngừng dùng) và kỵ nhẹ (Cần hóa giải).
    Tiếp tục hiển thị thông tin cho đến hạng mục cuối cùng.
    """
    
    # 1. TRÍCH XUẤT DỮ LIỆU
    info_ngay = next((info for m, info in lich_tong_hop.items() if info["ngay_dl"] == ngay_dl_chon), None)
    #st.write(info_ngay)
    row_goc = next((r for r in content if str(r[0]).strip() == ngay_dl_chon), None)
    
    if not info_ngay or not row_goc:
        st.error("Không tìm thấy dữ liệu.")
        return

    can_chi_ngay = info_ngay["can_chi"]
    can_ngay = can_chi_ngay.split()[0]
    chi_ngay = can_chi_ngay.split()[1] # Lấy Chi ngày để tính Hoàng đạo
    tiet_khi = str(row_goc[5]).strip() # Lấy tiết khí từ cột index 5

    st.markdown(f"**🛠️ HỆ THỐNG KIỂM ĐỊNH KHÍ VẬN: {ngay_dl_chon}**")
    st.write(f"**Ngày:** {can_chi_ngay} | **Tháng:** {thang_cc}")
    
    # Biến cờ để theo dõi lỗi kỵ nặng
    co_loi_nang = False
    thong_tin_canh_bao = []

    # --- HẠNG MỤC 1: KHÍ CÙNG CỰC (KỴ NẶNG) ---
    st.markdown("**1. Kiểm tra Khí Cùng Cực**")
    res_cc = kiem_tra_cung_cuc_ngay_hien_tai(nam_cc, thang_cc, can_chi_ngay)
    if res_cc["ngay_pham"]:
        st.error(f"❌ PHẠM: {res_cc['ngay_pham']}")
        st.caption("Tính chất: Ngày có Khí vận suy kiệt đến cùng cực theo khí Thiên Can, không còn sức sống.")
        co_loi_nang = True
        thong_tin_canh_bao.append("Phạm Khí Cùng Cực")
    else:
        st.success("✅ Đạt: Khí vận ổn định so với chu kỳ Khí Thiên can Năm/Tháng.")
    #st.divider()

    # --- HẠNG MỤC 2: 24 NGÀY KỴ & SAO HUNG (KỴ NẶNG) ---
    st.markdown("**2. Kiểm tra Ngày Kỵ & Nhị Thập Bát Tú**")
    res_ky = check_ngay_ky_2026(ngay_dl_chon, content)
    if res_ky["co_thong_tin"] and any(k in res_ky["noi_dung"] for k in ["Kỵ Lập Trạch", "Đại Hung"]):
        st.error(f"❌ PHẠM: {res_ky['noi_dung']}")
        st.caption(f"Tính chất: Ngày kỵ cố định/Sao Hung ({res_ky['sao']}). Sát khí mạnh.")
        co_loi_nang = True
        thong_tin_canh_bao.append("Phạm Ngày Kỵ/Sao Hung")
    else:
        st.success(f"✅ Đạt: Không phạm hệ thống 24 Ngày Kỵ và Sao Hung theo Nhị Thập Bát Tú năm 2026. Sao chiếu Ngày là sao {res_ky['sao'] if res_ky['co_thong_tin'] else 'Bình hòa'}")
    #st.divider()

    # --- HẠNG MỤC 3: TRIỆT LỘ KHÔNG VONG & VÒNG HOÀNG ĐẠO (BÙ TRỪ) ---
    st.markdown("**3. Triệt Lộ - Không Vong & Hoàng Đạo**")
    kv_tuan, tl_can = tinh_logic_khong_triet(thang_cc)
    loi_tlkv = chi_ngay in kv_tuan or chi_ngay in tl_can
    
    # Kiểm tra Hoàng Đạo/Hắc Đạo (Hàm giả định dựa trên bảng tra của bạn)
    # Giả sử info_ngay là biến chứa kết quả JSON bạn đã nêu
    danh_sach_sao_cat = info_ngay.get("cat", [])

    # Kiểm tra xem có chữ "Hoàng Đạo" trong bất kỳ phần tử nào của danh sách cat không
    is_hoang_dao = any("Hoàng Đạo" in sao for sao in danh_sach_sao_cat)
    #st.write(is_hoang_dao) # Kết quả sẽ trả về True nếu có "Hoàng Đạo (Thanh Long)"
    
    # Lấy thông tin Tam Kỳ để tính toán bù trừ sớm
    res_tk = kiem_tra_ngay_hien_tai_co_ky(ngay_dl_chon, ngay_tot_tk)
    is_co_tam_ky = res_tk["is_ky"]

    col_hd, col_tl = st.columns(2)
    with col_hd:
        if is_hoang_dao: st.success("✨ Ngày Hoàng Đạo")
        else: st.warning("🌑 Ngày Hắc Đạo")
    with col_tl:
        if loi_tlkv: st.error("🚧 Phạm Triệt Lộ/Không Vong")
        else: st.success("✅ Ngày không phạm Triệt Lộ Không Vong")

    # Dẫn luận bù trừ Hoàng Đạo
    if (loi_tlkv or not is_hoang_dao) and is_co_tam_ky:
        st.info("💡 **Bù trừ:** Lỗi Ngày phạm Triệt Không/Hắc Đạo đã được Bát Tiết Tam Kỳ hóa giải thành công.")
        ngay_dung_duoc = True
    elif loi_tlkv and not is_co_tam_ky and is_hoang_dao:
        st.warning("💡 **Bù trừ:** Ngày phạm Triệt Không, không có Tam Kỳ nhưng gặp Hoàng Đạo nên có thể dùng tạm.")
        ngay_dung_duoc = True
    elif loi_tlkv and not is_co_tam_ky and not is_hoang_dao:
        st.error("❌ **Kết quả:** Ngày phạm Triệt Không/Hắc Đạo, không có yếu tố hóa giải. Hung hiểm hội tụ")
        ngay_dung_duoc = False
    else:
        ngay_dung_duoc = not loi_tlkv
    #st.divider()

    # --- HẠNG MỤC 4: HỘI TỤ BÁT TIẾT TAM KỲ (VŨ KHÍ CẤP NGÀY) ---
    st.markdown("**4. Hội tụ Bát Tiết Tam Kỳ**")
    if is_co_tam_ky:
        st.info(f"🌟 XÁC NHẬN: Gặp {res_tk['loai_ky']} Kỳ tại {res_tk['cung']}")
        st.caption("Ghi chú: Đây là 'Thanh khí' tối thượng giúp bù đắp và hóa giải Hung sát của các lỗi Tuần Triệt Không Vong, Hắc Đạo.")
    else:
        st.info("Ngày này không hội tụ Tam Kỳ.")
    #st.divider()

    # --- HẠNG MỤC 5: GIỜ CÁT & BỘ LỌC CÙNG CỰC GIỜ ---
    st.markdown("**5. Giờ Quý Nhân, Hoàng Đạo & Bộ Lọc Cùng Cực, Triệt Lộ Không Vong**")
    # 1. Định nghĩa bảng tra nội bộ
    lst_chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
    map_nguyet_tuong = {
        "Vũ Thuỷ": "Hợi", "Kinh Trập": "Hợi", "Xuân Phân": "Tuất", "Thanh Minh": "Tuất",
        "Cốc Vũ": "Dậu", "Lập Hạ": "Dậu", "Tiểu Mãn": "Thân", "Mang Chủng": "Thân",
        "Hạ Chí": "Mùi", "Tiểu Thử": "Mùi", "Đại Thử": "Ngọ", "Lập Thu": "Ngọ",
        "Xử Thử": "Tỵ", "Bạch Lộ": "Tỵ", "Thu Phân": "Thìn", "Hàn Lộ": "Thìn",
        "Sương Giáng": "Mão", "Lập Đông": "Mão", "Tiểu Tuyết": "Dần", "Đại Tuyết": "Dần",
        "Đông Chí": "Sửu", "Tiểu Hàn": "Sửu", "Đại Hàn": "Tý", "Lập Xuân": "Tý"
    }
    map_quy_nhan = {
        "Giáp": {"D": "Mùi", "A": "Sửu"}, "Ất": {"D": "Thân", "A": "Tý"},
        "Bính": {"D": "Dậu", "A": "Hợi"}, "Đinh": {"D": "Hợi", "A": "Dậu"},
        "Mậu": {"D": "Sửu", "A": "Mùi"}, "Kỷ": {"D": "Tý", "A": "Thân"},
        "Canh": {"D": "Sửu", "A": "Mùi"}, "Tân": {"D": "Dần", "A": "Ngọ"},
        "Nhâm": {"D": "Mão", "A": "Tỵ"}, "Quý": {"D": "Tỵ", "A": "Mão"}
    }
    DAY_HOURS = ["Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân"]
    NIGHT_HOURS = ["Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần"]

    # 2. Tính toán biến T, H, Q
    tuong_chi = map_nguyet_tuong.get(tiet_khi, "Không xác định")
    if tuong_chi == "Không xác định":
        st.warning(f"Không xác định được Nguyệt Tướng cho tiết khí: {tiet_khi}")
        can_dung_duong = can_dung_am = False
    else:
        T = lst_chi.index(tuong_chi)
        H = 11 # Thiên Môn tại Hợi
        Q_duong = lst_chi.index(map_quy_nhan[can_ngay]["D"])
        Q_am = lst_chi.index(map_quy_nhan[can_ngay]["A"])

        gio_duong = lst_chi[(H - Q_duong + T) % 12]
        gio_am = lst_chi[(H - Q_am + T) % 12]

        can_dung_duong = gio_duong in DAY_HOURS
        can_dung_am = gio_am in NIGHT_HOURS

        st.info(f"Tiết khí: **{tiet_khi}** (Nguyệt Tướng: {tuong_chi})")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Dương Quý:** Giờ {gio_duong}")
            if can_dung_duong:
                st.success("✅ Đắc thời (Ban ngày)")
            else:
                st.error("❌ Lỗi thời (Phạm đêm)")
        with col2:
            st.write(f"**Âm Quý:** Giờ {gio_am}")
            if can_dung_am:
                st.success("✅ Đắc thời (Ban đêm)")
            else:
                st.error("❌ Lỗi thời (Phạm ngày)")

    # 3. Lọc Giờ Khí Cùng Cực & Triệt Lộ Không Vong của Ngày
    st.write("**PHÂN TÍCH & LỰA CHỌN GIỜ DỤNG SỰ**")
    
    # A. Xác định Can Cùng/Cực của ngày hiện tại
    can_cung_ngay, can_cuc_ngay = xac_dinh_cung_cuc(can_ngay) 
    ds_gio_ky_cung_cuc = []
    
    # B. Xác định Giờ Triệt Lộ & Không Vong (Logic từ Can và Chi ngày)
    # Tận dụng hàm tính toán logic đã có trong hệ thống của bạn
    kv_gio, tl_gio = tinh_logic_khong_triet(can_chi_ngay) 
    ds_gio_pham_nang = []

    # C. Lấy danh sách giờ Hoàng Đạo từ vòng Thanh Long

    ds_gio_hoang_dao = lay_ds_gio_hoang_dao(chi_ngay)
    #st.write(ds_gio_hoang_dao)

    # Duyệt 12 giờ để phân tích thứ tự ưu tiên
    for chi in lst_chi:
        # A. Xác định Can giờ (Ngũ Tý Độn)
        can_gio = tinh_ngu_ty_don(can_ngay, chi)
        
        # B. Kiểm tra các lỗi phạm
        is_cung_cuc = (can_gio == can_cung_ngay or can_gio == can_cuc_ngay)
        is_triet_lo = chi in tl_gio
        is_khong_vong = chi in kv_gio
        is_hoang_dao = chi in ds_gio_hoang_dao
        
        if is_cung_cuc: ds_gio_ky_cung_cuc.append(chi)
        if is_triet_lo or is_khong_vong: ds_gio_pham_nang.append(chi)

        # C. Xác định tính chất Giờ (Ưu tiên Quý Nhân Đắc Thời)
        is_quy_nhan_dac_thoi = (chi == gio_duong and can_dung_duong) or (chi == gio_am and can_dung_am)

        # D. Hiển thị giờ theo thứ tự ưu tiên và logic hóa giải
        if is_quy_nhan_dac_thoi or is_hoang_dao:
            col_t1, col_t2 = st.columns([1, 3])
            
            with col_t1:
                if is_quy_nhan_dac_thoi:
                    st.markdown(f"🌟 **Giờ {chi}**")
                    st.caption("**(Quý Nhân Đắc Thời)**")
                else:
                    st.markdown(f"✨ **Giờ {chi}**")
                    st.caption("(Hoàng Đạo)")
            
            with col_t2:
                # --- LOGIC PHÁN QUYẾT TỪNG GIỜ ---
                
                # 1. Nếu là Giờ Quý Nhân Đắc Thời -> Hóa giải được Triệt Lộ/Không Vong/Hắc Đạo
                if is_quy_nhan_dac_thoi:
                    if is_cung_cuc:
                        st.warning(f"⚠️ Quý Nhân lâm hạn: Giờ phạm Khí {can_gio} (Cùng Cực). Quý Nhân bị chế ngự, cân nhắc kỹ.")
                    elif is_triet_lo or is_khong_vong or not is_hoang_dao:
                        loi_gi = []
                        if is_triet_lo: loi_gi.append("Triệt Lộ")
                        if is_khong_vong: loi_gi.append("Không Vong")
                        if not is_hoang_dao: loi_gi.append("Hắc Đạo")
                        st.success(f"✅ Hóa Giải: Quý Nhân đắc thời đã hóa giải lỗi {', '.join(loi_gi)}. Dùng được.")
                    else:
                        st.success("✅ Đại Cát: Quý Nhân đắc thời, khí thông, dụng sự tốt nhất.")

                # 2. Nếu chỉ là Giờ Hoàng Đạo (Ưu tiên 2)
                elif is_hoang_dao:
                    if is_cung_cuc:
                        st.warning(f"⚠️ Cẩn trọng: Giờ Hoàng Đạo phạm Khí {can_gio} (Cùng Cực). Cân nhắc kỹ.")
                    elif is_triet_lo or is_khong_vong:
                        loi_gi = "Triệt Lộ" if is_triet_lo else "Không Vong"
                        if is_triet_lo and is_khong_vong: loi_gi = "Triệt Lộ & Không Vong"
                        st.warning(f"🚧 Cản trở: Giờ Hoàng Đạo nhưng phạm {loi_gi}. Cần Quý Nhân mới hóa giải được.")
                    else:
                        st.success("✅ Giờ Cát lành: Hoàng Đạo khí thông, dụng sự tốt.")

    # --- TỔNG KẾT PHÁN QUYẾT (CẬP NHẬT LUẬT BÙ TRỪ) ---
    #st.divider()
    st.markdown("🚩 **PHÁN QUYẾT TỔNG THỂ**")

    if co_loi_nang:
        st.error(f"⚠️ Ngày PHẠM {res_cc['ngay_pham']}. **KHÔNG NÊN DÙNG:** Cát không bù được Hung cấp độ Đại Kỵ (cho dù có gặp Tam Kỳ cũng khó hoá giải nổi). Nếu Ngày dụng sự không tránh được, nên chọn ưu tiên Giờ Quý Nhân, kế là Giờ Hoàng Đạo mà không phạm Cùng Cực hay Triệt Không mới giảm thiểu Hung sát gây ra")
    elif not ngay_dung_duoc:
        st.error("❌ **KHÔNG NÊN DÙNG:** Ngày Phạm kỵ Tuần Triệt Không Vong/Hắc Đạo mà không có yếu tố hóa giải Tam Kỳ. Nếu không tránh được nên chọn Giờ Quý Nhân, kế là Giờ Hoàng Đạo không phạm Cùng Cực hay Triệt Không mới giảm thiểu Hung sát gây ra")
    elif ngay_dung_duoc and loi_tlkv:
        st.warning("⚠️ **CẨN TRỌNG:** Ngày dùng được nhờ bù trừ (Tam Kỳ áp chế Triệt Không/Hắc Đạo), nhưng nên chọn giờ Cát (Qúy Nhân kế đến Hoàng Đạo) không phạm Cùng Cực, không rơi vào Triệt Lộ Không Vong.")
    else:
        st.success("🌟 **THUẬN LỢI:** Ngày sạch kỵ, khí vận hanh thông. Nếu có phạm Tiểu Hung, vẫn có Cát Khánh từ Ngày Tam Kỳ hay Giờ Quý Nhân - Hoàng Đạo đủ lực áp chế")
        


def tab_moi_su_dung_bien():
    # Kiểm tra xem "kho" đã có hàng chưa
    if 'content' in st.session_state:
        
        # GỌI BIẾN ĐỂ SỬ DỤNG
        # Bạn có thể gán lại tên ngắn gọn để dễ dùng trong hàm

        content = st.session_state.content 
        lich_tong_hop = st.session_state.lich_tong_hop
        ngay_tot = st.session_state.tam_ky_data
        nam_canchi = st.session_state.nam_ht
        thang_canchi = st.session_state.thang_ht
        ngay_thang_nam = st.session_state.ngay_ht
        
        #st.write(content[0])
        #st.warning(lich_tong_hop)
        #st.write(ngay_tot)  
        #st.write(nam_canchi)
        #st.write(thang_canchi)
        #st.write(ngay_thang_nam)  

        # Ví dụ: Sử dụng biến 'lich' để tìm thông tin một ngày khác mà không cần tính toán lại toàn bộ
        #ngay_can_tim = "16/03/2026"
        #thong_tin = next((v for k, v in lich_tong_hop.items() if v['ngay_dl'] == ngay_can_tim), None)
        
        #if thong_tin:
        #    st.write(f"Dữ liệu ngày {ngay_can_tim} lấy từ kho: {thong_tin['can_chi']}")
            
        # Gọi hàm kiểm duyệt với các biến vừa lấy từ kho
        
        #he_thong_kiem_duyet_ngay_toan_dien(ngay_thang_nam, thang_canchi, nam_canchi, content, lich_tong_hop, ngay_tot)

    else:
        st.error("Dữ liệu trống! Hãy chạy Tab CHỌN NGÀY GIỜ TỐT trước.")
