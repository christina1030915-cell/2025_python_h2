'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
fruits = ["apple", "banana", "cherry"]
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[2])

fruits[2] = "grape"

print(fruits[2])
print(fruits)

for f in fruits:
    print(f)
    
for i in range(len(fruits)):
    print(i,":",fruits[i])
