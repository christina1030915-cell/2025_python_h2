'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# 請使用者輸入年和月
year_str = input("請輸入年份（例如：2023）：")
month_str = input("請輸入月份（1-12）：")

year = int(year_str)
month = int(month_str)

# 判斷月份天數
if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month in (4, 6, 9, 11):
    days = 30
elif month == 2:
    # 判斷是否為閏年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days = 29
    else:
        days = 28
else:
    # 處理無效的月份輸入
    days = "無效的月份"

print(f"{year} 年 {month} 月的天數為：{days}")
