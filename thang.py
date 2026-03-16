def stt_thangam(ngay,thang,nam):
    stt = 0
    songay = 0
    if nam == 2026:
        if thang == 1:
            songay = 10 + ngay
        elif thang == 2:
            songay = 10 + 31 + ngay
        elif thang == 3:
            songay = 10+31+28+ngay
        elif thang == 4:
            songay = 10+31+28+31+ngay
        elif thang == 5:
            songay = 10+31+28+31+30+ngay
        elif thang == 6:
            songay = 10+31+28+31+30+31+ngay
        elif thang == 7:
            songay = ngay+10+31+28+31+30+31+30
        elif thang == 8:
            songay = ngay+10+31+28+31+30+31+30+31
        elif thang == 9:
            songay = ngay+10+31+28+31+30+31+30+31+31
        elif thang == 10:
            songay = ngay+10+31+28+31+30+31+30+31+31+30
        elif thang == 11:
            songay = ngay+10+31+28+31+30+31+30+31+31+30+31
        elif thang == 12:
            songay = ngay+10+31+28+31+30+31+30+31+31+30+31+30
    else:
        if 21<ngay<=31:
            songay = (ngay - 22)+1
        else:
            songay==0
    
    if 0<songay < 31:
        stt = 1
    elif 30<songay < 62:
        stt = 2
    elif 61<songay < 93:
        stt = 3
    elif 92<songay < 123:
        stt = 4   
    elif 122<songay < 153:
        stt = 5 
    elif 152<songay < 184:
        stt = 6
    elif 183<songay < 214:
        stt = 7
    elif 213<songay < 245:
        stt = 8
    elif 244<songay < 275:
        stt = 9
    elif 275<songay < 306:
        stt = 10
    elif 305<songay < 336:
        stt = 11
    elif 335<songay < 367:
        stt = 12
    elif songay == 0:
        stt = 0

    return int(stt)

def stt_ngay(ngay,thang,nam):
    stt = 0
    songay = 0
    if nam == 2026:
        if thang == 1:
            songay = 10 + ngay
        elif thang == 2:
            songay = 10 + 31 + ngay
        elif thang == 3:
            songay = 10+31+28+ngay
        elif thang == 4:
            songay = 10+31+28+31+ngay
        elif thang == 5:
            songay = 10+31+28+31+30+ngay
        elif thang == 6:
            songay = 10+31+28+31+30+31+ngay
        elif thang == 7:
            songay = ngay+10+31+28+31+30+31+30
        elif thang == 8:
            songay = ngay+10+31+28+31+30+31+30+31
        elif thang == 9:
            songay = ngay+10+31+28+31+30+31+30+31+31
        elif thang == 10:
            songay = ngay+10+31+28+31+30+31+30+31+31+30
        elif thang == 11:
            songay = ngay+10+31+28+31+30+31+30+31+31+30+31
        elif thang == 12:
            songay = ngay+10+31+28+31+30+31+30+31+31+30+31+30
    else:
        if 21<ngay<=31:
            songay = (ngay - 22)+1
        else:
            songay==0
    
    if 0<songay < 62:
        stt = songay
    elif 61<songay < 123:
        stt = songay-61   
    elif 122<songay < 184:
        stt = songay-122
    elif 183<songay < 245:
        stt = songay-183
    elif 244<songay < 306:
        stt = songay-244
    elif 305<songay < 367:
        stt = songay-305
    elif songay == 0:
        stt = 0

    return int(stt)

