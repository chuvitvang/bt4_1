from time import sleep
import matplotlib.pyplot as plt

def Fibonacci_Series(n): 
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2]) 
    return sequence[:n]

def ktmk():
    password = "DH23HM"
    for i in range(3):
        if input(f"Lần thử {i + 1}/3 - Nhập mật khẩu: ").strip() == password:
            print("Đăng nhập thành công!")
            return
        print("Sai mật khẩu." if i < 2 else "Sai 3 lần, thoát chương trình.")
    exit()

def Fibonacci_program():
    while True:
        n_input = input("Nhập số phần tử Fibonacci cần tính: ")
        if not n_input.isdigit() or (n := int(n_input)) <= 0:
            print("Vui lòng nhập số nguyên dương và lớn hơn 0")
            continue
        sequence = Fibonacci_Series(n)
        if len(sequence) > 100:
            print(f"Chuỗi Fibonacci quá dài ,chỉ hiển thị (100 phần tử đầu tiên):\n{sequence[:100]}...")
        else:
            print(f"Chuỗi Fibonacci:\n{sequence}")

        if input("Nhập 'end_Fibo' để thoát, nhấn bất kì để tiếp tục: ").strip() == "end_Fibo":
            print("Kết thúc chương trình.")
            return sequence
        print("Vui lòng chờ 3s.")
        sleep(3)

def plot_fibonacci(sequence):
    if len(sequence) < 2:
        print("Chuỗi phải có ít nhất 2 phần tử để vẽ.")
        return
    
    max_elements = 50
    if len(sequence) > max_elements:
        print(f"Số phần tử quá nhiều ({len(sequence)}),để tránh lỗi, chỉ hiển thị {max_elements} phần tử đầu tiên.")
    sequence = sequence[:max_elements]
    
    plt.figure(figsize=(12, 6))
    
    # Line chart
    plt.subplot(1, 2, 1)
    plt.plot(sequence, marker='o',linestyle='-', color='b')
    plt.title("Biểu đồ Fibonacci - Line Chart")
    plt.xlabel("Chỉ số")
    plt.ylabel("Giá trị")
    
    # Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(sequence, labels=range(1, len(sequence) + 1), autopct='%1.1f%%', startangle=140)
    plt.title("Biểu đồ chuỗi Fibonacci - Pie Chart")
    
    plt.tight_layout()
    plt.savefig("fibonacci_plot.png")
    plt.show()
    print("Lưu biểu đồ dưới dạng 'fibonacci_plot.png'.")

def main():
    ktmk()
    sequence = Fibonacci_program()
    if sequence:
        plot_fibonacci(sequence)

main()
