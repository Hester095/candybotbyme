# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Решать через множества и еще каким-нибудь способом кроме множества
lst = list(map(int, input("Введите числа через пробел:\n").split()))


result = []
for char in lst:
    if lst.count(char) < 2:
        result.append(char)
print(result)

# print([i for i in lst if lst.count(i) == 1])

