eight_system = input("Введите число в восьмеричной системе (5 цифр): ")    
ten_system = 0  
if len(eight_system)==5:
    for i in range(5):
        number = int(eight_system[i])  
        ten_system += number * (8 ** (4 - i))
    print("Число в десятичной системе:", ten_system)
elif len(eight_system)<5:
     print("Вы ввели менее 5 мимволов")
else:
    print("Вы ввели более 5 мимволов")