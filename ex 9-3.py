'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import math

# 提示使用者輸入半徑並轉換為浮點數
r_str = input("請輸入圓的半徑 (r >= 0): ")

try:
    r = float(r_str)
    
    if r >= 0:
        # 計算面積 (Area = π * r^2) 和周長 (Perimeter = 2 * π * r)
        area = math.pi * r**2
        perimeter = 2 * math.pi * r
        # 輸出結果
        print(f"半徑為 {r} 的圓面積為: {area:.2f}") # 輸出保留兩位小數
        print(f"半徑為 {r} 的圓周長為: {perimeter:.2f}") # 輸出保留兩位小數
    else:
        # 半徑為負數時的提示資訊
        print("輸入錯誤：半徑必須大於或等於 0。")
except ValueError:
    # 處理非數字輸入的情況
    print("輸入錯誤：請輸入一個有效的數字。")
