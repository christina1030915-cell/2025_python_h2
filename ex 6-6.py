'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
# 請使用者輸入兩個數
num1_str = input("請輸入第一個數字：")
num2_str = input("請輸入第二個數字：")

num1 = float(num1_str)
num2 = float(num2_str)

# 判斷最大值
if num1 > num2:
    maximum = num1
else:
    maximum = num2

print(f"這兩個數字中的最大值為：{maximum}")
