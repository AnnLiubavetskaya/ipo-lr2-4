eight_system = input("Введите число в восьмеричной системе (5 цифр): ")
ten = 0
if len(eight_system) == 5:
  for i in range(5): # range для количества символов (в нашем случае 5)
    num = int(eight_system[i])
    ten += num * (8 ** (4 - i)) #вывод (8 ** (4 - i)) перевод с 8 в 10 систему
    print("Число в десятичной системе:", ten)
elif len(eight_system)<5:
     print("Вы ввели менее 5 символов")
else:
    print("Вы ввели более 5 символов")
