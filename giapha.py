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
    plt.plot(data, marker='o', linestyle='-', color='b')
    plt.title(f"Biểu đồ gia phả theo từng thế hệ trong {so_nam} năm,với {thehe_tang} năm thêm 1 thế hệ")
    plt.xlabel("Thế hệ")
    plt.ylabel("Số lượng người")
    plt.grid(True)
    plt.show()

def inputfunc():
    while True:
        so_nam = input("Nhập số năm: ")
        if so_nam.isdigit() and (so_nam := int(so_nam)) > 0:
                thehe_tang = input("Nhập số năm để sinh ra thế hệ mới: ")
                if thehe_tang.isdigit() and (thehe_tang := int(thehe_tang)) >= 18:
                    so_the_he = so_nam // thehe_tang
                    return so_the_he,so_nam,thehe_tang
                else:
                    print("Số năm sinh ra thế hệ phải lớn hơn hoặc bằng 18 và là số nguyên")
        else:
            print("Số năm phải lớn hơn 0 và là số nguyên")

def main():
    so_the_he, so_nam, thehe_tang = inputfunc()
    thehe = poweroftwo(so_the_he)
    plot(thehe,so_nam,thehe_tang)

main()
