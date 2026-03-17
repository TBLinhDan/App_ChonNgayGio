import streamlit as st

    
#cho phép người dùng tải tệp tin từ máy chủ về máy cá nhân chỉ với một cú click chuột.    
def bmdp_txt():
    file_path = './Data Files/BÁT MÔN ĐỘN PHÁP.txt'
    
    # Mở file và đọc nội dung
    with open(file_path, 'r', encoding='UTF-8') as f:
        data = f.read()
    
    # Sử dụng biến data đã lưu nội dung
    st.download_button(
        label="Download", 
        data=data, 
        file_name="Bát_Môn_Độn_Pháp.txt",
        mime="text/plain"
    )

def bmdp_diengiai_txt():
    file_path = './Data Files/BátMônĐộnPháp_DiễnGiải.txt'
    
    try: #try-except: Giúp ứng dụng của bạn không bị "đứng" nếu file chẳng may bị xóa hoặc đổi tên.
        with open(file_path, 'r', encoding='UTF-8') as f:
            content = f.read() #Đọc và lưu nội dung vào biến content
        
        st.download_button(
            label="Click Here",
            data=content,
            file_name="BátMônĐộnPháp_DiễnGiải.txt", #thêm .txt vào file_name giúp hệ điều hành của người dùng nhận diện ngay đây là tệp văn bản.
            mime="text/plain" #Đảm bảo tệp tải về được xử lý như một tệp văn bản thuần túy.
        )
    except FileNotFoundError:
        st.error("Không tìm thấy tệp tin. Vui lòng kiểm tra lại đường dẫn!")


#Mở một tệp tin văn bản (note.txt) (có hỗ trợ tiếng Việt), đọc toàn bộ nội dung bên trong và hiển thị nó lên giao diện ứng dụng web.
def doc_file2(duong_dan):
    try:
        with open(duong_dan, 'r', encoding='UTF-8') as f:
            content = f.read()
            st.write(content) #Hiển thị nội dung đã đọc được lên giao diện người dùng của trang web (Streamlit).
    except FileNotFoundError:
        st.error("Không tìm thấy file note.txt! Bạn kiểm tra lại đường dẫn nhé.")


def doc_file1(duong_dan):
    # Cách tối ưu: Duyệt trực tiếp trên f, không dùng readlines()
    with open(duong_dan, 'r', encoding='UTF-8') as f:
        for line in f: #Đọc từng dòng một
            st.text(line.strip()) # .strip() giúp loại bỏ các ký tự xuống dòng thừa


#tạo ra đường dẫn đầy đủ tới một tệp tin văn bản dựa trên tên tệp mà bạn cung cấp.
#nối chuỗi ghép ba thành phần lại với nhau: thư mục chứa file, tên file truyền vào, và đuôi mở rộng .txt
def path_data(title):
    # Loại bỏ đuôi .txt nếu người dùng lỡ thêm vào
    clean_title = title.replace(".txt", "")
    return f"./Data Files/{clean_title}.txt"

def doc_file(duong_dan, delimiter=','):
    """
    Đọc tệp tin và trả về nội dung dưới dạng danh sách các dòng đã được tách.
    - duong_dan: Đường dẫn đến tệp tin của bạn.
    - delimiter: Dấu phân cách các cột (mặc định là dấu phẩy).
    """
    try:
        with open(duong_dan, 'r', encoding="utf-8") as file:
            # Sử dụng List Comprehension để làm sạch và tách dữ liệu ngay khi đọc
            du_lieu = [[item.strip() for item in line.strip().split(delimiter)] for line in file]
        return du_lieu
    except FileNotFoundError:
        st.error(f"Lỗi: Không tìm thấy tệp tại đường dẫn: {duong_dan}")
        return None
    except Exception as e:
        st.error(f"Có lỗi xảy ra trong quá trình đọc tệp: {e}")
        return None

def lay_thong_tin(name, title):
            try:
                PATH_DATA = path_data(title)
                du_lieu = doc_file(PATH_DATA, delimiter=';')
                if du_lieu:
                    for thongtin in du_lieu:
                        if thongtin[0] == name:
                            return thongtin
                else:
                    return None
            except Exception as e:
                st.write(f"Có lỗi xảy ra: {e}")
                return None


def doc_file(duong_dan, delimiter=';'):
    """
    Đọc tệp tin và trả về nội dung dưới dạng danh sách các dòng đã được tách.
    - duong_dan: Đường dẫn đến tệp tin của bạn.
    - delimiter: Dấu phân cách các cột (mặc định là dấu phẩy).
    """
    try:
        with open(duong_dan, 'r', encoding="utf-8") as file:
            # Sử dụng List Comprehension để làm sạch và tách dữ liệu ngay khi đọc
            du_lieu = [[item.strip() for item in line.strip().split(delimiter)] for line in file]
        return du_lieu
    except FileNotFoundError:
        st.error(f"Lỗi: Không tìm thấy tệp tại đường dẫn: {duong_dan}")
        return None
    except Exception as e:
        st.error(f"Có lỗi xảy ra trong quá trình đọc tệp: {e}")
        return None
    


