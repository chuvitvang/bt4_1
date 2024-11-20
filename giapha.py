import matplotlib.pyplot as plt
def gia_pha(n):
    ketqua = []
    value = 1
    for _ in range(n):
        ketqua.append(value)
        value *= 2
    return ketqua
def plot(data):
    plt.plot(data, marker='o', linestyle='-', color='b')
    plt.title("Biểu đồ gia phả theo từng thế hệ")
    plt.xlabel("Thế hệ")
    plt.ylabel("Số lượng người")
    # plt.grid(True)
    plt.show()

def main():
    so_nam = int(input("Nhập số năm: "))
    so_the_he = so_nam // int(input("Nhập số năm để sinh ra thế hệ mới (giả sử 30): "))
    list = gia_pha(so_the_he)
    print(list)
    plot(list)


main()

