'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import math

# 請使用者輸入半徑
r_str = input("請輸入圓的半徑（r）：")
r = float(r_str) # 將輸入的文字轉換成數字

# 判斷半徑是否有效
if r >= 0:
    area = math.pi * r * r         # 計算面積
    circumference = 2 * math.pi * r # 計算周長
    print(f"圓的面積為：{area:.2f}")        # 輸出面積，保留兩位小數
    print(f"圓的周長為：{circumference:.2f}")    # 輸出周長，保留兩位小數
else:
    print("錯誤：半徑必須大於或等於 0。") # 輸出錯誤提示