#tìm kiếm một "bản ghi" cụ thể dựa trên tên (name) trong một tệp dữ liệu (title).
def lay_thong_tin_cached(name, title, col_index=0):
    """
    Cải tiến: Tìm kiếm 'name' tại một cột (col_index) bất kỳ trong dòng dữ liệu.
    - col_index: Vị trí phần tử trong list dòng (mặc định là 0).
    """
    def path_data(title):
        clean_title = title.replace(".txt", "")
        return f"./Data Files/{clean_title}.txt"

    def load_data_once(path):
        if 'data_cache' not in st.session_state:
            # st.info("Đang nạp dữ liệu vào bộ nhớ tạm...") 
            st.session_state['data_cache'] = doc_file(path, delimiter=',')
        return st.session_state['data_cache']

    try:
        path = path_data(title)
        du_lieu = load_data_once(path)
            
        if du_lieu:
            search_name = str(name).strip().lower() # Chuẩn hóa từ khóa tìm kiếm
            for thongtin in du_lieu:
                # Kiểm tra dòng có đủ độ dài và phần tử tại col_index có khớp không
                if len(thongtin) > col_index:
                    target_value = str(thongtin[col_index]).strip().lower()
                    if target_value == search_name:
                        return thongtin
        return None
    except Exception as e:
        st.error(f"Lỗi tìm kiếm dữ liệu: {e}")
        return None

def lay_thong_tin_cached1(name, title, col_index=0):
    """
    Cải tiến: Tìm kiếm 'name' tại một cột (col_index) bất kỳ trong dòng dữ liệu.
    - col_index: Vị trí phần tử trong list dòng (mặc định là 0).
    """
    def path_data(title):
        clean_title = title.replace(".txt", "")
        return f"./Data Files/{clean_title}.txt"

    def load_data_once(path):
        if 'data_cache' not in st.session_state:
            # st.info("Đang nạp dữ liệu vào bộ nhớ tạm...") 
            st.session_state['data_cache'] = doc_file(path, delimiter=';')
        return st.session_state['data_cache']

    try:
        path = path_data(title)
        du_lieu = load_data_once(path)
            
        if du_lieu:
            search_name = str(name).strip().lower() # Chuẩn hóa từ khóa tìm kiếm
            for thongtin in du_lieu:
                # Kiểm tra dòng có đủ độ dài và phần tử tại col_index có khớp không
                if len(thongtin) > col_index:
                    target_value = str(thongtin[col_index]).strip().lower()
                    if target_value == search_name:
                        return thongtin
        return None
    except Exception as e:
        st.error(f"Lỗi tìm kiếm dữ liệu: {e}")
        return None

"""
Tóm tắt luồng xử lý:
Đầu vào: Nhận danh sách tổng và tên tháng cần lọc.
Vòng lặp: Đi qua từng dòng (row) trong danh sách.
Kiểm tra: Nếu dòng hợp lệ ➡️ So khớp tháng ➡️ Kiểm tra nội dung cột 11.
Lưu trữ: Nếu đạt cả 2 điều kiện, "nhặt" cả dòng đó bỏ vào danh sách ket_qua.
Đầu ra: Trả về một danh sách mới chỉ chứa các ngày có thông tin kiêng kỵ.
"""
def loc_ngay_kieng_ky(data_list, data_tim_kiem):
    """
    Lọc dữ liệu từ biến content đã có sẵn.
    - data_list: Biến content (mảng 2 chiều)
    - data_tim_kiem: Tên tháng muốn lọc (VD: "Canh Dần")
    """
    ket_qua = []
    
    # Chuẩn hóa tên tháng cần tìm để so sánh chính xác
    data_tim_kiem = str(data_tim_kiem).strip().lower()

    for row in data_list:
        # Kiểm tra độ dài dòng để tránh lỗi index (Cột 11 là Kiêng Kỵ, Cột 3 là Tháng)
        if len(row) > 11:
            thang_trong_file = str(row[3]).strip().lower()
            noi_dung_ky = str(row[11]).strip()
            
            # Điều kiện: Khớp tháng VÀ nội dung kiêng kỵ không rỗng
            if thang_trong_file == data_tim_kiem and noi_dung_ky != "":
                ket_qua.append(row)
                
    return ket_qua

