'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import calendar

# 提示使用者輸入年份和月份
year_str = input("請輸入年份 (例如: 2023): ")
month_str = input("請輸入月份 (例如: 2): ")

try:
    year = int(year_str)
    month = int(month_str)

    # 檢查月份是否在有效範圍 (1-12)
    if 1 <= month <= 12 and year >= 0:
        # 使用 calendar.monthrange 函數獲取當月天數
        # monthrange 返回一個 tuple (該月第一天是星期幾, 該月天數)
        num_days = calendar.monthrange(year, month)[1]
        print(f"{year} 年 {month} 月有 {num_days} 天。")
    else:
        print("輸入錯誤：請輸入有效的年份和月份 (月份範圍 1-12)。")
except ValueError:
    # 處理非整數輸入的情況
    print("輸入錯誤：請輸入有效的整數作為年份和月份。")
