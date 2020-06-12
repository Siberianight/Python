


# 1. Задание
name = 'Alex'
age = 21#

print(name) # строковый тип данных
print(age) # числовой тип данных

# 1.1
number = int(input('Введите число от 0 до 100: '))
color = input('Напишите Ваш любимый цвет: ')
print(number)
print(color)

# 2. Задание
time = int(input("Введите время в секундах "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс   {hours} : {minutes} : {seconds}")



# 3. Задание
n = input('Введите число: ')
n_n = n + n
n_n_n = n + n + n
result = int(n) + int(n_n) + int(n_n_n)
print(result)

# 4. Задание
n = abs(int(input("Введите целое положительное число ")))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Максимальное цифра в числе ", max)
        break

# 5. Задание
proceeds = int(input('Введите выручку фирмы: '))
costs  = int(input('Введите издержки фирмы: '))
revenue = proceeds - costs
worker = int(input('Введите численность сотрудников: '))
worker_income = revenue / worker

if proceeds > costs:
    print('В этом месяце прибыль больше издержек')
else:
    print('В этом месяце издержки больше прибыли')
result = 'Доход вашей фирмы составил {} рублей\n' \
         'Заработная плата сотрудника {} рублей' .format(revenue, worker_income)
print(result)

# 6. Задание
a = 2 # результат первого дня в км
b = 3 # требуемый результат в км
d = 1 # день

while b > a:
    a = a * 1.1
    d += 1

result = 'Спортсмен добъется заданного результата через {} дней, и он составит {} километра'.format(d, a)
print(result)

