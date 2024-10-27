eight_system = int(input("Введите число в восьмеричной системе (5 цифр): "))
five = eight_system // 10000
f = five * (8 ** 4)
four = ( eight_system // 1000) % 10
fo = four * (8 ** 3)
three = ( eight_system % 1000) // 100
t = three * (8 ** 2)
two = ( eight_system % 100) // 10
tw = two * (8 ** 1)
one = (eight_system % 10) 
o = one * (8 ** 0)
rez = f + fo + t + tw + o
print("Число в десятичной системе:", rez)