def truy_van_du_lieu_lich(data_list, gia_tri_tim_kiem, cot_tim_kiem=3, cot_trich_xuat=11, loc_rong=True):
    """
    Hàm tổng quát để lọc và trích xuất dữ liệu từ content.
    - data_list: Mảng 2 chiều (content)
    - gia_tri_tim_kiem: Giá trị muốn khớp (VD: "Canh Dần")
    - cot_tim_kiem: Chỉ số cột để đối chiếu (Mặc định là cột 3 - Tháng)
    - cot_trich_xuat: Chỉ số cột muốn lấy dữ liệu (Mặc định cột 11 - Kiêng kỵ)
    - loc_rong: Nếu True, sẽ bỏ qua các dòng có cột trích xuất bị trống.
    """
    ket_qua = []
    
    # Chuẩn hóa giá trị tìm kiếm
    val_search = str(gia_tri_tim_kiem).strip().lower()

    for row in data_list:
        # Kiểm tra độ dài dòng để tránh lỗi index
        max_idx = max(cot_tim_kiem, cot_trich_xuat)
        
        if len(row) > max_idx:
            noi_dung_doi_chieu = str(row[cot_tim_kiem]).strip().lower()
            noi_dung_lay_ra = str(row[cot_trich_xuat]).strip()
            
            # Điều kiện 1: Khớp giá trị tìm kiếm
            if noi_dung_doi_chieu == val_search:
                # Điều kiện 2: Kiểm tra rỗng nếu có yêu cầu
                if loc_rong and noi_dung_lay_ra == "":
                    continue
                
                # Trả về nguyên dòng row (hoặc bạn có thể tùy chỉnh chỉ trả về giá trị cột)
                ket_qua.append(row)
                
    return ket_qua

def xac_dinh_cung_cuc(can_duong_lenh):
    """
    Đầu vào: Tên Can (String)
    Đầu ra: (Can Cùng, Can Cực)
    """
    lst_can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    
    # Chuẩn hóa đầu vào
    can_duong_lenh = can_duong_lenh.strip()
    
    if can_duong_lenh not in lst_can:
        return None, None
        
    idx = lst_can.index(can_duong_lenh)
    
    # Khí tới Cùng: Cách 7 vị trí (idx + 7)
    can_cung = lst_can[(idx + 7) % 10]
    
    # Khí tới Cực: Cách 2 vị trí (idx + 2)
    can_cuc = lst_can[(idx + 2) % 10]
    
    return can_cung, can_cuc

"""
      Giáp đương lệnh: Tân tới Cùng, Bính tới Cực
      Ất đương lệnh: Nhâm tới Cùng, Đinh tới Cực
      Bính đương lệnh: Quý tới Cùng, Mậu tới Cực
      Đinh đương lệnh: Giáp tới Cùng, Kỷ tới Cực
      Mậu đương lệnh: Canh tới Cùng, Ất tới Cực
      Kỷ đương lệnh: Bính tới Cùng, Tân tới Cực
      Canh đương lệnh: Đinh tới Cùng, Nhâm tới Cực
      Tân đương lệnh: Mậu tới Cùng, Quý tới Cực
      Nhâm đương lệnh: Kỷ tới Cùng, Giáp tới Cực
      Quý đương lệnh: Ất tới Cùng, Canh tới Cực
"""
def loc_ngay_cung_cuc_trong_thang(data_list, ten_thang_full):
    """
    Lọc các ngày phạm Khí Cùng Cực TRONG MỘT THÁNG cụ thể.
    - ten_thang_full: Tên đầy đủ của tháng (VD: "Canh Dần")
    """
    # 1. Tách lấy Can của tháng (VD: "Canh")
    can_thang = ten_thang_full.split()[0]
    
    # 2. Xác định cặp Can kỵ (Sử dụng hàm xac_dinh_cung_cuc đã viết ở trên)
    can_khi_cung, can_khi_cuc = xac_dinh_cung_cuc(can_thang)
    
    if not can_khi_cung:
        return []

    ket_qua_loc = []
    ten_thang_search = ten_thang_full.strip().lower()

    for row in data_list:
        # Kiểm tra dòng hợp lệ (ít nhất 5 cột để lấy Ngày Can Chi ở cột 4)
        if len(row) > 4:
            thang_trong_file = str(row[3]).strip().lower()
            
            # BƯỚC 1: Phải đúng là tháng đang xét
            if thang_trong_file == ten_thang_search:
                
                # BƯỚC 2: Kiểm tra Can Ngày (Cột 4)
                can_ngay = row[4].strip().split()[0]
                
                if can_ngay == can_khi_cung or can_ngay == can_khi_cuc:
                    row_copy = list(row)
                    loai_kỵ = "Khí Cùng" if can_ngay == can_khi_cung else "Khí Cực"
                    # Ghi chú thêm vào cuối dòng để hiển thị
                    row_copy.append(f"Phạm {loai_kỵ} ({can_ngay})")
                    ket_qua_loc.append(row_copy)
                    
    return ket_qua_loc

