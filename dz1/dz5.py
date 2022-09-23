a = float(input('укажите номер четверти(от 1 до 4)'))

if a == 1:
    print('допустимые значения координат для точек этой четверти от 0 до + бесконечности по обеим осям')
elif a == 2:
    print('допустимые значения координат для точек этой четверти от 0 до + бесконечности по оси у и от 0 до - бесконечности по оси х')
elif a == 3:
    print('допустимые значения координат для точек этой четверти от 0 до - бесконечности по обеим осям')
elif a == 4:
    print('допустимые значения координат для точек этой четверти от 0 до + бесконечности по оси х и от 0 до - бесконечности по оси у')
else:
    if a > 4 or a<1:
        print('введите число от 1 до 4')
# def inputNumbers(x):
#     xy = ["X", "Y"]
#     a = []
#     for i in range(x):
#         is_OK = False
#         while not is_OK:
#             try:
#                 number = int(input(f"Введите координату по {xy[i]}: "))
#                 a.append(number)
#                 is_OK = True
#             except ValueError:
#                 print("Ты ошибся. Вводить надо целые числа!")
#     return a


# def calculateLengthSegment(a, b):
#     lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
#     return lengthSegment


# print("Введите координаты точки А")
# pointA = inputNumbers(2)
# print("Введите координаты точки В")
# pointB = inputNumbers(2)

# print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")