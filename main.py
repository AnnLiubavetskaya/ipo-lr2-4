eight_system = input("Введите число в восьмеричной системе (5 цифр): ")
ten_system = (int(eight_system[0]) * 8**4 +
int(eight_system[1]) * 8**3 +
int(eight_system[2]) * 8**2 +
int(eight_system[3]) * 8**1 +
int(eight_system[4]) * 8**0)
print("Число в десятичной системе:", ten_system)