def loc_Thang_cung_cuc(data_list, can_nam_nhap):
    """
    Lọc các tháng trong năm có Can phạm Khí Cùng Cực của Can Năm.
    - data_list: Biến content chứa dữ liệu năm.
    - can_nam_nhap: Can của năm đang xét (VD: "Bính").
    """
    can_cung, can_cuc = xac_dinh_cung_cuc(can_nam_nhap)
    ket_qua = []
    thang_da_them = set() # Tránh trùng lặp vì một tháng có nhiều ngày

    for row in data_list:
        if len(row) > 3:
            ten_thang_full = row[3].strip()
            can_thang = ten_thang_full.split()[0]
            
            if (can_thang == can_cung or can_thang == can_cuc) and ten_thang_full not in thang_da_them:
                loai_ky = "Khí Cùng" if can_thang == can_cung else "Khí Cực"
                ket_qua.append({
                    "Tháng": ten_thang_full,
                    "Loại": loai_ky,
                    "Can vi phạm": can_thang
                })
                thang_da_them.add(ten_thang_full)
    return ket_qua

def loc_Gio_cung_cuc(can_ngay_nhap, ds_12_gio_can_chi):
    """
    Lọc các giờ trong ngày phạm Khí Cùng Cực của Can Ngày.
    - can_ngay_nhap: Can của ngày đang xét (VD: "Giáp").
    - ds_12_gio_can_chi: List 12 giờ (Tý, Sửu...) của ngày đó.
    """
    can_cung, can_cuc = xac_dinh_cung_cuc(can_ngay_nhap)
    ket_qua_gio = []

    for gio_full in ds_12_gio_can_chi:
        can_gio = gio_full.split()[0]
        if can_gio == can_cung or can_gio == can_cuc:
            loai_ky = "Khí Cùng" if can_gio == can_cung else "Khí Cực"
            ket_qua_gio.append(f"{gio_full} ({loai_ky})")
            
    return ket_qua_gio


# TRIỆT LỘ KHÔNG VONG
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

def kiem_tra_trietkhong_ngay_hien_tai(ngay_canchi, thang_canchi):
    """
    Kiểm tra toàn diện một ngày dựa trên 2 hệ quy chiếu:
    1. Nội tại: Ngày đó gây ra Triệt/Không cho giờ nào?
    2. Hệ thống: Ngày đó có bị Tháng 'triệt' hay 'không' hay không?
    """
    # Lấy logic chung (đã thống nhất: KV theo Tuần, TL theo Can)
    def get_logic(cc):
        kv, tl = tinh_logic_khong_triet(cc) # Hàm đã viết ở turn trước
        return kv, tl

    can_ngay, chi_ngay = ngay_canchi.split()
    
    # 1. TÍNH TOÁN
    kv_cua_thang, tl_cua_thang = get_logic(thang_canchi)
    kv_cua_ngay, tl_cua_ngay = get_logic(ngay_canchi)

    st.markdown(f"**🧩 Khí vận TRIỆT LỘ KHÔNG VONG**")

    # --- PHẦN A: KIỂM TRA NGÀY ĐÓ CÓ PHẠM LUẬT CỦA THÁNG KHÔNG ---
    st.markdown(f"1. Vị thế của Ngày **{ngay_canchi}**/Tháng **{thang_canchi}**")
    col1, col2 = st.columns(2)
    
    with col1:
        is_nguyet_kv = chi_ngay in kv_cua_thang
        status_kv = "🔴 PHẠM" if is_nguyet_kv else "✅ Không"
        st.write(f"**Phạm Không Vong của Tháng:** {status_kv}")
        if is_nguyet_kv:
            st.caption(f"(Do tháng {thang_canchi} trống tại {', '.join(kv_cua_thang)})")

    with col2:
        is_nguyet_tl = chi_ngay in tl_cua_thang
        status_tl = "🔴 PHẠM" if is_nguyet_tl else "✅ Không"
        st.write(f"**Phạm Triệt Lộ của Tháng:** {status_tl}")
        if is_nguyet_tl:
            st.caption(f"(Do Can {thang_canchi.split()[0]} của tháng chặn tại {', '.join(tl_cua_thang)})")

    # --- PHẦN C: TỔNG KẾT ---
    if is_nguyet_kv or is_nguyet_tl:
        if is_nguyet_kv and is_nguyet_tl:
            st.error("💀 **Kết Luận:** Ngày này là điểm 'Khí Tuyệt' của tháng theo phép tính Triệt Lộ Không Vong (nên Tránh)")
        else:
            st.warning("⚠️ **Kết Luận:** Ngày này bị lỗi khí Triệt Lộ Không Vong từ cấp Tháng.")
    else:
        st.success("🌟 **Kết Luận:** Ngày này có vị thế tốt so với Tháng, khí vận theo phép tính Triệt Lộ Không Vong thông suốt.")


    # --- PHẦN B: ẢNH HƯỞNG CỦA NGÀY ĐẾN CÁC GIỜ (NỘI TẠI) ---
    st.markdown("**2. Sức ảnh hưởng nội tại của Ngày**")
    st.info(f"Trong ngày {ngay_canchi}, khí vận tự thân sẽ tạo ra các vùng trống/chặn sau:")
    
    st.write(f"👉 **Giờ Không Vong (Rỗng):** {', '.join(kv_cua_ngay)}")
    st.write(f"👉 **Giờ Triệt Lộ (Chặn):** {', '.join(tl_cua_ngay)}")


