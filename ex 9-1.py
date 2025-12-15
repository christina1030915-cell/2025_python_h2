'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# 提示使用者輸入兩個數字
num1_str = input("請輸入第一個數字: ")
num2_str = input("請輸入第二個數字: ")

try:
    # 將輸入轉換為浮點數以便比較
    num1 = float(num1_str)
    num2 = float(num2_str)

    if num1 > num2:
        maximum = num1
        print(f"最大值是: {maximum}")
    elif num2 > num1:
        maximum = num2
        print(f"最大值是: {maximum}")
    else:
        print("兩個數字相等。")
        
except ValueError:
    print("輸入錯誤：請輸入有效的數字。")
