from time import sleep  # Nhập hàm sleep từ thư viện time để sử dụng việc tạm dừng chương trình
import matplotlib.pyplot as plt # thư viện matplotlib.pyplot để vẽ biểu đồ

def Fibonacci_Cal(n): #Tính toán chuỗi Fibonacci với n phần tử.
    sequence = [0, 1] # Khởi tạo chuỗi Fibonacci với hai phần tử đầu tiên
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2]) # Thêm phần tử tiếp theo bằng tổng hai phần tử cuối cùng
    return sequence[:n]# Trả về chuỗi Fibonacci với n phần tử


def ktmk():  
    password = "DH23HM"
    for i in range(3):
        if input(f"Lần thử {i + 1}/3 - Nhập mật khẩu: ").strip() == password:# KIỂM TRA MẬT KHẨU VỚI 3 LẦN THỬ
            print("Đăng nhập thành công!")#Nếu người dùng nhập đúng mật khẩu, in thông báo đăng nhập thành công và tiếp tục chương trình.
            return
        print("Sai mật khẩu." if i < 2 else "Sai 3 lần, thoát chương trình.")#Nếu sai, thông báo sai mật khẩu. Sau 3 lần sai, thoát chương trình
    exit()

def Fibonacci_Series():#Yêu cầu người dùng nhập số lượng phần tử Fibonacci cần tính và hiển thị chuỗi Fibonacci.
    while True:
        n_input = input("Nhập số phần tử Fibonacci cần tính: ").strip()
        if n_input.isdigit() and (n := int(n_input)) > 0: ## Kiểm tra đầu vào có phải số nguyên dương không
            sequence = Fibonacci_Cal(n)
            if len(sequence) > 100: # Kiểm tra độ dài chuỗi để hạn chế hiển thị
                print(f"Chuỗi Fibonacci quá dài, chỉ hiển thị 100 phần tử đầu tiên:\n{sequence[:100]}...")
            else:
                print(f"Chuỗi Fibonacci:\n{sequence}")
            return sequence
        else:
            print("Vui lòng nhập số nguyên dương lớn hơn 0.") # Thông báo lỗi nếu đầu vào không hợp lệ

def plot_fibonacci(sequence): # Vẽ biểu đồ chuỗi Fibonacci dưới dạng biểu đồ đường và biểu đồ tròn.
    if len(sequence) < 2:  # Thoát hàm nếu chuỗi không đủ phần tử
        print("Chuỗi phải có ít nhất 2 phần tử để vẽ.")
        return  
    
    max_phantu = 50 # Giới hạn số phần tử để vẽ
    if len(sequence) > max_phantu:
        print(f"Số phần tử quá nhiều ({len(sequence)}), chỉ hiển thị {max_phantu} phần tử đầu tiên.")
    sequence = sequence[:max_phantu] # Lấy n phần tử đầu tiên để vẽ
    
    plt.figure(figsize=(12, 6)) # kích thước của biểu đồ
    
    # Line chart # vẽ biểu đồ đường
    plt.subplot(1, 2, 1) # Chia biểu đồ thành 1 hàng, 2 cột, và chọn ô thứ 1
    plt.plot(sequence, marker='o', linestyle='-', color='b') # Vẽ chuỗi Fibonacci với các điểm đánh dấu
    plt.title("Biểu đồ Fibonacci - Line Chart") # TÊN BIỂU ĐỒ
    plt.xlabel("Chỉ số")
    plt.ylabel("Giá trị")
     # Tính tổng các phần tử để chuẩn hóa cho biểu đồ tròn
    total = sum(sequence)
    normalized_sequence = [x / total for x in sequence]
    
    # Pie chart # Vẽ biểu đồ tròn 
    plt.subplot(1, 2, 2) # Chọn ô thứ 2 trong bố cục 1 hàng, 2 cột. 
    plt.pie(normalized_sequence, labels=range(1, len(sequence) + 1), autopct='%1.1f%%', startangle=140)
    plt.title("Biểu đồ chuỗi Fibonacci - Pie Chart") # TÊN BIỂU ĐỒ
    
    plt.tight_layout()#điều chỉnh khoảng cách giữa các phần tử trong biểu đồ
    plt.show() # hiển thị biểu đồ

def Fibonacci_Program(): #hàm kết thúc hay khoong
    while True: 
        if input("Nhập 'end_Fibo' để thoát, nhấn bất kỳ phím nào để tiếp tục: ").strip() == "end_Fibo":
            print("Kết thúc chương trình.")
            return True
        else:
            print("Vui lòng chờ 3s.")
            sleep(3)
            return
def main():
    ktmk() # Kiểm tra mật khẩu trước khi tiếp tục
    while True:
         end = Fibonacci_Series()
         if Fibonacci_Program() == True:
            break

    plot_fibonacci(end) # Vẽ biểu đồ chuỗi Fibonacci cuối cùng

# Gọi hàm main để bắt đầu chương trình
main()

