number_a = float(input('введите число '))
print (f'кратно ли оно 5 и 10 или 15 но не 30: {(not number_a % 5 and not number_a % 10 or not number_a % 15) and (number_a % 30 != 0)} ')
# day = int(input('Введите номер дня недели '))
# if day > 7 or day < 1:
#      print('Пожалуйста, введите правильный номер')
# elif day == 6 or day == 7:
#      print("выходной")
# else:  
#      print("рабочий")