# KIỂM TRA KHI CÙNG CỰC Ngày Hiện tại
def kiem_tra_cung_cuc_ngay_hien_tai(nam_canchi, thang_canchi, ngay_canchi):
    """
    Kiểm tra ngày hiện tại theo 2 cấp độ Khí Cùng Cực:
    1. Cấp Năm: Tháng này có phạm Cùng Cực của Năm không?
    2. Cấp Tháng: Ngày này có phạm Cùng Cực của Tháng không?
    """
    can_nam = nam_canchi.split()[0]
    can_thang = thang_canchi.split()[0]
    can_ngay = ngay_canchi.split()[0]

    # --- TẦNG 1: KIỂM TRA THÁNG ĐỐI VỚI NĂM ---
    can_cung_nam, can_cuc_nam = xac_dinh_cung_cuc(can_nam)
    pham_thang = None
    if can_thang == can_cung_nam: pham_thang = "Khí Cùng của Năm"
    if can_thang == can_cuc_nam: pham_thang = "Khí Cực của Năm"

    # --- TẦNG 2: KIỂM TRA NGÀY ĐỐI VỚI THÁNG ---
    can_cung_thang, can_cuc_thang = xac_dinh_cung_cuc(can_thang)
    pham_ngay = None
    if can_ngay == can_cung_thang: pham_ngay = "Khí Cùng của Tháng"
    if can_ngay == can_cuc_thang: pham_ngay = "Khí Cực của Tháng"

    return {
        "thang_pham": pham_thang,
        "ngay_pham": pham_ngay,
        "can_ky_thang": (can_cung_nam, can_cuc_nam),
        "can_ky_ngay": (can_cung_thang, can_cuc_thang)
    }

def display_cung_cuc_ngay_hien_tai(nam_canchi, thang_canchi, ngay_canchi):

    def kiem_tra_cung_cuc_ngay_hien_tai(nam_canchi, thang_canchi, ngay_canchi):
        """
        Kiểm tra ngày hiện tại theo 2 cấp độ Khí Cùng Cực:
        1. Cấp Năm: Tháng này có phạm Cùng Cực của Năm không?
        2. Cấp Tháng: Ngày này có phạm Cùng Cực của Tháng không?
        """
        can_nam = nam_canchi.split()[0]
        can_thang = thang_canchi.split()[0]
        can_ngay = ngay_canchi.split()[0]

        # --- TẦNG 1: KIỂM TRA THÁNG ĐỐI VỚI NĂM ---
        can_cung_nam, can_cuc_nam = xac_dinh_cung_cuc(can_nam)
        pham_thang = None
        if can_thang == can_cung_nam: pham_thang = "Khí Cùng của Năm"
        if can_thang == can_cuc_nam: pham_thang = "Khí Cực của Năm"

        # --- TẦNG 2: KIỂM TRA NGÀY ĐỐI VỚI THÁNG ---
        can_cung_thang, can_cuc_thang = xac_dinh_cung_cuc(can_thang)
        pham_ngay = None
        if can_ngay == can_cung_thang: pham_ngay = "Khí Cùng của Tháng"
        if can_ngay == can_cuc_thang: pham_ngay = "Khí Cực của Tháng"

        return {
            "thang_pham": pham_thang,
            "ngay_pham": pham_ngay,
            "can_ky_thang": (can_cung_nam, can_cuc_nam),
            "can_ky_ngay": (can_cung_thang, can_cuc_thang)
        }
    
    res = kiem_tra_cung_cuc_ngay_hien_tai(nam_canchi, thang_canchi, ngay_canchi)
    
    st.markdown(f"Kiểm tra Khí Cùng Cực (**ngày {ngay_canchi}**)")
    
    # Hiển thị Cảnh báo cấp Tháng
    if res["thang_pham"]:
        st.error(f"⚠️ **CẢNH BÁO THÁNG:** Tháng {thang_canchi} đang phạm **{res['thang_pham']}** ({nam_canchi}).")
    else:
        st.success(f"✅ Tháng {thang_canchi} không vi phạm Khí Cùng Cực của năm {nam_canchi}.")

    # Hiển thị Cảnh báo cấp Ngày
    if res["ngay_pham"]:
        st.error(f"❌ **CẢNH BÁO NGÀY:** Ngày {ngay_canchi} đang phạm **{res['ngay_pham']}** ({thang_canchi}).")
        
        # TRƯỜNG HỢP TRÙNG LẶP (Cực Hung)
        if res["thang_pham"]:
            st.error("💀 **ĐẠI NẠN:** Ngày và Tháng cùng phạm Cùng Cực. Khí vận bị triệt tiêu hoàn toàn, tuyệt đối không hành sự.")
    else:
        st.success(f"✅ Ngày {ngay_canchi} không vi phạm Khí Cùng Cực của tháng {thang_canchi}.")

    # Hiển thị bảng tra nhanh Can kỵ
    with st.expander("🔍 Chi tiết Can kỵ cấp độ Khí"):
        st.write(f"- Năm {nam_canchi} kỵ tháng có Can: `{', '.join(res['can_ky_thang'])}`")
        st.write(f"- Tháng {thang_canchi} kỵ ngày có Can: `{', '.join(res['can_ky_ngay'])}`")