def tiet_khi(ngay,thang,nam):
    stt = 0
    songay = 0
    if nam == 2026:
        if thang == 1:
            songay = 10 + ngay
        elif thang == 2:
            songay = 10 + 31 + ngay
        elif thang == 3:
            songay = 10+31+28+ngay
        elif thang == 4:
            songay = 10+31+28+31+ngay
        elif thang == 5:
            songay = 10+31+28+31+30+ngay
        elif thang == 6:
            songay = 10+31+28+31+30+31+ngay
        elif thang == 7:
            songay = ngay+10+31+28+31+30+31+30
        elif thang == 8:
            songay = ngay+10+31+28+31+30+31+30+31
        elif thang == 9:
            songay = ngay+10+31+28+31+30+31+30+31+31
        elif thang == 10:
            songay = ngay+10+31+28+31+30+31+30+31+31+30
        elif thang == 11:
            songay = ngay+10+31+28+31+30+31+30+31+31+30+31
        elif thang == 12:
            songay = ngay+10+31+28+31+30+31+30+31+31+30+31+30
    else:
        if 21<ngay<=31:
            songay = (ngay - 22)+1
        else:
            songay==0
    
    if 0<songay < 16:
        stt = "Đông Chí"
    elif 15<songay < 31:
        stt = "Tiểu Hàn"
    elif 30<songay < 46:
        stt = "Đại Hàn"
    elif 45<songay < 62:
        stt = "Lập Xuân"   
    elif 61<songay < 77:
        stt = "Vũ Thuỷ" 
    elif 76<songay < 92:
        stt = "Kinh Trập"
    elif 91<songay < 107:
        stt = "Xuân Phân"
    elif 106<songay < 123:
        stt = "Thanh Minh"
    elif 122<songay < 138:
        stt = "Cốc Vũ"
    elif 137<songay < 153:
        stt = "Lập Hạ"
    elif 152<songay < 168:
        stt = "Tiểu Mãn"
    elif 167<songay < 184:
        stt = "Mang Chủng"
    elif 183<songay < 199:
        stt = "Hạ Chí"
    elif 198<songay < 214:
        stt = "Tiểu Thử"
    elif 213<songay < 229:
        stt = "Đại Thử"   
    elif 228<songay < 245:
        stt = "Lập Thu" 
    elif 244<songay < 260:
        stt = "Xử Thử"
    elif 259<songay < 275:
        stt = "Bạch Lộ"
    elif 274<songay < 290:
        stt = "Thu Phân"
    elif 289<songay < 306:
        stt = "Hàn Lộ"
    elif 305<songay < 321:
        stt = "Sương Giáng"
    elif 320<songay < 336:
        stt = "Lập Đông"
    elif 335<songay < 351:
        stt = "Tiểu Tuyết"
    elif 350<songay < 366:
        stt = "Đại Tuyết"
    
    elif songay == 0:
        stt = 0

    return (stt)
    
    
#tách riêng Thiên Can ra khỏi tên Can Chi năm
def lay_thien_can(canchi):
    # Kiểm tra nếu input hợp lệ
    if not canchi or ' ' not in canchi.strip():
        return None # Hoặc trả về giá trị mặc định
        
    HG = canchi.title() #đảm bảo rằng chữ cái đầu của mỗi từ trong chuỗi y đều được viết hoa
    lst = HG.split(' ') #cắt chuỗi HG thành một danh sách (list) tại vị trí có khoảng trắng.
    #lst = HG.split() # Tự động xử lý bất kỳ số lượng khoảng trắng nào
    return lst[0]

def lay_dia_chi(canchi):
    # Kiểm tra nếu input hợp lệ
    if not canchi or ' ' not in canchi.strip():
        return None # Hoặc trả về giá trị mặc định
        
    HG = canchi.title() #đảm bảo rằng chữ cái đầu của mỗi từ trong chuỗi y đều được viết hoa
    lst = HG.split(' ') #cắt chuỗi HG thành một danh sách (list) tại vị trí có khoảng trắng.
    #lst = HG.split() # Tự động xử lý bất kỳ số lượng khoảng trắng nào
    return lst[1]

def thanggieng(Can_năm):   # Gán Can_năm làm thông số đầu vào Hàm Thanggieng
    match Can_năm:  # Tuy Can Năm mà suy ra Can của tháng 1_Dần
        case "Giáp":
            return "Bính Dần"
        case "Kỷ":
            return "Bính Dần"
        case "Ất":
            return "Mậu Dần"
        case "Canh":
            return "Mậu Dần"
        case "Bính":
            return "Canh Dần"
        case "Tân":
            return "Canh Dần"
        case "Đinh":
            return "Nhâm Dần"
        case "Nhâm":
            return "Nhâm Dần"
        case "Mậu":
            return "Giáp Dần"
        case _:
            return "Giáp Dần"

