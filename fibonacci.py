from time import sleep
import matplotlib.pyplot as plt

def Fibonacci_Cal(n): 
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

def Fibonacci_Series():
    while True:
        n_input = input("Nhập số phần tử Fibonacci cần tính: ").strip()
        if n_input.isdigit() and (n := int(n_input)) > 0:
            sequence = Fibonacci_Cal(n)
            if len(sequence) > 100:
                print(f"Chuỗi Fibonacci quá dài, chỉ hiển thị 100 phần tử đầu tiên:\n{sequence[:100]}...")
            else:
                print(f"Chuỗi Fibonacci:\n{sequence}")
            return sequence
        else:
            print("Vui lòng nhập số nguyên dương lớn hơn 0.")

def plot_fibonacci(sequence):
    if len(sequence) < 2:
        print("Chuỗi phải có ít nhất 2 phần tử để vẽ.")
        return
    
    max_phantu = 50
    if len(sequence) > max_phantu:
        print(f"Số phần tử quá nhiều ({len(sequence)}), chỉ hiển thị {max_phantu} phần tử đầu tiên.")
    sequence = sequence[:max_phantu]
    
    plt.figure(figsize=(12, 6))
    
    # Line chart
    plt.subplot(1, 2, 1)
    plt.plot(sequence, marker='o', linestyle='-', color='b')
    plt.title("Biểu đồ Fibonacci - Line Chart")
    plt.xlabel("Chỉ số")
    plt.ylabel("Giá trị")
    
    total = sum(sequence)
    normalized_sequence = [x / total for x in sequence]
    
    # Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(normalized_sequence, labels=range(1, len(sequence) + 1), autopct='%1.1f%%', startangle=140)
    plt.title("Biểu đồ chuỗi Fibonacci - Pie Chart")
    
    plt.tight_layout()
    plt.show()

def Fibonacci_Program():
    while True:
        end = Fibonacci_Series()
        if input("Nhập 'end_Fibo' để thoát, nhấn bất kỳ phím nào để tiếp tục: ").strip() == "end_Fibo":
            print("Kết thúc chương trình.")
            return end
        print("Vui lòng chờ 3s.")
        sleep(3)

def main():
    ktmk()
    end = Fibonacci_Program()
    plot_fibonacci(end)

main()