def check_ngay_ky_2026(ngay_thang_nam, content):
    """
    Kiểm tra thông tin ghi chú tại cột 11 từ dữ liệu content.
    - Nếu cột 11 có dữ liệu: Trả về thông tin để hiển thị.
    - Nếu cột 11 trống: Bỏ qua.
    """
    # Danh sách sao hung để bổ sung cảnh báo (tùy chọn)
    SAO_HUNG_LIST = ["Nguy", "Hư", "Nữ", "Bích", "Mão", "Sâm", "Quỷ", "Liễu", "Tinh", "Trương", "Dực"]

    for row in content:
        # So khớp ngày Dương lịch (Cột 0)
        if str(row[0]).strip() == str(ngay_thang_nam).strip():
            ghi_chu_ky = str(row[11]).strip()
            sao_ten = str(row[7]).strip()
                
            # Logic: Nếu cột 11 có nội dung HOẶC ngày đó phạm sao hung
            if ghi_chu_ky != "" or sao_ten in SAO_HUNG_LIST:
                return {
                    "co_thong_tin": True,
                    "ngay": row[0],
                    "noi_dung": ghi_chu_ky if ghi_chu_ky != "" else f"Phạm sao {sao_ten} (Hung)",
                    "sao": sao_ten,
                    "can_chi": row[4] # Lấy thêm can chi để hiển thị cho rõ ràng
                    }
                    
    return {"co_thong_tin": False}

def check_ngay_ky_sao_2026(ngay_thang_nam, content):
    
    def check_ngay_ky_2026(ngay_thang_nam, content):
        """
        Kiểm tra thông tin ghi chú tại cột 11 từ dữ liệu content.
        - Nếu cột 11 có dữ liệu: Trả về thông tin để hiển thị.
        - Nếu cột 11 trống: Bỏ qua.
        """
        # Danh sách sao hung để bổ sung cảnh báo (tùy chọn)
        SAO_HUNG_LIST = ["Cang", "Đê", "Tâm", "Ngưu", "Nữ", "Hư", "Mão", "Chủy", "Quỷ", "Liễu", "Dực"]

        for row in content:
            # So khớp ngày Dương lịch (Cột 0)
            if str(row[0]).strip() == str(ngay_thang_nam).strip():
                ghi_chu_ky = str(row[11]).strip()
                sao_ten = str(row[7]).strip()
                
                # Logic: Nếu cột 11 có nội dung HOẶC ngày đó phạm sao hung
                if ghi_chu_ky != "" or sao_ten in SAO_HUNG_LIST:
                    return {
                        "co_thong_tin": True,
                        "ngay": row[0],
                        "noi_dung": ghi_chu_ky if ghi_chu_ky != "" else f"Phạm sao {sao_ten} (Hung)",
                        "sao": sao_ten,
                        "can_chi": row[4] # Lấy thêm can chi để hiển thị cho rõ ràng
                    }
                    
        return {"co_thong_tin": False}

        # Giả sử ngay_dl_chon là ngày người dùng đang click vào xem
    res = check_ngay_ky_2026(ngay_thang_nam, content)

    if res["co_thong_tin"]:
        
        st.markdown(f"📋 Ghi chú Sao ngày {res['ngay']}")
        
        # Hiển thị Can Chi và Sao để người dùng dễ đối chiếu
        st.write(f"**Ngày:** {res['can_chi']} | **Sao:** {res['sao']}")
        
        # Hiển thị nội dung cảnh báo từ cột 11
        st.error(f"⚠️ {res['noi_dung']}")
        
        # Lời khuyên dựa trên sự hiện diện của nội dung
        if "Kỵ" in res['noi_dung'] or "Sát" in res['noi_dung']:
            st.caption("🚨 Đây là ngày có chỉ số hung cao, nên thận trọng tối đa.")

