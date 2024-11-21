import matplotlib.pyplot as plt
def poweroftwo(n):
    ketqua = []  # Danh sách lưu số lượng thành viên mỗi thế hệ
    i = 0  # Khởi tạo thế hệ đầu tiên
    while i <= n:  # Tiếp tục cho đến thế hệ cuối cùng
        ketqua.append(2**i)  # Tăng trưởng theo hàm mũ
        i += 1  # Tăng thế hệ
    print(ketqua)
    return ketqua
    
def plot(data,so_nam,thehe_tang):
    plt.plot(data, marker='o', linestyle='-', color='b')  # Vẽ đồ thị đường với dấu tròn tại các điểm
    plt.title(f"Biểu đồ gia phả theo từng thế hệ trong {so_nam} năm,với {thehe_tang} năm thêm 1 thế hệ")
    plt.xlabel("Thế hệ")  #  trục X là "Thế hệ"
    plt.ylabel("Số lượng người") # trục  là "số lượng người"
    plt.grid(True) # Hiển thị lưới trên đồ thị
    plt.show() # hiển thị đồ thị

def inputfunc():
    while True:
        so_nam = input("Nhập số năm: ") 
        if so_nam.isdigit() and (so_nam := int(so_nam)) > 0:
            while True:
                thehe_tang = input("Nhập số năm để sinh ra thế hệ mới: ") # Nhập số năm tạo thế hệ mới
                if thehe_tang.isdigit() and (thehe_tang := int(thehe_tang)) >= 18: # Kiểm tra hợp lệ
                    so_the_he = so_nam // thehe_tang # tính số thế hệ ( số năm /  số năm tạo 1thế hệ)
                    return so_the_he,so_nam,thehe_tang # trả về các kết quả cần thiết
                else:
                    print("Số năm sinh ra thế hệ phải lớn hơn hoặc bằng 18 và là số nguyên")
        else:
            print("Số năm phải lớn hơn 0 và là số nguyên")

def main():
    so_the_he, so_nam, thehe_tang = inputfunc() #lấy giá trị từ hàm input
    thehe = poweroftwo(so_the_he) # tính số lượng người theo từng thế hệ
    plot(thehe,so_nam,thehe_tang) # vẽ đồ thị

main()
