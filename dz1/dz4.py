x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z '))
for x in range(2):
        for y in range(2):
            for z in range(2):
                print(not (x or y or z) == (not x and not y and not z))
                print(x, y, z)
# x = int(input("Введите координату x: "))
# y = int(input("Введите координату y: "))
# if x > 0 and y > 0:
#     print("1 четверть")
# elif x < 0 and y > 0:
#     print("2 четверть")
# elif x < 0 and y < 0:
#     print("3 четверть")
# elif x > 0 and y < 0:
#     print("4 четверть")
# elif x == 0:
#     print("Точка на оси Y")
# else:
#     print("Точка на оси X")