def kiem_tra_ngay_hien_tai_co_ky(ngay_thang_nam, ket_qua_tam_ky):
        """
        Đối soát ngày đang xem với danh sách Tam Kỳ hội tụ.
        - ngay_dl_dang_xem: Ngày Dương lịch cần kiểm tra (định dạng chuỗi khớp với cột 0, VD: "13/03/2026")
        - ket_qua_tam_ky: Biến 'ket_qua_ngay' trả về từ hàm he_thong_an_que_tam_ky
        """
        # Tìm kiếm ngày trong danh sách Tam Kỳ
        ngay_trung_khop = next((item for item in ket_qua_tam_ky if item["Ngày DL"] == ngay_thang_nam), None)
        
        if ngay_trung_khop:
            # Nếu trùng khớp, trả về thông tin chi tiết
            return {
                "is_ky": True,
                "mồng": ngay_trung_khop["Mồng"],
                "can_chi": ngay_trung_khop["Can Chi"],
                "cung": ngay_trung_khop["Cung"],
                "loai_ky": ngay_trung_khop["Gặp Kỳ"]
            }
        
        return {"is_ky": False}


def ngay_hien_tai_co_ky(ngay_thang_nam, ket_qua_ngay):
    
    def kiem_tra_ngay_hien_tai_co_ky(ngay_thang_nam, ket_qua_tam_ky):
        """
        Đối soát ngày đang xem với danh sách Tam Kỳ hội tụ.
        Sửa lỗi lệch ngày bằng cách chuẩn hóa dữ liệu đầu vào.
        """
        # 1. Chuẩn hóa chuỗi ngày nhập vào (Xóa khoảng trắng thừa)
        ngay_can_tim = str(ngay_thang_nam).strip()

        # 2. Tìm kiếm ngày trong danh sách Tam Kỳ
        # Sử dụng next với giá trị mặc định là None để tối ưu hiệu suất
        ngay_trung_khop = next(
            (item for item in ket_qua_tam_ky if str(item["Ngày DL"]).strip() == ngay_can_tim), 
            None
        )
        
        if ngay_trung_khop:
            return {
                "is_ky": True,
                "mồng": ngay_trung_khop.get("Mồng"),
                "can_chi": ngay_trung_khop.get("Can Chi"),
                "cung": ngay_trung_khop.get("Cung"),
                "loai_ky": ngay_trung_khop.get("Gặp Kỳ"),
                "tiet_khi": ngay_trung_khop.get("Tiết khí") # Bổ sung để kiểm tra mốc tiết
            }
        
        return {"is_ky": False}

    # Gọi hàm đối soát
    check_res = kiem_tra_ngay_hien_tai_co_ky(ngay_thang_nam, ket_qua_ngay)
    #st.write(check_res)
    
    if check_res["is_ky"]:
        # Hiển thị thông báo rực rỡ nếu là ngày Tam Kỳ
        st.success(f"🌟 **THÔNG BÁO: Hôm nay {ngay_thang_nam} Là ngày TAM KỲ Hội Tụ!**")
                    
        st.markdown(f"👉 Ngày **{check_res['can_chi']}** hội tụ thanh khí của **{check_res['loai_ky']} Kỳ** tại cung **{check_res['cung']}**. Đây là thời điểm tốt để hành sự theo hệ thống Bát Tiết.")
    else:
        # Thông báo nếu không phải ngày Tam Kỳ
        st.info(f"📅 Ngày {ngay_thang_nam} không nằm trong danh sách Gặp Kỳ của tháng này.")