# Từ Tháng Giêng tìm ra DS 12 tháng trong năm từ tháng Tý
def Lst_thang(HG):
    lst_HG = ['Giáp Tý', 'Ất Sửu', 'Bính Dần', 'Đinh Mão', 'Mậu Thìn', 'Kỷ Tỵ', 'Canh Ngọ', 'Tân Mùi', 'Nhâm Thân', 'Quý Dậu',
                'Giáp Tuất', 'Ất Hợi', 'Bính Tý', 'Đinh Sửu', 'Mậu Dần', 'Kỷ Mão', 'Canh Thìn', 'Tân Tỵ', 'Nhâm Ngọ', 'Quý Mùi',
                'Giáp Thân', 'Ất Dậu ', 'Bính Tuất', 'Đinh Hợi', 'Mậu Tý', 'Kỷ Sửu', 'Canh Dần', 'Tân Mão', 'Nhâm Thìn', 'Quý Tỵ',
                'Giáp Ngọ', 'Ất Mùi', 'Bính Thân', 'Đinh Dậu', 'Mậu Tuất', 'Kỷ Hợi', 'Canh Tý', 'Tân Sửu', 'Nhâm Dần', 'Quý Mão',
                'Giáp Thìn', 'Ất Tỵ', 'Bính Ngọ', 'Đinh Mùi', 'Mậu Thân', 'Kỷ Dậu', 'Canh Tuất', 'Tân Hợi', 'Nhâm Tý', 'Quý Sửu',
                'Giáp Dần', 'Ất Mão', 'Bính Thìn', 'Đinh Tỵ', 'Mậu Ngọ', 'Kỷ Mùi', 'Canh Thân', 'Tân Dậu', 'Nhâm Tuất', 'Quý Hợi']

    idx_goc = lst_HG.index(HG) # Tìm vị trí index) của năm HG trong danh sách lst_HG (60 cặp Can-Chi).
    start_idx = (idx_goc - 2) % 60 # Từ stt của Can Chi (Tháng Dần -2) tính stt của Tháng Tý
    """Sử dụng logic modulo để không bao giờ bị lỗi tràn danh sách. 
        Toán tử % 60 (Modulo): Đây là kỹ thuật "xoay vòng" 60
        Nếu kết quả của idx_goc - 2 bị âm (ví dụ: năm đầu tiên "Giáp Tý" ở vị trí 0, trừ 2 thành -2), 
        phép toán % 60 sẽ tự động đưa nó về cuối danh sách (vị trí 58). 
        Nó đảm bảo chỉ số luôn nằm trong phạm vi hợp lệ của danh sách 60 Hoa Giáp."""
    lst12 = []
    for i in range(12):
          # (start_idx + i) % 60 đảm bảo luôn nằm trong khoảng 0-59
        lst12.append(lst_HG[(start_idx + i) % 60])
    return lst12

# Hàm Tính Can giờ Tý theo Can Ngày nhập vào string
def tim_gio_Ty(can_ngay):   
    match can_ngay:  # Tuy Can Năm mà suy ra Can của tháng 1_Dần
        case "Giáp":
            return "Giáp Tý"
        case "Kỷ":
            return "Giáp Tý"
        case "Ất":
            return "Bính Tý"
        case "Canh":
            return "Bính Tý"
        case "Bính":
            return "Mậu Tý"
        case "Tân":
            return "Mậu Tý"
        case "Đinh":
            return "Canh Tý"
        case "Nhâm":
            return "Canh Tý"
        case "Mậu":
            return "Nhâm Tý"
        case _:
            return "Nhâm Tý"


def tao_ds_12_gio(gio_ty_khoi):
    """
    Tạo danh sách 12 giờ bắt đầu từ giờ Tý tìm được.
    Sử dụng toán tử % 60 để xoay vòng danh sách Hoa Giáp an toàn.
    """
    # Danh sách 60 Hoa Giáp chuẩn
    lst_data = [
                'Giáp Tý', 'Ất Sửu', 'Bính Dần', 'Đinh Mão', 'Mậu Thìn', 'Kỷ Tỵ', 'Canh Ngọ', 'Tân Mùi', 'Nhâm Thân', 'Quý Dậu',
                'Giáp Tuất', 'Ất Hợi', 'Bính Tý', 'Đinh Sửu', 'Mậu Dần', 'Kỷ Mão', 'Canh Thìn', 'Tân Tỵ', 'Nhâm Ngọ', 'Quý Mùi',
                'Giáp Thân', 'Ất Dậu ', 'Bính Tuất', 'Đinh Hợi', 'Mậu Tý', 'Kỷ Sửu', 'Canh Dần', 'Tân Mão', 'Nhâm Thìn', 'Quý Tỵ',
                'Giáp Ngọ', 'Ất Mùi', 'Bính Thân', 'Đinh Dậu', 'Mậu Tuất', 'Kỷ Hợi', 'Canh Tý', 'Tân Sửu', 'Nhâm Dần', 'Quý Mão',
                'Giáp Thìn', 'Ất Tỵ', 'Bính Ngọ', 'Đinh Mùi', 'Mậu Thân', 'Kỷ Dậu', 'Canh Tuất', 'Tân Hợi', 'Nhâm Tý', 'Quý Sửu',
                'Giáp Dần', 'Ất Mão', 'Bính Thìn', 'Đinh Tỵ', 'Mậu Ngọ', 'Kỷ Mùi', 'Canh Thân', 'Tân Dậu', 'Nhâm Tuất', 'Quý Hợi'
                ]
    try:
        start_idx = lst_data.index(gio_ty_khoi)
        # Lấy 12 phần tử kế tiếp, dùng modulo để quay vòng nếu chạm cuối danh sách
        return [lst_data[(start_idx + i) % 60] for i in range(12)]
    except ValueError:
        return None

