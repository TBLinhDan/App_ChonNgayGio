# Hàm chuyển đổi năm Dương Lịch sang năm Can Chi
def year(namDL):
    nam = 0
    if namDL==2025:
        nam=namDL+1
        lst_Can1 = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
        lst_Chi1 = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi']
        Can_index = nam % 10
        Chi_index = nam % 12
        CanChi =lst_Can1[Can_index] +" "+ lst_Chi1[Chi_index]
    else:
        nam = namDL
        lst_Can1 = ['Canh', 'Tân', 'Nhâm', 'Quý', 'Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ']
        lst_Chi1 = ['Thân', 'Dậu', 'Tuất', 'Hợi', 'Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', 'Mùi']
        Can_index = nam % 10
        Chi_index = nam % 12
        CanChi =lst_Can1[Can_index] +" "+ lst_Chi1[Chi_index]
    
    return(CanChi)