def tinh_gio_quy_nhan_tu_content(ngay_dl_hien_tai, content_data):

        """
        ngay_dl_hien_tai: chuỗi định dạng "dd/mm/yyyy" khớp với cột 0
        content_data: mảng dữ liệu lịch từ file
        """
        lst_chi = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
        
        # Bảng mapping Nguyệt Tướng (Dựa theo ảnh bạn cung cấp)
        map_nguyet_tuong = {
            "Vũ Thủy": "Hợi", "Kinh Trập": "Hợi",
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


def cosodichly():
    st.sidebar.header("___PHƯƠNG PHÁP TÍNH:___")
    path_data1 = path_data("CoSoPhuongPhapTinh_short")

    # Sử dụng 'with st.sidebar' để nội dung của doc_file2 hiện ở bên trái
    with st.sidebar:
        doc_file2(path_data1)


def coso_phuongphaptinh():
    path_data2 = path_data("CoSoPhuongPhapTinh")    
    doc_file2(path_data2)



def nhap_CanChi_ngaysinh():
    # 1. Định nghĩa các nhóm Can và Chi (Loại bỏ "" bên trong các tuple phụ)
    duong_can = ("GIÁP", "BÍNH", "MẬU", "CANH", "NHÂM")
    am_can = ("ẤT", "ĐINH", "KỶ", "TÂN", "QUÝ")

    duong_chi = ("TÝ", "DẦN", "THÌN", "NGỌ", "THÂN", "TUẤT")
    am_chi = ("SỬU", "MÃO", "TỴ", "MÙI", "DẬU", "HỢI")

    # 2. Selectbox chọn Can
    nhap_canngaysinh = st.selectbox(
        "**Nhập CAN Ngày Sinh**", 
        ("", "GIÁP", "ẤT", "BÍNH", "ĐINH", "MẬU", "KỶ", "CANH", "TÂN", "NHÂM", "QUÝ"),
        key="sb_can"
    )

    # 3. Logic xác định danh sách Chi hiển thị (Đảm bảo chỉ có 1 giá trị rỗng ở đầu)
    if nhap_canngaysinh in duong_can:
        list_chi_hien_thi = ("",) + duong_chi
    elif nhap_canngaysinh in am_can:
        list_chi_hien_thi = ("",) + am_chi
    else:
        list_chi_hien_thi = ("",) + duong_chi + am_chi

    # 4. Selectbox chọn Chi
    nhap_chingaysinh = st.selectbox(
        "**Nhập CHI Ngày Sinh**", 
        options=list_chi_hien_thi,
        key="sb_chi"
    )

    # QUAN TRỌNG: Reset trạng thái trả lời nếu người dùng thay đổi Can/Chi
    # giúp tránh hiển thị kết quả cũ của ngày cũ
    if 'old_can' not in st.session_state:
        st.session_state.old_can = nhap_canngaysinh
    
    if st.session_state.old_can != nhap_canngaysinh:
        st.session_state.show_answer = False
        st.session_state.old_can = nhap_canngaysinh

    # Khởi tạo trạng thái trả lời
    if 'show_answer' not in st.session_state:
        st.session_state.show_answer = False

    # Nút TRẢ LỜI
    if st.button("**TRẢ LỜI**"):
        if nhap_canngaysinh and nhap_chingaysinh:
            st.session_state.show_answer = True
        else:
            st.error("Vui lòng chọn đầy đủ Can và Chi ngày sinh!")

    # Hiển thị nội dung khi show_answer = True
    if st.session_state.show_answer:
        # Giả sử lay_thong_tin trả về một list/tuple
        thongtin_TDST = lay_thong_tin(nhap_canngaysinh, "TuDaiSatThoi")
        
        #st.markdown('---')
        st.markdown(f'<span style="color: darkred; font-size: 18px;">**TỨ ĐẠI SÁT THỜI vận cá nhân**</span>', unsafe_allow_html=True)
        st.success(f"Bạn đã chọn Ngày sinh: **{nhap_canngaysinh} {nhap_chingaysinh}**")
        st.write(f"CAN Ngày Sinh **{nhap_canngaysinh}**: {thongtin_TDST[1]}")
        
        # Nút TIẾP TỤC xử lý bằng logic reset trạng thái
        if st.button("**TIẾP TỤC**"):
            st.balloons()
            st.warning("**Sau khi xem xét bản chất của Thời gian và Không gian, dùng bộ lọc vũ trụ để tìm ra những Ngày/Giờ có năng lượng tự nhiên nguyên thủy tốt nhất, loại bỏ sát khí vĩ mô. Ta mới đặt con người (Nhân) vào trong mối quan hệ tương tác sinh khắc, xem Nhân Mệnh có khả năng hấp thụ thời cơ đó hay không. Khí của tự nhiên (Trực Ngày) nằm trong sự kiểm soát dịch chuyển thời gian của Thiên Trực cùng định vị không gian Địa Trực và Khí của con người (Nhân Trực) đồng thanh tương ứng, đồng khí tương cầu thì vạn sự tất thành.\n\n Hẹn gặp lại Bạn ở phiên bản nâng cấp.**\n\n **XIN CẢM ƠN !!!**")
            # Tùy chọn: st.session_state.show_answer = False (để đóng lại sau khi cảm ơn)

    return nhap_canngaysinh, nhap_chingaysinh