# Tính Giờ Thực Địa Phương
def xu_ly_thoi_gian_thuc_dia(tinh_chon, h_moc_chuan, p_moc_chuan, data_kinh_do):
    """
    Tính mốc Tý thực địa từ tỉnh được chọn.
    """
    kinh_do = data_kinh_do.get(tinh_chon, 105.0) #truy cập vào danh sách (dictionary) data_kinh_do để lấy số kinh độ của tỉnh mà người dùng đã chọn (tinh_chon).
    lech_phut = (kinh_do - 105.0) * 4 #sự chênh lệch thời gian giữa địa phương và múi giờ chuẩn quốc gia
    
    phut_ty_chuan = h_moc_chuan * 60 + p_moc_chuan
    moc_ty_thuc_phut = (phut_ty_chuan - lech_phut) % 1440
    h_ty_thuc = int(moc_ty_thuc_phut // 60)     #Chia lấy phần nguyên để ra số giờ.
    p_ty_thuc = int(moc_ty_thuc_phut % 60)      #Chia lấy phần dư để ra số phút lẻ.
    
    return h_ty_thuc, p_ty_thuc     #mốc thời gian mà giờ Tý thực sự bắt đầu tại tỉnh đó.

def quy_doi_gio_can_chi(h_hien_tai, p_hien_tai, h_moc_ty, p_moc_ty, ds_12_gio):
    """
    Quy đổi giờ phút thực tế sang giờ Can Chi dựa trên mốc khởi Tý tùy chỉnh.
    - h_hien_tai, p_hien_tai: Giờ và phút lúc bấm quẻ.
    - h_moc_ty, p_moc_ty: Giờ và phút bắt đầu giờ Tý của ngày đó.
    - ds_12_gio: Danh sách 12 giờ Can Chi khởi từ Tý.
    """
    if not ds_12_gio:
        return "Lỗi danh sách"

    # 1. Chuyển tất cả sang đơn vị phút tính từ 00:00
    phut_hien_tai = int(h_hien_tai) * 60 + int(p_hien_tai)
    phut_bat_dau_ty = int(h_moc_ty) * 60 + int(p_moc_ty)

    # 2. Tính khoảng cách phút từ mốc Tý đến hiện tại
    # Nếu giờ hiện tại nhỏ hơn mốc Tý (vd: 1h sáng < 23h đêm), 
    # ta hiểu là đã sang ngày mới, cộng thêm 1440 phút (24h).
    if phut_hien_tai < phut_bat_dau_ty:
        khoang_cach = phut_hien_tai + (1440 - phut_bat_dau_ty)
    else:
        khoang_cach = phut_hien_tai - phut_bat_dau_ty

    # 3. Chia cho 120 phút để tìm vị trí (index) từ 0 đến 11
    idx = (khoang_cach // 120) % 12

    return ds_12_gio[idx]

# chuyển đổi một con số (số thứ tự ngày) thành tên Can Chi tương ứng.
def tinh_can_ngay (stt_ngày):
    if 1 <= stt <= 60: # Sử dụng logic lấy dư trực tiếp và căn chỉnh mảng
        can_idx = (stt - 1) % 10
        chi_idx = (stt - 1) % 12
        lst_Can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']    
        lst_Chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
        ngay_can_chi = f"{lst_Can[can_idx]} {lst_Chi[chi_idx]}"
        st.write(f"\nNgày {ngay_cantinh}: {ngay_can_chi}")
        can = lst_Can[can_idx]
    elif stt == 61 or stt == 0: # Trường hợp đặc biệt cuối chu kỳ
        st.write(f"\nNgày {ngay_cantinh}: Quý Hợi")
        can = "Quý"

def stt_CanChi(stt):
    if 1 <= stt <= 60: # Sử dụng logic lấy dư trực tiếp và căn chỉnh mảng
        can_idx = (stt - 1) % 10
        chi_idx = (stt - 1) % 12
        lst_Can = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']    
        lst_Chi = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
        can_chi = f"{lst_Can[can_idx]} {lst_Chi[chi_idx]}"
    elif stt == 61 or stt == 0: # Trường hợp đặc biệt cuối chu kỳ
        can_chi == "Quý Hợi"
    return can_chi
