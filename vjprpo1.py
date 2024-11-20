from time import sleep
import matplotlib.pyplot as plt

def Fibonacci_Series(n): 
    sequence = [0, 1]   
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2]) 
           
    return sequence[:n] if n > 1 else sequence[:1]

def ktmk():
    password = "DH23HM"
    for i in range(3):
        matkhau = input(f"Lần thử {i + 1}/{3} - Nhập mật khẩu để vào chương trình: ")
        if matkhau.strip() == password:
            print("Đăng nhập thành công!")
            return
        else:
            if i < 2:
                print("Sai mật khẩu ,vui lòng thử lại.")
            else:
                print("sai 3 lần , thoát chương trình"), exit()

def Fibonacci_program():
    while True:
        n_input = input("Nhập số phần tử Fibonacci cần tính:\n")
        n = n_input
        if not n_input.isdigit() or int(n_input) <= 0:
            print("Giá trị nhập vào không hợp lệ. Số phần tử phải là một số nguyên dương và không phải ký tự.")
            continue
        n = int(n_input)
        sequence = Fibonacci_Series(n)
        print(f"Chuỗi fibonacci:\n{sequence}")

        n_out = input("Bạn có muốn kết thúc chương trình hay không? Nếu có, nhập: end_Fibo\n")
        if n_out.strip().lower() == "end_fibo":
            print("Kết thúc chương trình.")
            return sequence 
        else:
            print("Bạn đã chọn tiếp tục,vui lòng chờ 3s")
            sleep(3)

def plot_fibonacci(sequence):
    if len(sequence) <= 1:
        print("Chuỗi Fibonacci phải có ít nhất 2 phần tử để vẽ biểu đồ.")
        return
    
        # Biểu đồ Line chart
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(sequence, marker='o', linestyle='-', color='b')
    plt.title("Biểu đồ Fibonacci - Line Chart")
    plt.xlabel("Chỉ số")
    plt.ylabel("Giá trị")
        
        # Biểu đồ Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(sequence, labels=range(1, len(sequence) + 1), autopct='%1.1f%%', startangle=140)
    plt.title("Biểu đồ chuỗi Fibonacci - Pie Chart")
        
    # Hiển thị biểu đồ
    plt.tight_layout()
    plt.show()

    print("Lưu biểu đồ dưới dạng hình ảnh 'fibonacci_plot.png'.")
    plt.savefig("fibonacci_plot.png")


def main():
    ktmk()
    sequence = Fibonacci_program()
    plot_fibonacci(sequence)

main()
