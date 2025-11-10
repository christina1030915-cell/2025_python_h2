'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# 整數 (Integer)
age = input("please input int number = ")
print("age = ",age)
print(type(age))

age = int(input("please input int number = "))
print("age = ",age)
print(type(age))

# 簡單的加法計算器
print("=== 簡單加法計算器 ===")

# 輸入第一個數字
num1 = float(input("請輸入第一個數字："))

# 輸入第二個數字
num2 = float(input("請輸入第二個數字："))

# 計算結果
result = num1 + num2

# 顯示結果
print(f"{num1} + {num2} = {result}")
